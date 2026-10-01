# Relatório de Auditoria Técnica e Diagnóstico de Engenharia

**Workspace:** `Imersao-Alura`  
**Data da Auditoria:** 01 de Outubro de 2026  
**Responsável Técnico:** Arquiteto de Soluções & Engenheiro de Software Sênior  
**Status da Auditoria:** Concluída — Plano de Reestruturação e Segurança Executado com Sucesso  

---

## 1. Sumário Executivo

O presente documento consolida a auditoria técnica detalhada, arquitetural e de segurança realizada nos três projetos desenvolvidos na **Imersão Alura**.

Após a varredura completa de todos os diretórios, arquivos de texto, prompts, bases de conhecimento e documentos de referência, constatou-se que o workspace compõe uma jornada progressiva e coerente voltada ao ecossistema corporativo fictício da **ARI CONSULTING** (consultoria especializada em soluções Oracle Cloud, sediada em São Paulo):

1. **Aula 1 (Inteligência de Mercado):** Painel de notícias automatizado (*ARI NEWS*) com busca em tempo real, geração de arte visual abstrata e geração de página HTML em conformidade com Design System corporativo em ambiente restrito (Google Opal).
2. **Aula 2 (Inteligência Comercial):** Copiloto conversacional (*ARI DEAL*) para validação de briefings empresariais e geração automatizada de propostas comerciais no formato Word (.docx), suportado por regras de negócio rígidas, catálogo de serviços e Brand Book.
3. **Aula 3 (Inteligência de Atendimento & Suporte):** Pipeline de atendimento e suporte automatizado de e-mails (*ARI SUPPORT / Copiloto de Atendimento*) utilizando classificação binária por IA, arquitetura RAG (*Retrieval-Augmented Generation*) sobre manuais técnicos do Oracle Fusion Cloud (Financials, HCM, Sales, Supply Chain) e orquestração de workflow (Make/n8n + Gemini).

Abaixo apresentam-se o diagnóstico aprofundado, os gaps arquiteturais identificados, o plano de modernização e a proposta de reestruturação física e semântica do repositório.

---

## 2. Auditoria Técnica Detalhada por Módulo / Aula

### 2.1. Aula 1 — ARI NEWS: Painel de Inteligência de Negócios

#### A. Tema e Objetivo Principal
Desenvolvimento de uma aplicação/agente multimodal (*ARI NEWS*) encadeado em nós para curadoria, sumarização e exibição visual de notícias setoriais e regionais recentes em um painel web minimalista de alta sofisticação.

#### B. Regras de Negócio e Diretrizes de Design
- **Ancoragem Temporal e Veracidade:** Busca restrita estritamente a notícias publicadas a partir da data parametrizada pelo usuário; proibição absoluta de alucinação de URLs (extração de links reais ou geração de busca padronizada via slug do Google).
- **Quantitativo Estrito:** Seleção de exatamente 3 notícias relevantes em português do Brasil (pt-BR).
- **Design System Institucional (ARI System):**
  - Estética minimalista ("Liderança de Pensamento"), cantos vivos de 90° (`border-radius: 0`), proibição de cantos arredondados, gradientes ou modos escuros.
  - Paleta restrita: Fundo `#FFFFFF`, Superfície Secundária `#F9F9F9`, Texto Primário `#0D0D0D`, Texto Secundário/Muted `#555555`.
  - Alternância de blocos: 1º e 3º blocos em fundo branco, 2º bloco em `#F9F9F9`.
  - Identificadores sequenciais: `01 / 03`, `02 / 03`, `03 / 03`.
- **Restrições de Segurança (CSP - Content Security Policy):**
  - O código HTML/CSS deve ser único e autônomo para renderização segura em `iframe` dentro da plataforma Google Opal.
  - Proibição de bibliotecas externas via CDN (Tailwind, Bootstrap, Google Fonts externas ou scripts de terceiros).
  - Geração de imagem artística para seção Hero via modelo generativo (sem texto na imagem).

#### C. Persona e Caso de Uso
- **Persona:** Executivos, consultores de negócios e decisores corporativos que necessitam de um resumo matinal ou setorial sem ruído publicitário.
- **Caso de Uso:** O usuário informa o setor (ex.: *Inteligência Artificial*), a região (ex.: *Brasil*) e a data de corte (ex.: *últimos 7 dias*). O sistema pesquisa os fatos mais relevantes, gera um banner conceitual e exibe um painel pronto para consumo imediato.

