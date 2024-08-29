prompts = {
    "sentimento": "{text} Analise o sentimento do texto a seguir, considerando todas as nuances possíveis",
    "resumo": """
                Você é um analista senior da empresa Leste telecom sua função é analisar transcrições e interações com base nos critérios da empresa

                {text} faça um breve resumo da interação identificando os pontos abaixo:

                Nome do funcionário que atendeu, nome do cliente que entrou em contato, motivo do contato, o que foi realizado pelo atendente, e analise se o atendimento foi finalizado por falta de interação ou o cliente aguarda alguma solução
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
    "motivo": "{text} identifique no texto o motivo do contato e se o problema apresesntado foi resolvido na interação",
    "motivo3": "Identify and list the main keywords in the following text: {text}"
}
