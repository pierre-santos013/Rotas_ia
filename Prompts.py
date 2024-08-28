prompts = {
    "motivo1": "Analyze the sentiment of the following text, considering all possible nuances: {text}",
    "resumo": "realize um resumo da interação retornando o motivo do contato, se o problema foi resolvido e se o atendimento foi finalizado por falta de interação : {text}",
    "aprovar": """
                    Analise a seguinte transcrição de interação entre cliente e empresa: 

                    {text} 

                    Responda as perguntas:

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
                    12- FOI SOLICITADO AO CLIENTE A LOCALIZAÇÃO POR COORDENADAS ?
                    13- FOI PERGUNTADO AO CLIENTE SE ESTÁ MIGRANDO DE UM OUTRO PROVEDOR, INDEPENDENTE DO VALOR DE ATIVAÇÃO?
                    14- FOI PERGUNTADO COMO CONHECEU A EMPRESA ?
                    15- FOI OFERTADO O LESTE MÓVEL?
                    16- CLIENTE FOI INFORMADO SOBRE O OPTIN?
                    17- CLIENTE POSSUI ALGUMA RESTRIÇÃO DE HORÁRIO?
                    18- FOI INFORMADO SOBRE OS BENEFÍCIOS COMO SKEELO, LESTE CLUBE (SVAs)?
                    19- CLIENTE FOI INFORMADO DA DURAÇÃO DA INSTALAÇÃO DE 1 A 2 HORAS?
                    20- CLIENTE SOLICITOU PAGAMENTO EM DÉBITO AUTOMÁTICO?
                    21- ALGUMA PERGUNTA O CLIENTE REALIZOU QUE NÃO FOI RESPONDIDA?

                    Responda em português do Brasil.
    """,
    "motivo2": "Based on the following text, answer the question as thoroughly as possible: {text}",
    "motivo3": "Identify and list the main keywords in the following text: {text}"
}