#### D. Tecnologias e Modelos de IA Explorados
- **Plataforma de Execução:** Google Opal (ambiente de orquestração visual de agentes e nós).
- **Modelos de IA:**
  - `text_generation_agent` com ancoragem em busca web (Google Search Grounding).
  - Modelo de Geração de Imagens (Google Imagen) com prompt estruturado para estética abstrata/minimalista (proibição de tipografia na imagem).
  - LLM de formatação estruturada e geração de código (HTML/CSS inline).

#### E. Resumo dos Componentes
- `Arquivos aula 1/Arquivos - Aula 1/Aulal 1 - Prompts.txt`: Contém o fluxo completo:
  - *Prompt 0:* Especificação do app de prompt único.
  - *Prompt 1 (Nó 4):* Buscador de notícias com ancoragem temporal.
  - *Prompt 2 (Nó 6):* Formatador de dados e gerador de slugs seguros para busca Google.
  - *Prompt 3 (Nó 7):* Gerador de Hero Image conceitual.
  - *Prompt 4 & 4.1 (Nó 5):* Criador da página web HTML/CSS e System Instructions compatíveis com CSP.

#### F. Diagnóstico Atual: O que está Pronto vs. O que é Esqueleto
| Componente | Situação Atual | Diagnóstico de Engenharia |
|---|---|---|
| **Engenharia de Prompt** | Pronto e maduro | Instruções detalhadas, restrições negativas claras e formatação precisa. |
| **Código da Aplicação** | Esqueleto / Inexistente localmente | Não há código backend/frontend versionado no repositório; os prompts dependem exclusivamente da execução manual dentro do Google Opal. |
| **Pipeline de Testes** | Ausente | Não existem scripts automatizados para validar a validade das URLs geradas ou integridade do HTML retornado. |

#### G. Potencial de Customização e Modernização (Roadmap)
1. **Desacoplamento de Plataforma (Engine Própria):** Criar uma API em **FastAPI (Python)** ou **Node.js** consumindo diretamente a API do **Gemini 2.5/Flash** com `google-genai` SDK e Google Search Tool.
2. **Frontend Moderno:** Substituir a renderização inline de iframe por uma interface reativa em **Next.js (React)** ou **Streamlit**, consumindo o Design System como tokens CSS reutilizáveis.
3. **Persistência e Cache:** Implementar cache com **Redis** ou banco de dados relacional (**PostgreSQL/SQLite**) para armazenar newsletters diárias por setor, evitando custos desnecessários de inferência e chamadas de busca repetidas.

---

### 2.2. Aula 2 — ARI DEAL: Copiloto de Propostas Comerciais

#### A. Tema e Objetivo Principal
Criação de um copiloto comercial inteligente (*ARI DEAL*) capaz de orientar consultores, processar briefings complexos de clientes corporativos, validar conformidade com tabelas de preço e catálogo de serviços, e gerar propostas comerciais completas e formatadas em Microsoft Word (.docx).

#### B. Regras de Negócio Invioláveis (Hard Constraints)
1. **Catálogo Fechado:** Aderência obrigatória aos 8 serviços vigentes do Catálogo 2026 da ARI CONSULTING. Bloqueio automático de qualquer solicitação fora do portfólio.
2. **Faixas de Investimento Estritas:** Valores obrigatoriamente dentro das faixas mínima e máxima tabeladas; qualquer desvio bloqueia o fluxo.
3. **Prazos Operacionais:** Consistência dos cronogramas com os prazos típicos de cada módulo.
4. **Política de Desconto:** Permitido desconto de 10% a 15% apenas para pacotes combinados de 2 ou mais serviços.
5. **Condições de Pagamento Imutáveis:** 30% na assinatura do contrato, 40% na conclusão da fase Build e 30% no Go-Live (com valores nominais calculados e explícitos).
6. **Validade da Proposta:** Fixa em 30 dias corridos a partir da data de emissão.
7. **Governança de Risco (Alçada > R$ 200k):** Propostas com valor superior a R$ 200.000,00 exigem a inclusão obrigatória de estudo de caso de referência fornecido pelo marketing.
8. **Revisão de Alçada:** Alerta mandatório de que a seção de investimentos requer aprovação formal do Gerente de Contas antes do envio ao cliente.
9. **Metodologia Padronizada:** Adoção estrita das 6 fases da metodologia OCIM (*Descoberta, Design, Build, Testes, Go-Live, Hiperescalada*).
10. **Segurança de Marca:** Proibição de menção a nomes de consultorias concorrentes.

