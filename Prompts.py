prompts = {
    "aprovar": '''
                com base na transcrição: responda as perguntas: 

                {text}

                1- FORMA DE COBRANÇA FOI EXPLICADA FORMA CORRETA?
                2- CLIENTE COMPREENDEU A FORMA DE COBRANÇA?
                3- O CLIENTE CONCORDA COM A DATA DA ATIVAÇÃO?
                4- FOI INFORMADO SOBRE A NECESSIDADE DE TER UMA PESSOA CADASTRADA PARA RECEBER A EQUIPE?
                5- FOI OFERTADO SEGUNDO RESPONSÁVEL?
                6- FOI COLETADO COORDENADA DO CLIENTE ?
                7- FOI INFORMADO SOBRE A NECESSIDADE DE APRESENTAR O DOCUMENTO COM FOTO FÍSICO NO DIA DA VISITA?
                8- FOI INFORMADO SOBRE A NECESSIDADE DE DEVOLVER OS EQUIPAMENTOS?
                9- FOI INFORMADO DOS MEIOS DE RETIRADA E ENVIO DO BOLETO?
                10- FOI INFORMADO FORMAS DE CONTATO COM A EMPRESA ?
                11- É INFORMADO OS BENEFÍCIOS DO PLANO? (SVAS)
                12- FOI SOLICITADO AO CLIENTE A COORDENADA PELO WHATSAPP ?
                13- FOI PERGUNTADO AO CLIENTE SE ESTÁ MIGRANDO DE UM OUTRO PROVEDOR, INDEPENDENTE DO VALOR DE ATIVAÇÃO?
                14- FOI PERGUNTADO COMO CONHECEU A EMPRESA ?
                15- FOI OFERTADO O LESTE MÓVEL?
                16- CLIENTE FOI INFORMADO SOBRE O OPTIN?
                17- CLIENTE POSSUI ALGUMA RESTRIÇÃO DE HORÁRIO?
                18- FOI INFORMADO SOBRE OS BENEFÍCIOS COMO SKEELO, LESTE CLUBE (SVAs)?
                19- CLIENTE FOI INFORMADO DA DURAÇÃO DA INSTALAÇÃO DE 1 A 2 HORAS?
                20- CLIENTE SOLICITOU PAGAMENTO EM DÉBITO AUTOMÁTICO?
                21- ALGUMA PERGUNTA O CLIENTE REALIZOU QUE NÃO FOI RESPONDIDA?
    ''',

    "resumo": "Por favor, faça um resumo detalhado do contato: ",


    "motivo": "Por favor, informe o motivo do contato e a satisfação do cliente: ",

    "aprovar2": '''
                Com base na transcrição, responda às perguntas abaixo e inclua na resposta a pergunta original, a resposta e a justificativa com trechos específicos do texto: 

                {text}

                1- FORMA DE COBRANÇA FOI EXPLICADA FORMA CORRETA?
                2- CLIENTE COMPREENDEU A FORMA DE COBRANÇA?
                3- O CLIENTE CONCORDA COM A DATA DA ATIVAÇÃO?
                4- FOI INFORMADO SOBRE A NECESSIDADE DE TER UMA PESSOA CADASTRADA PARA RECEBER A EQUIPE?
                5- FOI OFERTADO SEGUNDO RESPONSÁVEL?
                6- FOI COLETADO COORDENADA DO CLIENTE ?
                7- FOI INFORMADO SOBRE A NECESSIDADE DE APRESENTAR O DOCUMENTO COM FOTO FÍSICO NO DIA DA VISITA?
                8- FOI INFORMADO SOBRE A NECESSIDADE DE DEVOLVER OS EQUIPAMENTOS?
                9- FOI INFORMADO DOS MEIOS DE RETIRADA E ENVIO DO BOLETO?
                10- FOI INFORMADO FORMAS DE CONTATO COM A EMPRESA ?
                11- É INFORMADO OS BENEFÍCIOS DO PLANO? (SVAS)
                12- FOI SOLICITADO AO CLIENTE A COORDENADA PELO WHATSAPP ?
                13- FOI PERGUNTADO AO CLIENTE SE ESTÁ MIGRANDO DE UM OUTRO PROVEDOR, INDEPENDENTE DO VALOR DE ATIVAÇÃO?
                14- FOI PERGUNTADO COMO CONHECEU A EMPRESA ?
                15- FOI OFERTADO O LESTE MÓVEL?
                16- CLIENTE FOI INFORMADO SOBRE O OPTIN?
                17- CLIENTE POSSUI ALGUMA RESTRIÇÃO DE HORÁRIO?
                18- FOI INFORMADO SOBRE OS BENEFÍCIOS COMO SKEELO, LESTE CLUBE (SVAs)?
                19- CLIENTE FOI INFORMADO DA DURAÇÃO DA INSTALAÇÃO DE 1 A 2 HORAS?
                20- CLIENTE SOLICITOU PAGAMENTO EM DÉBITO AUTOMÁTICO?
                21- ALGUMA PERGUNTA O CLIENTE REALIZOU QUE NÃO FOI RESPONDIDA?
    ''',

    "sentimento":'''
                "realize uma análise detalhada " \
                "dos sentimentos do cliente e do atendente expresso no texto delimitado por {}, "\
                "classifique o sentimento de cada um como: 'positivo', 'negativo' ou 'neutro'. "\
                "Identifique e liste os sentimentos dp cliente e atendente mais presentes na interação, "\
                "em sua forma mais simples e direta (palavra primitiva)" \
                "tanto explícitos quanto implícitos, e avalie a intensidade de cada sentimento somados dentro de uma escala total de 0 (zero) a 100 (cem) em porcentagem(%). "\
                "Indique quais palavras-chave na sentença contribuíram " \
                "para os sentimentos identificados. "\
                "Além disso, sugira possíveis razões para esses sentimentos "\
                "com base na conversa. Por fim, explique como você chegou " \
                "a essas conclusões. Retorne todas essas informações em português do Brasil " \
                "no seguinte formato de um objeto JSON entre 3 cráses ´´´ respeitando a estrutura abaixo para cliente e atendente: " \
                <json>
                "{" \
                    "\"role_cliente\": \"cliente\"," \
                    "\"classe_cliente\": \"classificação\"," \
                    "\"sent_cliente\": {\"sentimento\": intensidade}," \
                    "\"razoes_possiveis_cliente\": [\"string\"]," \
                    "\"explicacao_modelo_cliente\": \"string\"," \
                    "\"role_atendente\": \"atendente\"," \
                    "\"classe_atendente\": \"classificação\"," \
                    "\"sent_atendente\": {\"sentimento\": intensidade}," \
                    "\"razoes_possiveis_atendente\": [\"string\"]," \
                    "\"explicacao_modelo_atendente\": \"string\"" \
                "}"
                <json>
                retorne apenas a estrutura do json com a análise
    '''
    
    # Adicione outras ações e prompts conforme necessário
}
