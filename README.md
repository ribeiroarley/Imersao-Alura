# ARI CONSULTING — Suíte Corporativa de Automação Inteligente (Oracle Cloud)

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Google GenAI SDK](https://img.shields.io/badge/Google%20GenAI-Gemini%203.8%20Flash-4285F4.svg)](https://ai.google.dev/)
[![Pydantic v2](https://img.shields.io/badge/Pydantic-v2.0+-e92063.svg)](https://docs.pydantic.dev/)
[![python-docx](https://img.shields.io/badge/python--docx-v1.2+-2b579a.svg)](https://python-docx.readthedocs.io/)
[![Jinja2](https://img.shields.io/badge/Jinja2-v3.1+-b41717.svg)](https://jinja.palletsprojects.com/)

Plataforma integrada de inteligência artificial aplicada ao ciclo completo de negócios B2B da **ARI CONSULTING** (consultoria especializada no ecossistema **Oracle Cloud Applications**, sediada em São Paulo — Capital).

A suíte unifica **inteligência de mercado**, **automação de propostas comerciais** e **suporte técnico pós-implementação com arquitetura RAG**, combinando modelos de linguagem de última geração a motores determinísticos de validação de regras de negócio.

---

## 1. Visão Geral da Solução

O ecossistema é composto por três módulos independentes e complementares que cobrem as principais esteiras corporativas da consultoria:

1. **Módulo 1 — ARI NEWS (Inteligência & Prospecção de Mercado):**
   Agente autônomo de curadoria em tempo real utilizando **Google Search Grounding** para monitorar o ecossistema corporativo brasileiro (ERP, automação, nuvem e conformidade fiscal), gerando briefings executivos em HTML com ganchos comerciais estratégicos para abordagem de clientes com soluções Oracle Cloud.

2. **Módulo 2 — ARI DEAL (Inteligência Comercial & Validação de Negócios):**
   Copiloto de vendas com motor determinístico em **Pydantic v2** que audita briefings de clientes corporativos, valida teto orçamentário (*budget ceiling*), aplica regras restritas de desconto e gera propostas comerciais oficiais em **Microsoft Word (.docx)** respeitando o Brand Book corporativo e a metodologia **OCIM em 6 fases**.

3. **Módulo 3 — ARI SUPPORT (Atendimento Técnico Especializado com RAG):**
   Pipeline de atendimento corporativo com **Nó de Triagem de Escopo** e **Nó RAG Técnico** que consulta dinamicamente manuais técnico-funcionais da suíte Oracle Fusion Cloud (Release 26C), gerando pareceres técnicos estruturados em e-mails HTML minimalistas com passos de parametrização e citação oficial da fonte.

---

## 2. Arquitetura da Solução

O fluxo de dados integra a prospecção de mercado, o fechamento de contratos e o suporte contínuo aos clientes:

```text
===================================================================================================
                               ARQUITETURA DA SUÍTE ARI CONSULTING
===================================================================================================

 [ 01 - ARI NEWS ]                    [ 02 - ARI DEAL ]                    [ 03 - ARI SUPPORT ]
 Inteligência de Mercado             Inteligência Comercial                Suporte Técnico RAG
 
  +------------------+                +------------------+                 +------------------+
  |  Web em Tempo    |                | Briefing Cliente |                 | Chamado / Ticket |
  |  Real (Grounding)|                | (Ex: Vetria S.A.)|                 | do Cliente       |
  +--------+---------+                +--------+---------+                 +--------+---------+
           |                                   |                                    |
           v                                   v                                    v
  +------------------+                +------------------+                 +------------------+
  | Gemini 3.8 Flash |                | Validador        |                 | Nó de Triagem    |
  | + Google Search  |                | Determinístico   |                 | (Scope Gate)     |
  +--------+---------+                | (Pydantic v2)    |                 +--------+---------+
           |                          +--------+---------+                          |
           |                                   | (Regras 100% OK)                   v (Em Escopo)
           v                                   v                           +------------------+
  +------------------+                +------------------+                 | Nó RAG Técnico   |
  | Ganchos Comerciais|                | Injeção no Modelo|                 | (Base de Manuais |
  | Oracle Cloud     |                | Master .docx     |                 | Release 26C)     |
  +--------+---------+                +--------+---------+                 +--------+---------+
           |                                   |                                    |
           v                                   v                                    v
  +------------------+                +------------------+                 +------------------+
  | Briefing HTML    |                | Proposta Word    |                 | Parecer Técnico  |
  | Executivo 90°    |                | Oficial (.docx)  |                 | E-mail HTML 90°  |
  +------------------+                +------------------+                 +------------------+
===================================================================================================
```

Para o diagnóstico técnico detalhado, matriz de conformidade e roadmap de engenharia de cada projeto, consulte:
* [Relatório de Auditoria e Diagnóstico Arquitetural](docs/RELATORIO_AUDITORIA_PROJETOS.md)

---

## 3. Estrutura de Diretórios

```text
Imersao-Alura/
├── .env.example                               # Exemplo de configuração de variáveis de ambiente
├── .gitignore                                 # Regras de exclusão do Git (.venv, chaves, temporários)
├── requirements.txt                           # Dependências consolidadas do ecossistema
├── README.md                                  # Documentação executiva e arquitetural
├── docs/                                      # Governança e documentação técnica
│   └── RELATORIO_AUDITORIA_PROJETOS.md        # Relatório de Auditoria e Diagnóstico Arquitetural
│
├── 01-ari-news-dashboard/                     # MÓDULO 1: Radar de Notícias & Inteligência
│   ├── prompts/
│   │   └── ari-news-prompts.md                # Prompts do pipeline Google Opal / Gemini
│   ├── src/
│   │   └── news_agent.py                      # Agente de curadoria com Grounding e Jinja2
│   └── output/
│       └── briefing_noticias.html             # Briefing executivo gerado
│
├── 02-ari-deal-propostas/                     # MÓDULO 2: Copiloto de Propostas Comerciais
│   ├── base-conhecimento/
│   │   ├── brand-book.json                    # Design System corporativo oficial
│   │   ├── catalogo-servicos-2026.pdf         # Tabela canônica de 8 serviços e faixas
│   │   ├── template-proposta-comercial.docx   # Modelo mestre oficial Word (5 seções)
│   │   └── benchmark-proposta-*.pdf           # Propostas de referência de grande porte
│   ├── docs-ref/
│   │   ├── briefing-vetria-embalagens.txt     # Caso de teste canônico Vetria S.A.
│   │   └── instrucoes-ari-deal.txt            # Especificação de regras de negócio
│   ├── src/
│   │   ├── deal_validator.py                  # Motor determinístico de regras (Pydantic v2)
│   │   └── docx_generator.py                  # Gerador de documentos Word com precisão visual
│   └── output/
│       └── Proposta_Comercial_Vetria_Embalagens.docx  # Proposta final nº 082/2026
│
└── 03-ari-support-rag/                        # MÓDULO 3: Atendimento e Suporte RAG
    ├── base-conhecimento/
    │   ├── oracle-fusion-cloud-financials.md  # Manual técnico Core (GL, AP, Cash)
    │   ├── oracle-fusion-cloud-hcm.md         # Manual técnico de RH e Talentos
    │   ├── oracle-fusion-cloud-sales.md       # Manual técnico de CX e Vendas
    │   └── oracle-fusion-cloud-supply-chain.md# Manual técnico de Suprimentos e Logística
    ├── prompts/
    │   └── prompts-triagem-e-resposta.md      # Prompts de triagem e injeção de contexto RAG
    ├── src/
    │   └── support_agent.py                   # Agente de suporte (Triagem + RAG + Resiliência)
    └── output/
        └── resposta_ticket_suporte.html       # E-mail corporativo de resposta técnica
```

---

## 4. Instruções de Instalação e Execução

### 4.1. Pré-Requisitos e Ativação do Ambiente

Certifique-se de possuir o **Python 3.13** instalado. Na raiz do projeto, ative o ambiente virtual e instale as dependências:

```powershell
# No Windows PowerShell:
.\.venv\Scripts\Activate.ps1

# Atualize/instale as dependências:
pip install -r requirements.txt
```

### 4.2. Configuração de Credenciais

Crie o arquivo `.env` na raiz do projeto (ou copie a partir de `.env.example`) e configure sua chave de API:

```env
GEMINI_API_KEY=sua_chave_gemini_aqui
```

---

### 4.3. Execução dos Agentes

#### A. Executar Módulo 1 (ARI NEWS):
Coleta 3 notícias corporativas em tempo real via Google Search, formula ganchos comerciais de Oracle Cloud e gera o briefing HTML minimalista:

```powershell
python 01-ari-news-dashboard\src\news_agent.py
```
> **Saída:** Arquivo gerado em `01-ari-news-dashboard/output/briefing_noticias.html`.

#### B. Executar Módulo 2 (ARI DEAL):
Valida o briefing de negócio com Pydantic e gera o documento oficial da proposta comercial em Word (.docx):

```powershell
# Validação determinística das regras de negócio:
python 02-ari-deal-propostas\src\deal_validator.py

# Geração da proposta final formatada em Word:
python 02-ari-deal-propostas\src\docx_generator.py
```
> **Saída:** Arquivo gerado em `02-ari-deal-propostas/output/Proposta_Comercial_Vetria_Embalagens.docx`.

#### C. Executar Módulo 3 (ARI SUPPORT):
Realiza a triagem semântica do chamado da Vetria Embalagens, recupera o manual de Financials e compila o parecer técnico de atendimento em HTML:

```powershell
python 03-ari-support-rag\src\support_agent.py
```
> **Saída:** Arquivo gerado em `03-ari-support-rag/output/resposta_ticket_suporte.html`.

---

## 5. Tecnologias Utilizadas

| Tecnologia | Versão | Aplicação na Arquitetura |
|---|---|---|
| **Python** | `3.13+` | Runtime principal dos agentes e orquestração do ecossistema. |
| **Google GenAI SDK** | `0.1.1+` | Conexão de baixa latência com o modelo `gemini-3.8-flash` e ferramentas de busca (`GoogleSearch`). |
| **Pydantic** | `2.0.0+` | Validação determinística de esquemas, faixas de investimento, integridade de e-mails corporativos e políticas comerciais. |
| **python-docx** | `1.2.0+` | Leitura, manipulação de tabelas, injeção de texto e serialização de documentos Word com aderência ao Brand Book. |
| **Jinja2** | `3.1.0+` | Motor de templates para compilação dinâmica de layouts HTML responsivos sem frameworks externos. |
| **python-dotenv** | `1.0.0+` | Isolamento e injeção segura de segredos e credenciais via variáveis de ambiente. |

---

## 6. Governança, Segurança e Resiliência Corporativa

1. **Isolamento de Credenciais (.env):**
   Chaves de acesso jamais são expostas em código. O `.gitignore` protege chaves privadas, arquivos temporários de compilação (`__pycache__`) e o ambiente virtual `.venv`.

2. **Conformidade Determinística (Zero-Alucinação):**
   Cálculos financeiros e validações de regras críticas não dependem de saídas livres de LLMs:
   - **Catálogo Fechado 2026:** Validação estrita de cada serviço contra os 8 serviços canônicos da consultoria.
   - **Teto Orçamentário (*Budget Ceiling*):** Bloqueio imediato caso o total líquido ultrapasse o orçamento aprovado pelo conselho do cliente (ex: R$ 350.000,00 no caso Vetria).
   - **Política de Desconto Inviolável:** Desconto de 10% a 15% é liberado estritamente para pacotes combinados com 2 ou mais serviços.
   - **Condições Fixas de Pagamento:** Divisão rígida de 30% na assinatura, 40% na conclusão do Build e 30% no Go-Live calculados com precisão monetária (`Decimal`).
   - **Governança de Alçada:** Alerta mandatório de auditoria e estudo de caso de marketing para propostas com valor superior a R$ 200.000,00.

3. **Camadas de Resiliência Corporativa (High Availability):**
   Todos os agentes de IA possuem interceptação de exceções de API (`errors.APIError`, `429 RESOURCE_EXHAUSTED`, `503 UNAVAILABLE` e oscilações de rede). Em cenários de exaustão de cota momentânea:
   - O **ARI NEWS** ativa o feed de inteligência resiliente com links codificados do Google Search, garantindo geração sem falha de briefing.
   - O **ARI SUPPORT** ativa a triagem heurística e gera o parecer técnico fundamentado diretamente nos manuais locais da suíte Release 26C, garantindo disponibilidade ininterrupta do serviço.

4. **Design System Institucional (ARI Visual Standards):**
   Todos os artefatos visuais (HTML e DOCX) seguem a estética de "Liderança de Pensamento":
   - Cantos estritamente retos de 90° (`border-radius: 0px`).
   - Paleta monocromática elegante (`#0D0D0D`, `#555555`, `#F9F9F9`, `#FFFFFF`).
   - Tipografia geométrica sem serifa (Arial para documentos impressos/Word, Inter/system-ui para web).
   - Proibição de bibliotecas CDN externas, garantindo total compatibilidade com ambientes corporativos com restrições rígidas de CSP (*Content Security Policy*).

---

## 👥 Créditos e Autoria

Este projeto foi concebido e implementado dentro de uma dinâmica de colaboração em arquitetura e engenharia de soluções em IA:

* **Idealizadores & Programa Formador:**
  * **Oracle Next Education (ONE)**
  * **Imersão ONE — Business AI Builder** (Alura & Oracle)

* **Aluno & Copiloto Técnico:**
  * **Arley Ribeiro da Silva Xavier**
  * *Perfil:* Administrador de Banco de Dados (DBA) | Oracle Database e Automação com Python
  * *Especialidade:* Especialista no ecossistema Oracle Database em ambientes locais e em nuvem, com foco em automação, governança de dados e integração com inteligência artificial.
  * *GitHub:* [github.com/ribeiroarley](https://github.com/ribeiroarley)

* **Ferramentas & Tecnologias de Suporte:**
  * **Gemini (Google DeepMind)** — Arquitetura de soluções, modelagem de prompts e esteira RAG.
  * **Antigravity CLI (agy)** — Execução determinística de comandos, manipulação de arquivos e compilação do workspace.

---

*ARI CONSULTING © 2026 — Centro de Excelência em Soluções Oracle Cloud Applications. São Paulo — SP, Capital.*