#### C. Persona e Caso de Uso
- **Persona:** Consultor de Pré-Vendas e Gerente de Contas da ARI CONSULTING negociando implementações de grande porte.
- **Caso de Uso Auditado (Briefing Vetria Embalagens Industriais S.A.):** Empresa média-grande (1.450 colaboradores, R$ 680M faturamento) com legado fragmentado de 3 ERPs (Protheus, Sankhya, Delphi), dor crítica de fechamento contábil em 14 dias (meta: 5 dias), R$ 340k de pagamentos duplicados, orçamento teto de R$ 350.000,00 e necessidade de módulos Core (GL, AP, Cash Management e integração OIC).

#### D. Tecnologias e Modelos de IA Explorados
- **Arquitetura de Agente:** Copiloto de Conversação e Validação Estruturada com suporte a dois fluxos:
  - *Fluxo A (Validador de Briefing):* Ingestão de documento externo, extração de entidades, verificação contra 10 campos obrigatórios e 10 opcionais, geração de relatório de gaps e resumo executivo.
  - *Fluxo B (Formulário Guiado):* Diálogo passo a passo em 5 etapas sequenciais.
- **Engenharia de Contexto:** Injeção de múltiplos arquivos de base de conhecimento (`brand-book.json`, Catálogo em PDF, Propostas de benchmark anteriores e Template DOCX).
- **Modelo Alvo:** LLMs multimodais avançadas (Gemini / Claude / GPT-4o) em ambiente de chat ou skill de sistema.

#### E. Resumo dos Componentes
- `Docs-Ref/instrucoes-ari-deal.txt`: Especificação técnica completa do agente, mapeamento de campos, fluxos de validação e diretrizes de geração.
- `Docs-Ref/briefing-teste-vetria-embalagens.txt`: Cenário de teste enterprise realista para estressar as regras de negócio.
- `Docs-Ref/Prompt Aula 2.txt`: Prompt meta-instrução para transformar a especificação em uma "Skill reutilizável no Codex".
- `Base-Conhecimento/brand-book.json`: Especificação formal de design system para documentos corporativos (paleta, tipografia Arial, margens A4 de 2,5 cm, estrutura de tabelas sem bordas, pills de capa, etc.).
- `Base-Conhecimento/Catalogo-Servicos-2026-ARI-CONSULTING.pdf`: Tabela oficial de 8 serviços, faixas de preços, durações e pacotes de sustentação pós-go-live.
- `Base-Conhecimento/Proposta-Comercial-ARI-CONSULTING.docx`: Template mestre no formato Word com as 5 seções canônicas.
- `Base-Conhecimento/Proposta-047-2026-Banco-Central-Sul-ARI-CONSULTING.pdf`: Benchmark real de proposta para módulo HCM.
- `Base-Conhecimento/Proposta-061-2026-Logistica-Norte-ARI-CONSULTING.pdf`: Benchmark real de proposta para módulo SCM e Integração.

#### F. Diagnóstico Atual: O que está Pronto vs. O que é Esqueleto
| Componente | Situação Atual | Diagnóstico de Engenharia |
|---|---|---|
| **Base Documental e Regras** | Produção / Altíssimo nível | A documentação de regras de negócio, brand book e templates possui qualidade de nível corporativo e está completa. |
| **Automação de Geração de DOCX** | Esqueleto / Dependente de IA generativa no chat | A criação do `.docx` final depende de recursos nativos da interface da LLM (Code Interpreter / Advanced Data Analysis). Não há um script em Python versionado para gerar o arquivo determinístico a partir dos dados extraídos. |
| **Validação Determinística** | Parcialmente confiada à LLM | Cálculos de parcelamento e checagem de faixas de valores estão delegados ao prompt, o que pode gerar alucinações matemáticas ocasionais se não houver um motor de cálculo complementar. |

#### G. Potencial de Customização e Modernização (Roadmap)
1. **Motor Determinístico de Geração em Python:** Criar um microserviço utilizando `python-docx` e `pydantic` para receber os dados JSON validados e preencher o template `Proposta-Comercial-ARI-CONSULTING.docx` com fidelidade visual milimétrica, sem risco de corrupção de layout.
2. **Interface Web para Vendedores:** Construir um portal em **Streamlit** ou **Next.js** onde o consultor pode subir o arquivo de briefing, visualizar o checklist de validação em tempo real, ajustar os serviços e baixar o `.docx` e `.pdf` gerados com um clique.
3. **Persistência de Propostas:** Armazenar os históricos de versões e briefings em banco de dados relacional para auditoria de alçadas de desconto e integração com CRM (HubSpot / Salesforce / Oracle Sales Cloud).

---

### 2.3. Aula 3 — ARI SUPPORT: Triagem e Atendimento Automatizado com RAG

#### A. Tema e Objetivo Principal
Implementação de um fluxo de automação de e-mails para suporte corporativo (*ARI SUPPORT*), combinando classificação inteligente de mensagens recebidas, recuperação de contexto de documentos técnicos (RAG) e geração de respostas resolutivas e estruturadas em HTML.

