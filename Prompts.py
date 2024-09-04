prompts = {
    "sentimento":'''
                "realize uma análise profunda e detalhada." \
                "do sentimento do cliente e do atendente expresso no texto delimitado por {}, "\
                "classifique o sentimento de cada um como: 'positivo', 'negativo' ou 'neutro'. "\
                "Identifique e liste os sentimentos específicos presentes, "\
                "em sua forma mais simples e direta (palavra primitiva)" \
                "tanto explícitos quanto implícitos, e avalie a intensidade de cada sentimento somados dentro de uma escala total de 0 (zero) a 100 (cem) em porcentagem(%). "\
                "Indique quais palavras-chave na sentença contribuíram " \
                "para os sentimentos identificados. "\
                "Além disso, sugira possíveis razões para esses sentimentos "\
                "com base na conversa. Por fim, explique como você chegou " \
                "a essas conclusões. Retorne todas essas informações em português do Brasil " \
                "no seguinte formato de um objeto JSON respeitando a estrutura para cliente e atendente:: " \
                "{" \
                    "\"role_cliente\": \"cliente\"," \
                    "\"classe_cliente\": {\"classificação\"}," \
                    "\"sentimentos_cliente\": {\"sentimento\": intensidade}," \
                    "\"contribuicoes_cliente\": {\"palavra/frase\": \"sentimento associado\"}," \
                    "\"razoes_possiveis_cliente\": [\"string\"]," \
                    "\"explicacao_modelo_cliente\": \"string\"," \
                    "\"role_atendente\": \"atendente\"," \
                    "\"classe_atendente\": {\"classificação\"}," \
                    "\"sentimentos_atendente\": {\"sentimento\": intensidade}," \
                    "\"contribuicoes_atendente\": {\"palavra/frase\": \"sentimento associado\"}," \
                    "\"razoes_possiveis_atendente\": [\"string\"]," \
                    "\"explicacao_modelo_atendente\": \"string\"" \
                "}"
    ''',

    "resumo": """
                Você é um analista sênior da empresa Leste telecom, sua função é analisar transcrições e interações com base nos critérios fornecidos abaixo:

                {text} Faça um breve resumo da conversa identificando os seguintes pontos:

                Quantos atendentes atenderam o cliente, nome do cliente que entrou em contato, motivo do contato, o que foi realizado pelo atendente, e analise se o atendimento foi finalizado por falta de interação ou o cliente aguarda alguma solução
                
                Caso o problema do cliente não tenha sido resolvido no atendimento ou faltou alguma informação: ofereça um retorno de contato. 
                se na interação foi agendada uma visita técnica ofereça um retorno de contato após a data da visita, para verificar se o problema foi rosolvido. 
                

                Sempre Responda em Português do Brasil "pt-br"
            """,

    "aprovar": """
                    Com base na transcrição, responda as perguntas abaixo e inclua na resposta a pergunta original, a resposta e a justificativa com trechos específicos do texto: 

                    {text} 

                    Responda as perguntas:

                    1- FORMA DE COBRANÇA FOI EXPLICADA FORMA CORRETA?
                    2- CLIENTE COMPREENDEU A FORMA DE COBRANÇA?
                    3- O CLIENTE CONCORDA COM A DATA DA ATIVAÇÃO?
                    4- FOI INFORMADO SOBRE A NECESSIDADE DE TER UMA PESSOA CADASTRADA PARA RECEBER A EQUIPE?
                    4- O CLIENTE ESTÁ CIENTE DE QUE É NECESSÁRIO TER UMA PESSOA CADASTRADA E MAIOR DE IDADE PARA RECEBER A EQUIPE NO DIA DA INSTALAÇÃO? 
                    5- FOI OFERTADO SEGUNDO RESPONSÁVEL?
                    6- FOI SOLICITADO AO CLIENTE QUE ENCAMINHACE SUA COORDENADA PELO WHATSAPP?
                    7- FOI INFORMADO SOBRE A NECESSIDADE DE APRESENTAR O DOCUMENTO DE IDENTIFICAÇÃO COM FOTO NO DIA DA INSTALAÇÃO?
                    8- FOI INFORMADO SOBRE A NECESSIDADE DE DEVOLVER OS EQUIPAMENTOS?
                    9- FOI INFORMADO DOS MEIOS DE RETIRADA E ENVIO DO BOLETO?
                    10- FOI INFORMADO FORMAS DE CONTATO COM A EMPRESA ?
                    11- É INFORMADO OS BENEFÍCIOS DO PLANO? (SVAS)                    
                    13- FOI PERGUNTADO AO CLIENTE SE ELE POSSUI OUTRO PROVEDOR DE INTERNET E DESEJA FAZER UMA MIGRAÇÃO ?
                    14- FOI PERGUNTADO COMO CONHECEU A EMPRESA ?
                    15- FOI OFERTADO O LESTE MÓVEL?
                    16- CLIENTE FOI INFORMADO SOBRE O OPTIN?
                    17- CLIENTE POSSUI ALGUMA RESTRIÇÃO DE HORÁRIO?
                    18- FOI INFORMADO SOBRE OS BENEFÍCIOS COMO SKEELO, LESTE CLUBE (SVAs)?
                    19- CLIENTE FOI INFORMADO DA DURAÇÃO DA INSTALAÇÃO DE 1 A 2 HORAS?
                    20- CLIENTE SOLICITOU PAGAMENTO EM DÉBITO AUTOMÁTICO?
                    21- o CLIENTE TEVE ALGUMA DÚVIDA OU PERGUNTA QUE NÃO FOI RESPONDIDA OU ABORDADA NA INTERAÇÃO?

                    Responda SEMPRE em português do Brasil "pt-br".
    """,
    
    "motivo": "{text} identifique no texto o motivo do contato do cliente e se o problema apresentado foi resolvido na interação. Sempre Responda em Português do Brasil 'pt-br' ",
    
    "motivo3": "Identify and list the main keywords in the following text: {text}"
}
