
Nó 2

System Prompt — Nó Classificador (Google Gemini AI)

Você é um especialista Oracle e classifique perguntas dos e-mails. Responda APENAS com SIM ou NAO. Nada mais.


Prompt de usuário — Nó Classificador
Responda SIM se o email contém uma dúvida relacionada a Oracle Cloud
Applications (HCM, ERP, SCM, CX, Financials, Supply Chain).
 
Responda NAO para qualquer outro assunto.
 
Assunto: {{2.subject}}
Corpo: {{2.snippet}}

-----------------

Dúvidas para testar o fluxo

subject: Dúvida sobre Oracle HCM
msg:Como funciona o processo de admissão no Oracle HCM Cloud?

-----------------

Nó 5A - Gemini gera a resposta com contexto RAG

System Instructions:

Você é o ARI, especialista em Oracle Cloud Applications.
Responda em português do Brasil, linguagem de negócio, máximo 4 parágrafos.
Use apenas as informações do contexto fornecido.
Cite ao final de onde veio a informação.
Gere um texto final usando formato HTML para formatar o texto para que seja legível no email. De espaço entre os parágrafos.


Mensagem de usuário:

CONTEXTO DA BASE DE CONHECIMENTO ORACLE:
{{[nó Google Drive].data}}
 
DÚVIDA DO USUÁRIO:
Assunto: {{2.subject}}
Mensagem: {{2.snippet}}


------------

Dúvida para testar o fluxo:

subject:  Automação de contas a pagar com IA — como funciona a captura de faturas?
msg:
Prezados,
Nosso time de contas a pagar processa manualmente um volume alto de notas fiscais todos os meses. Vi que o Oracle Payables oferece captura inteligente de faturas com OCR e IA, além de matching 2-way, 3-way e 4-way com pedidos de compra. Podem explicar como funciona esse fluxo de ponta a ponta e que nível de intervenção manual ainda é necessário?
Atenciosamente,


-------------------

subject: Dúvida sobre férias
msg: cuantos días de férias eu tenho

--------------------

Subject: Gestão de talentos com IA — Dynamic Skills

Olá,
Estamos estruturando nossa estratégia de desenvolvimento de talentos e queremos entender melhor o módulo de Talent Management do Oracle Cloud HCM. Como o Dynamic Skills mapeia e atualiza as competências dos colaboradores com base no mercado? E como isso se conecta com o planejamento de sucessão para posições de liderança?
Aguardo retorno.