#### B. Regras de Negócio e Diretrizes de Fluxo
- **Classificação Estrita (Portão de Entrada):** O modelo classificador deve responder estritamente com `SIM` ou `NAO`.
  - `SIM`: A mensagem refere-se a dúvidas sobre aplicações Oracle Cloud (HCM, ERP, SCM, CX, Financials, Supply Chain).
  - `NAO`: Mensagens não relacionadas ao escopo Oracle (ex.: pedidos de férias diretos de funcionários sem relação com a ferramenta, spam, dúvidas alheias).
- **Diretrizes de Geração de Resposta (RAG):**
  - Persona especializada (*ARI*, consultor sênior em Oracle Cloud).
  - Linguagem executiva de negócios em português do Brasil (pt-BR).
  - Tamanho controlado: Máximo de 4 parágrafos.
  - Fidelidade estrita: Utilizar exclusivamente as informações contidas no contexto recuperado.
  - Citação obrigatória de fontes documentais ao final.
  - Formatação obrigatória em HTML limpo com espaçamento entre parágrafos para renderização perfeita no cliente de e-mail do destinatário.

#### C. Persona e Caso de Uso
- **Persona:** Clientes corporativos, analistas de negócios e decisores que enviam dúvidas funcionais e técnicas por e-mail para a ARI CONSULTING.
- **Casos de Uso Testados:**
  - Pergunta sobre automação de Contas a Pagar com IA e matching de faturas (direcionada ao Oracle Financials).
  - Pergunta sobre mapeamento de competências com Dynamic Skills e sucessão (direcionada ao Oracle HCM).
  - Filtro negativo: Mensagem em espanhol solicitando cálculo pessoal de dias de férias (filtrada como `NAO`).

#### D. Tecnologias e Modelos de IA Explorados
- **Orquestrador de Workflows:** Make.com ou n8n (evidenciado pela sintaxe de variáveis `{{2.subject}}`, `{{2.snippet}}`, `{{[nó Google Drive].data}}`).
- **Modelo de Linguagem:** Google Gemini AI (nós dedicados de classificação e geração).
- **Mecanismo RAG:** Ingestão de contexto documental a partir de pasta integrada no Google Drive contendo manuais técnicos em Markdown.

