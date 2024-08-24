from flask import Flask, request, jsonify
import logging
import os
from werkzeug.utils import secure_filename
import speech_recognition as sr
from pydub import AudioSegment
from fpdf import FPDF
from groq import Groq
import google.generativeai as genai
import Prompts

import assemblyai as aai

# Inicializa o Flask
app = Flask(__name__)

# Configurações de API
GROQ_API_KEY = "Your key"
client = Groq(api_key=GROQ_API_KEY)
genai.configure(api_key="Your key")

ASSEMBLYAI_API_KEY = "Your key"
aai.settings.api_key = ASSEMBLYAI_API_KEY

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurações de upload de arquivo 
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'gsm', 'mp3', 'flac'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Carrega os prompts
prompts = Prompts.prompts





# Funções auxiliares 
#--------------------------------------------------------------------------------#

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_to_flac(input_file):
    audio = AudioSegment.from_file(input_file)
    flac_filename = os.path.splitext(input_file)[0] + ".flac"
    audio.export(flac_filename, format="flac")
    return flac_filename

def save_chunk(chunk, index, output_dir='chunks'):
    os.makedirs(output_dir, exist_ok=True)
    chunk_filename = os.path.join(output_dir, f"chunk_{index}.flac")
    chunk.export(chunk_filename, format="flac")
    return chunk_filename

def run_groq(prompt, text):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": f"{text}: {prompt}"}],
            model="llama3-70b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        logger.error(f"Error in Groq processing: {e}")
        return None

def run_gemini(prompt, text):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(f"{text}: {prompt}")
        return response.text
    except Exception as e:
        logger.error(f"Error in Gemini processing: {e}")
        return "An error occurred while processing the request with the fallback LLM."

def validate_input(keyword, text):
    if not keyword or keyword not in prompts:
        logger.error("Invalid keyword provided.")
        return False, "Invalid keyword. Please provide a valid keyword."
    if not text or len(text.strip()) == 0:
        logger.error("Empty or invalid text provided.")
        return False, "Text cannot be empty. Please provide valid text."
    return True, ""

def run_with_fallback(prompt, text):
    result = run_groq(prompt, text)
    if not result or len(result.strip()) == 0:
        logger.warning("Erro ao utilizar a Groq, utilizando o Gemini.")
        result = run_gemini(prompt, text)
    return result




# Rotas da aplicação combinada
#--------------------------------------------------------------------------------#

# realiza a transcrição do audio.
@app.route('/transcribe', methods=['POST'])
def transcrever_audio():
    try:
        if 'audio' not in request.files:
            return jsonify({"error": "Nenhum arquivo de áudio encontrado"}), 400

        files = request.files.getlist('audio')
        transcricoes = []

        for file in files:
            if file.filename == '':
                return jsonify({"error": "Nenhum arquivo selecionado"}), 400

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)

                if filepath.endswith('.gsm') or filepath.endswith('.mp3'):
                    filepath = convert_to_flac(filepath)

                audio_segment = AudioSegment.from_file(filepath)
                chunk_length_ms = 120000
                chunks = [audio_segment[i:i + chunk_length_ms] for i in range(0, len(audio_segment), chunk_length_ms)]

                recognizer = sr.Recognizer()
                full_transcript = ""

                for i, chunk in enumerate(chunks):
                    chunk_filename = save_chunk(chunk, i)
                    with sr.AudioFile(chunk_filename) as source:
                        audio_data = recognizer.record(source)
                    texto = recognizer.recognize_google(audio_data, language='pt-BR')
                    full_transcript += texto + "\n"
                    os.remove(chunk_filename)

                transcricao_dir = 'transcricoes'
                os.makedirs(transcricao_dir, exist_ok=True)
                transcricao_filename = f"transcricao_{filename}.pdf"
                transcricao_path = os.path.join(transcricao_dir, transcricao_filename)

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                for line in full_transcript.split("\n"):
                    pdf.multi_cell(0, 10, line)
                pdf.output(transcricao_path)

                transcricoes.append({"filename": filename, "transcription": full_transcript, "file_path": transcricao_path})

            else:
                return jsonify({"error": f"Tipo de arquivo inválido para o arquivo {file.filename}"}), 400

        return jsonify(transcricoes)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

#analisa individualmente as transcrições  
@app.route('/analyze', methods=['POST'])
def analisar_transcricao():
    try:
        transcricoes = request.json.get('transcricoes', [])

        if not transcricoes:
            return jsonify({"error": "Nenhuma transcrição fornecida"}), 400

        analisadas = []
        for transcricao in transcricoes:
            prompt = f"faça um resumo da interação: {transcricao}"

            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": f"{prompt}"}],
                model="llama3-70b-8192",
            )
            analise = chat_completion.choices[0].message.content

            analisadas.append({'transcricao': transcricao, 'analise': analise})

        return jsonify({"analisadas": analisadas})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# response como uma auditoria do ticket
#recebe o payload simples ou um array com transcrições 
@app.route('/context', methods=['POST'])
def analisar_transcricao2():
    try:
        transcricoes = request.json.get('transcricoes', [])

        if not transcricoes:
            return jsonify({"error": "Nenhuma transcrição fornecida"}), 400

        texto_completo = "\n".join(transcricoes)
        prompt = f"faça um resumo da interação: {texto_completo}"

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": f"{prompt}"}],
            model="llama3-70b-8192",
        )
        analise = chat_completion.choices[0].message.content

        return jsonify({"analise": analise})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

 
#processa a requisilção de acordo com a palavra chave
@app.route('/process', methods=['POST'])
def process_request():
    data = request.json
    keyword = data.get("keyword")
    text = data.get("text")
    
    is_valid, error_message = validate_input(keyword, text)
    if not is_valid:
        return jsonify({"error": error_message}), 400
    
    if keyword in prompts:
        prompt = prompts[keyword]
        result = run_with_fallback(prompt, text)
    else:
        logger.info("Keyword not recognized, using default handling.")
        result = run_gemini(f"Process the following text: {text}", text)
    
    return jsonify({"result": result})





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