#### E. Resumo dos Componentes
- `Aula 3 - Prompts.txt`: Prompts para os nós classificadores e geradores de e-mail, além de bateria de testes reais.
- `Base Conhecimento Apps Oracle.url`: Atalho para Google Docs com a base unificada.
- `Oracle Fusion Cloud Financials.md`: Manual técnico completo da suíte financeira (GL, AP, AR, Assets, Cash Management, arquitetura 4 C's, relatórios e novidades da Release 26C com GenAI).
- `Oracle Fusion Cloud HCM.md`: Manual técnico aprofundado de recursos humanos (Core HR, Benefits, Workforce Modeling, Recruiting, Learning, Dynamic Skills, Payroll e interface Redwood).
- `Oracle Fusion Cloud Sales.md`: Manual técnico de automação comercial e CRM (Unity CDP, Lead Scoring, Opportunity Management, Sales Playbooks e AI Next Best Action).
- `Oracle Fusion Cloud Supply Chain.md`: Manual técnico da cadeia de suprimentos (PLM, Procurement, Inventory, Manufacturing, OTM/WMS e manutenção preditiva com IoT na Release 26C).
- `Chave Key Gemini Projeto ONE.txt`: Arquivo com credencial de acesso em texto plano (**Risco Crítico de Segurança**).

#### F. Diagnóstico Atual: O que está Pronto vs. O que é Esqueleto
| Componente | Situação Atual | Diagnóstico de Engenharia |
|---|---|---|
| **Manuais Técnicos da Base** | Nível de Excelência | O conteúdo dos 4 arquivos `.md` é extremamente denso, atualizado (Release 26C) e estruturado com alta precisão técnica. |
| **Pipeline RAG** | Ingênuo (Naive RAG) / Incompleto | A injeção de contexto é feita injetando o conteúdo bruto do Google Drive na janela de contexto (`{{[nó Google Drive].data}}`). Não há fragmentação (*chunking*), geração de *embeddings*, nem busca vetorial semântica. |
| **Orquestração** | Dependente de SaaS externo | O fluxo depende de uma conta externa no Make.com conectada ao Gmail e Google Drive. Não há código standalone reproduzível no ambiente local. |

#### G. Potencial de Customização e Modernização (Roadmap)
1. **Pipeline RAG Robusto (Vector Search):** Implementar um pipeline RAG com **LangChain** ou **LlamaIndex**, fatiando os manuais em chunks semânticos com sobreposição, gerando embeddings com `text-embedding-004` e armazenando em um banco vetorial local (**ChromaDB** ou **Qdrant**).
2. **Avaliação Automatizada (RAG Triad):** Implementar testes automatizados com frameworks como **Ragas** ou **DeepEval** para mensurar relevância de contexto, precisão da resposta (*faithfulness*) e resposta à pergunta.
3. **Webhook e Dispatcher Autônomo:** Desenvolver uma aplicação em Python conectada à API do Gmail ou IMAP/SMTP empresarial, operando em container Docker autônomo com trilha de auditoria completa em banco de dados.

---

## 3. Auditoria de Segurança, Governança e Boas Práticas

Durante a varredura profunda no workspace, foram identificadas vulnerabilidades e não-conformidades técnicas que devem ser sanadas:

### 3.1. [CRÍTICO] Exposição de Credencial em Arquivo de Texto
- **Localização:** `Arquivos aula 3/Arquivos - Aula 3/Chave Key Gemini Projeto ONE.txt`
- **Conteúdo Identificado:** Uma chave/token da API do Google Gemini (`AQ.Ab8RN6...`).
- **Risco:** O versionamento ou compartilhamento acidental deste repositório expõe a cota de uso, faturamento e acesso à infraestrutura do Google Cloud associada à conta.
- **Recomendação de Engenharia Imediata:**
  1. Revogar/rotacionar a chave imediatamente no console do Google AI Studio / Google Cloud.
  2. Remover o arquivo com a chave física do repositório.
  3. Criar um arquivo `.env.example` para documentar a variável `GEMINI_API_KEY`.
  4. Adicionar `.env` e chaves sensíveis ao `.gitignore`.

### 3.2. [ESTRUTURAL] Duplicidade e Aninhamento Redundante de Pastas
- Todas as três pastas do projeto possuem um nível intermediário desnecessário resultante de descompactação incorreta:
  - `Arquivos aula 1/Arquivos - Aula 1/...`
  - `Arquivos aula 2/Arquivos - Aula 2/...`
  - `Arquivos aula 3/Arquivos - Aula 3/...`
- **Impacto:** Caminhos de arquivo excessivamente longos, propensos a problemas de limite de path no Windows (`MAX_PATH`) e dificuldade de navegação no terminal e IDEs.

### 3.3. [QUALIDADE] Erros de Grafia e Nomenclaturas Não-Semânticas
- Arquivo `Aulal 1 - Prompts.txt` com erro evidente de digitação no nome (`Aulal`).
- Pastas e arquivos com espaços, caracteres acentuados e formatos mistos (`Docs-Ref` vs `Base-Conhecimento` vs `Base Conhecimento Apps Oracle.url`), dificultando a manipulação segura via scripts de CI/CD e shells multiplataforma.

---

## 4. Matriz Comparativa dos Projetos

| Dimensão | Aula 1: ARI NEWS | Aula 2: ARI DEAL | Aula 3: ARI SUPPORT |
|---|---|---|---|
| **Domínio de Negócio** | Inteligência de Mercado / Curadoria | Pré-Vendas & Propostas Comerciais B2B | Suporte Técnico N1/N2 & Atendimento |
| **Entradas de Usuário** | Setor, Região, Data | Briefing em texto/DOCX ou Diálogo em 5 etapas | E-mails recebidos (Assunto + Corpo) |
| **Modelos de IA** | Gemini (Busca Web) + Imagen (Imagem) | LLM para extração e validação de regras | Gemini (Classificador Binário + RAG) |
| **Mecanismo de Orquestração** | Nós do Google Opal | Conversação orientada por regras / Codex Skill | Make.com / n8n acoplado ao Gmail/Drive |
| **Saída Principal** | Página HTML renderizada em iframe CSP | Documento Word (.docx) no padrão visual | E-mail corporativo em HTML com fontes |
| **Maturidade Técnica Atual** | Média (Conceitual / No-Code) | Alta (Regras e bases maduras) | Média-Alta (Bases ricas, RAG ingênuo) |
| **Stack Recomendada de Produção** | FastAPI + Next.js + Gemini Flash | FastAPI + Streamlit + python-docx + Pydantic | Python + LangChain + ChromaDB + IMAP/SMTP |

---

## 5. Plano de Reestruturação e Renomeação Semântica

Para adequar o workspace aos padrões de excelência de Engenharia de Software, propõe-se:
1. Eliminar a pasta aninhada redundante em cada projeto.
2. Adotar convenção universal `kebab-case` para diretórios e arquivos de configuração.
3. Agrupar logicamente os componentes de cada projeto em pastas padronizadas: `prompts/`, `base-conhecimento/`, `docs-ref/`.
4. Isolar credenciais sensíveis através de `.env.example`.

### 5.1. Tabela "De -> Para" Completa

| Item | Caminho Atual (Origem) | Novo Caminho Proposto (Destino) | Justificativa Semântica |
|---|---|---|---|
| **Dir** | `Arquivos aula 1/` e subpasta `Arquivos - Aula 1/` | `01-ari-news-dashboard/` | Nome descritivo da aplicação, eliminando aninhamento redundante |
| **Arq** | `.../Aulal 1 - Prompts.txt` | `01-ari-news-dashboard/prompts/ari-news-prompts.md` | Corrige o erro de digitação (`Aulal`), converte para markdown estruturado |
| **Dir** | `Arquivos aula 2/` e subpasta `Arquivos - Aula 2/` | `02-ari-deal-propostas/` | Identifica a finalidade comercial do módulo sem duplicidade |
| **Arq** | `.../Docs-Ref/briefing-teste-vetria-embalagens.txt` | `02-ari-deal-propostas/docs-ref/briefing-vetria-embalagens.txt` | Padronização em `kebab-case` sem redundância |
| **Arq** | `.../Docs-Ref/instrucoes-ari-deal.txt` | `02-ari-deal-propostas/docs-ref/instrucoes-ari-deal.txt` | Mantém rastreabilidade com padrão limpo |
| **Arq** | `.../Docs-Ref/Prompt Aula 2.txt` | `02-ari-deal-propostas/docs-ref/prompt-skill-codex.txt` | Nome semântico que descreve o objetivo da criação da Skill |
| **Arq** | `.../Base-Conhecimento/brand-book.json` | `02-ari-deal-propostas/base-conhecimento/brand-book.json` | Mantido e padronizado em minúsculas |
| **Arq** | `.../Base-Conhecimento/Catalogo-Servicos-2026-ARI-CONSULTING.pdf` | `02-ari-deal-propostas/base-conhecimento/catalogo-servicos-2026.pdf` | Nome simplificado e sem redundância |
| **Arq** | `.../Base-Conhecimento/Proposta-047-2026-Banco-Central-Sul-ARI-CONSULTING.pdf` | `02-ari-deal-propostas/base-conhecimento/benchmark-proposta-047-banco-central-sul.pdf` | Clarifica que o arquivo é um exemplo/benchmark |
| **Arq** | `.../Base-Conhecimento/Proposta-061-2026-Logistica-Norte-ARI-CONSULTING.pdf` | `02-ari-deal-propostas/base-conhecimento/benchmark-proposta-061-logistica-norte.pdf` | Clarifica que o arquivo é um exemplo/benchmark |
| **Arq** | `.../Base-Conhecimento/Proposta-Comercial-ARI-CONSULTING.docx` | `02-ari-deal-propostas/base-conhecimento/template-proposta-comercial.docx` | Destaca sua função estrutural como gabarito |
| **Dir** | `Arquivos aula 3/` e subpasta `Arquivos - Aula 3/` | `03-ari-support-rag/` | Nome descritivo da aplicação RAG e suporte |
| **Arq** | `.../Aula 3 - Prompts.txt` | `03-ari-support-rag/prompts/prompts-triagem-e-resposta.md` | Nome explícito para a finalidade dos prompts |
| **Arq** | `.../Base Conhecimento Apps Oracle.url` | `03-ari-support-rag/base-conhecimento/referencia-google-docs-apps-oracle.url` | Nome legível sem espaços |
| **Arq** | `.../Chave Key Gemini Projeto ONE.txt` | `03-ari-support-rag/.env.example` *(conteúdo higienizado)* | Elimina chave exposta e cria template seguro |
| **Arq** | `.../Oracle Fusion Cloud Financials.md` | `03-ari-support-rag/base-conhecimento/oracle-fusion-cloud-financials.md` | Padronização em `kebab-case` minúsculo |
| **Arq** | `.../Oracle Fusion Cloud HCM.md` | `03-ari-support-rag/base-conhecimento/oracle-fusion-cloud-hcm.md` | Padronização em `kebab-case` minúsculo |
| **Arq** | `.../Oracle Fusion Cloud Sales.md` | `03-ari-support-rag/base-conhecimento/oracle-fusion-cloud-sales.md` | Padronização em `kebab-case` minúsculo |
| **Arq** | `.../Oracle Fusion Cloud Supply Chain.md` | `03-ari-support-rag/base-conhecimento/oracle-fusion-cloud-supply-chain.md` | Padronização em `kebab-case` minúsculo |

---

### 5.2. Script PowerShell para Execução Segura e Idempotente

> [!WARNING]
> **Aviso de Congelamento:** O script abaixo **não foi executado**. Ele está preparado para execução após a aprovação formal do usuário, garantindo a integridade dos dados, tratamento de erros e remoção segura das pastas órfãs.

```powershell
<#
.SYNOPSIS
    Script de Reestruturação e Padronização Semântica do Workspace Imersao-Alura
.DESCRIPTION
    Cria a nova árvore de diretórios, move e renomeia os arquivos de forma segura,
    higieniza o arquivo de credenciais e remove as pastas antigas redundantes.
#>

$ErrorActionPreference = "Stop"
$root = Get-Location

Write-Host "Iniciando reestruturação semântica do workspace: $root" -ForegroundColor Cyan

# 1. Criação da nova estrutura de diretórios
$novosDiretorios = @(
    "01-ari-news-dashboard/prompts",
    "02-ari-deal-propostas/docs-ref",
    "02-ari-deal-propostas/base-conhecimento",
    "03-ari-support-rag/prompts",
    "03-ari-support-rag/base-conhecimento"
)

foreach ($dir in $novosDiretorios) {
    $fullPath = Join-Path $root $dir
    if (-not (Test-Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath -Force | Out-Null
        Write-Host "[+] Diretório criado: $dir" -ForegroundColor Green
    }
}

# 2. Migração dos arquivos da Aula 1
$aula1Origem = "Arquivos aula 1/Arquivos - Aula 1/Aulal 1 - Prompts.txt"
$aula1Destino = "01-ari-news-dashboard/prompts/ari-news-prompts.md"
if (Test-Path $aula1Origem) {
    Move-Item -Path $aula1Origem -Destination $aula1Destino -Force
    Write-Host "[->] Movido e renomeado: $aula1Destino" -ForegroundColor Yellow
}

# 3. Migração dos arquivos da Aula 2 - Docs-Ref
$mapaAula2Docs = @{
    "Arquivos aula 2/Arquivos - Aula 2/Docs-Ref/briefing-teste-vetria-embalagens.txt" = "02-ari-deal-propostas/docs-ref/briefing-vetria-embalagens.txt"
    "Arquivos aula 2/Arquivos - Aula 2/Docs-Ref/instrucoes-ari-deal.txt"              = "02-ari-deal-propostas/docs-ref/instrucoes-ari-deal.txt"
    "Arquivos aula 2/Arquivos - Aula 2/Docs-Ref/Prompt Aula 2.txt"                  = "02-ari-deal-propostas/docs-ref/prompt-skill-codex.txt"
}

foreach ($origem in $mapaAula2Docs.Keys) {
    if (Test-Path $origem) {
        $destino = $mapaAula2Docs[$origem]
        Move-Item -Path $origem -Destination $destino -Force
        Write-Host "[->] Movido e renomeado: $destino" -ForegroundColor Yellow
    }
}

# 4. Migração dos arquivos da Aula 2 - Base-Conhecimento
$mapaAula2Base = @{
    "Arquivos aula 2/Arquivos - Aula 2/Base-Conhecimento/brand-book.json"                              = "02-ari-deal-propostas/base-conhecimento/brand-book.json"
    "Arquivos aula 2/Arquivos - Aula 2/Base-Conhecimento/Catalogo-Servicos-2026-ARI-CONSULTING.pdf"      = "02-ari-deal-propostas/base-conhecimento/catalogo-servicos-2026.pdf"
    "Arquivos aula 2/Arquivos - Aula 2/Base-Conhecimento/Proposta-047-2026-Banco-Central-Sul-ARI-CONSULTING.pdf" = "02-ari-deal-propostas/base-conhecimento/benchmark-proposta-047-banco-central-sul.pdf"
    "Arquivos aula 2/Arquivos - Aula 2/Base-Conhecimento/Proposta-061-2026-Logistica-Norte-ARI-CONSULTING.pdf"   = "02-ari-deal-propostas/base-conhecimento/benchmark-proposta-061-logistica-norte.pdf"
    "Arquivos aula 2/Arquivos - Aula 2/Base-Conhecimento/Proposta-Comercial-ARI-CONSULTING.docx"          = "02-ari-deal-propostas/base-conhecimento/template-proposta-comercial.docx"
}

foreach ($origem in $mapaAula2Base.Keys) {
    if (Test-Path $origem) {
        $destino = $mapaAula2Base[$origem]
        Move-Item -Path $origem -Destination $destino -Force
        Write-Host "[->] Movido e renomeado: $destino" -ForegroundColor Yellow
    }
}

# 5. Migração dos arquivos da Aula 3 - Prompts e Base
$mapaAula3 = @{
    "Arquivos aula 3/Arquivos - Aula 3/Aula 3 - Prompts.txt"                  = "03-ari-support-rag/prompts/prompts-triagem-e-resposta.md"
    "Arquivos aula 3/Arquivos - Aula 3/Base Conhecimento Apps Oracle.url"      = "03-ari-support-rag/base-conhecimento/referencia-google-docs-apps-oracle.url"
    "Arquivos aula 3/Arquivos - Aula 3/Oracle Fusion Cloud Financials.md"     = "03-ari-support-rag/base-conhecimento/oracle-fusion-cloud-financials.md"
    "Arquivos aula 3/Arquivos - Aula 3/Oracle Fusion Cloud HCM.md"            = "03-ari-support-rag/base-conhecimento/oracle-fusion-cloud-hcm.md"
    "Arquivos aula 3/Arquivos - Aula 3/Oracle Fusion Cloud Sales.md"          = "03-ari-support-rag/base-conhecimento/oracle-fusion-cloud-sales.md"
    "Arquivos aula 3/Arquivos - Aula 3/Oracle Fusion Cloud Supply Chain.md"   = "03-ari-support-rag/base-conhecimento/oracle-fusion-cloud-supply-chain.md"
}

foreach ($origem in $mapaAula3.Keys) {
    if (Test-Path $origem) {
        $destino = $mapaAula3[$origem]
        Move-Item -Path $origem -Destination $destino -Force
        Write-Host "[->] Movido e renomeado: $destino" -ForegroundColor Yellow
    }
}

# 6. Higienização da Chave de API e criação do .env.example
$chaveOrigem = "Arquivos aula 3/Arquivos - Aula 3/Chave Key Gemini Projeto ONE.txt"
if (Test-Path $chaveOrigem) {
    Remove-Item -Path $chaveOrigem -Force
    Write-Host "[!] Chave exposta removida por segurança!" -ForegroundColor Red
}

$envExamplePath = "03-ari-support-rag/.env.example"
$envContent = @"
# Configuração de Credenciais - ARI SUPPORT RAG
# Obtenha sua chave no Google AI Studio (https://aistudio.google.com/)
GEMINI_API_KEY=sua_chave_gemini_aqui
GMAIL_USER=seu_email@empresa.com
GMAIL_APP_PASSWORD=sua_senha_de_aplicativo_aqui
"@
Set-Content -Path $envExamplePath -Value $envContent -Encoding UTF8
Write-Host "[+] Arquivo modelo .env.example criado com sucesso!" -ForegroundColor Green

# 7. Criação de arquivo .gitignore na raiz (se não existir)
$gitignorePath = ".gitignore"
$gitignoreContent = @"
.env
*.token
*secret*
*.log
__pycache__/
"@
if (-not (Test-Path $gitignorePath)) {
    Set-Content -Path $gitignorePath -Value $gitignoreContent -Encoding UTF8
    Write-Host "[+] Arquivo .gitignore criado na raiz!" -ForegroundColor Green
}

# 8. Limpeza de diretórios antigos vazios
$diretoriosAntigos = @(
    "Arquivos aula 1/Arquivos - Aula 1",
    "Arquivos aula 1",
    "Arquivos aula 2/Arquivos - Aula 2/Base-Conhecimento",
    "Arquivos aula 2/Arquivos - Aula 2/Docs-Ref",
    "Arquivos aula 2/Arquivos - Aula 2",
    "Arquivos aula 2",
    "Arquivos aula 3/Arquivos - Aula 3",
    "Arquivos aula 3"
)

foreach ($dir in $diretoriosAntigos) {
    if (Test-Path $dir) {
        Remove-Item -Path $dir -Recurse -Force
        Write-Host "[-] Diretório obsoleto removido: $dir" -ForegroundColor DarkGray
    }
}

Write-Host "`nReestruturação concluída com sucesso e integridade preservada!" -ForegroundColor Cyan
```

---

## 6. Conclusão e Próximos Passos

O repositório apresenta material didático e prático de alto valor sobre o uso de IA Generativa aplicada a processos corporativos em soluções Oracle. Com a reestruturação semântica, higienização das credenciais e desacoplamento das soluções em código versionável, o projeto evolui de uma coleção de exercícios para uma base profissional sólida de soluções em IA.

**Aguardando autorização:** Mediante a sua validação, o script PowerShell acima será executado no terminal para aplicar imediatamente as mudanças físicas no workspace.
