# Oracle Fusion Cloud Human Capital Management (HCM)

## Manual Completo de Referência, Arquitetura e Módulos

---

## 1. Visão Geral Estratégica e Filosofia da Plataforma

O **Oracle Fusion Cloud HCM** é uma suíte de aplicativos nativa em nuvem projetada para conectar todos os processos de recursos humanos — e todas as pessoas — de uma organização global. Ao contrário de soluções fragmentadas que dependem de integrações complexas, o Oracle Cloud HCM é construído sobre um **modelo de dados único** (*Single Source of Truth*) e uma infraestrutura unificada.

### Diferenciais Core:

* **Experiência de Usuário Unificada (Redwood Design):** Interface consistente, responsiva e adaptável que aprende com o comportamento do usuário e simplifica tarefas diárias em qualquer dispositivo.
* **Inteligência Artificial Incorporada (Fusion AI):** Uso extensivo de IA Tradicional, Machine Learning e Inteligência Artificial Generativa (GenAI) integrados diretamente nos fluxos de trabalho funcionais para recrutamento, sugestão de competências, automação de tarefas e análise preditiva.
* **Conexão Nativa com o Ecossistema Cloud:** Integração fluida out-of-the-box com o Oracle ERP (Financeiro), SCM (Cadeia de Suprimentos) e CX (Vendas/Atendimento), permitindo alinhar a estratégia de pessoas ao planejamento orçamentário e operacional do negócio.
* **Localização e Conformidade Global:** Suporte nativo para gerenciar forças de trabalho em mais de 200 países e jurisdições, atendendo a complexidades de leis trabalhistas locais, acordos sindicais e requerimentos regulatórios estruturados.

---

## 2. Arquitetura Funcional e Principais Módulos

A suíte está dividida em pilares fundamentais, cobrindo todo o ciclo de vida do colaborador (do recrutamento à aposentadoria).

### 2.1. Global Human Resources (Core HR)

É a fundação de todo o sistema. Gerencia as estruturas organizacionais, perfis de funcionários e a conformidade global.

* **Core HR:** Permite a modelagem flexível de posições, cargos, estruturas de relatórios organizacionais e o gerenciamento de múltiplos tipos de contratos de trabalho (CLT, prestadores de serviço, contingentes).
* **Oracle Benefits:** Sistema configurável para a administração e elegibilidade de pacotes de benefícios complexos, autoatendimento durante períodos de contratação aberta (*open enrollment*) e processamento de eventos de vida.
* **Workforce Modeling and Predictions:** Ferramentas gráficas de arrastar e soltar que permitem aos gestores simular reestruturações organizacionais, avaliar impactos financeiros e prever taxas de atrito/turnover com o suporte de IA.
* **HR Help Desk:** Uma solução nativa de gerenciamento de casos de RH que garante a privacidade dos dados operacionais e permite que os funcionários resolvam dúvidas por meio de solicitações de serviço automatizadas.

### 2.2. Talent Management (Gestão de Talentos)

Visa atrair, desenvolver, engajar e reter os melhores profissionais.

* **Oracle Recruiting & Recruiting Booster:** Sistema de rastreamento de candidatos (ATS) nativo. Utiliza IA para classificar candidatos ideais, prever a probabilidade de aceitação de propostas e automatizar campanhas de recrutamento e agendamentos de entrevistas.
* **Onboarding:** Fluxos de trabalho automatizados direcionados que engajam o novo colaborador desde o pré-emprego, garantindo que ele tenha acesso a ferramentas, treinamentos e documentações desde o primeiro dia.
* **Learning:** Plataforma corporativa de E-learning (LMS) que suporta trilhas de aprendizagem, catálogos de cursos, certificações obrigatórias e compartilhamento de conhecimento peer-to-peer.
* **Dynamic Skills:** Uma plataforma orientada por IA que inventaria e atualiza continuamente o mapa de competências da empresa, recomendando habilidades para os perfis dos funcionários com base no mercado de trabalho global.
* **Performance, Goal & Succession Management:** Gestão contínua de metas organizacionais e individuais, avaliações de desempenho flexíveis (anuais, 360°, check-ins contínuos) e planejamento de sucessão para mitigar os riscos de liderança com pipelines de talentos estruturados.

### 2.3. Workforce Management (Gestão da Força de Trabalho)

Otimiza a alocação de tempo, custos e garante a segurança do ambiente corporativo.

* **Absence Management:** Rastreamento global de ausências, licenças médicas, férias e afastamentos de acordo com regras locais de conformidade de cada país.
* **Time and Labor:** Sistema robusto de controle de ponto e presença. Permite o registro via web, dispositivos móveis ou relógios de ponto, gerando regras complexas de cálculo de horas extras e adicionais noturnos integrados à folha.
* **Workforce Scheduling & Labor Optimization:** Criação de escalas de trabalho e turnos complexos para indústrias, varejo ou saúde, equilibrando a demanda operacional com as restrições de custos trabalhistas.
* **Workforce Health and Safety:** Módulo dedicado para relatar incidentes de segurança no trabalho, rastrear investigações, auditorias e garantir a conformidade com normas regulamentadoras (como a CIPA e eSocial no Brasil).

### 2.4. Payroll (Folha de Pagamento Global)

Uma engine de cálculo altamente configurável projetada para processar folhas de pagamento de alta escala com precisão e segurança.

* **Localizações de Folha Nativas:** Disponibilidade de motores de cálculo locais para mercados complexos (como EUA, Reino Unido, Canadá, México, Arábia Saudita, etc.) e flexibilidade para integração via APIs com fornecedores de folha locais em outros países.
* **Integração Financeira Recíproca:** Distribuição automática de custos de pessoal diretamente para o livro razão (*General Ledger*) do ERP Cloud de maneira transparente.

### 2.5. Oracle ME (Employee Experience Platform)

A plataforma de experiência do colaborador focada em aumentar o engajamento e a comunicação aberta.

* **Journeys:** Criação de guias passo a passo personalizados para momentos importantes da vida do colaborador (ex: guias de licença paternidade, promoções, transferências ou processos pessoais).
* **Touchpoints:** Ferramenta para gerentes estimularem interações regulares com suas equipes, acompanhando o clima organizacional e agendando feedbacks contínuos.
* **Connections:** Um diretório social corporativo inteligente onde os colaboradores podem encontrar especialistas internos por meio de filtros de habilidades, competências e estruturas de equipe.
* **Oracle Communicate:** Permite que o RH crie, dispare e mensure o impacto de campanhas de comunicação interna segmentadas para públicos específicos.

---

## 3. Segurança, Governança e Inteligência de Dados

Para apoiar a robustez do sistema, o Oracle Cloud HCM emprega camadas críticas de governança corporativa e análise de dados.

### 3.1. Oracle Advanced HCM Controls

* Utiliza algoritmos de Machine Learning para auditar e monitorar continuamente o acesso a dados confidenciais de RH.
* Detecta automaticamente anomalias de segurança, violações de segregação de funções (*Segregation of Duties - SoD*) e previne potenciais fraudes internas gerando alertas em tempo real para os administradores do sistema.

### 3.2. Oracle Fusion HCM Analytics

* Alimentado pelo *Oracle Autonomous Data Warehouse* e *Oracle Analytics Cloud*.
* Oferece KPIs e dashboards pré-construídos prontos para uso para analisar diversidade (DE&I), custos de força de trabalho, retenção de talentos e eficiência de contratação.
* Capacidade de mesclar dados do HCM com dados externos (vendas, finanças, CRM) para criar correlações estratégicas de negócios de ponta a ponta.

---

## 4. Integração, APIs e Ciclo de Atualizações

O Oracle Cloud HCM é extensível e preparado para ambientes híbridos através das seguintes capacidades técnicas:

### 4.1. Interfaces de Extensibilidade e APIs

* **REST e SOAP APIs:** Amplo catálogo de APIs RESTful atualizadas continuamente para leitura, gravação e sincronização de entidades de dados de funcionários, estruturas, registros de ponto e remuneração.
* **Tables and Views:** Documentação detalhada do esquema lógico de banco de dados subjacente para a construção de relatórios BI Publisher personalizados de alta complexidade.
* **Oracle Visual Builder Studio:** Ferramenta low-code integrada para estender telas, fluxos e regras de negócio da interface Redwood sem quebrar a compatibilidade com atualizações futuras.

### 4.2. Modelo de Entrega Contínua (Updates Trimestrais)

A Oracle adota uma estratégia de inovação contínua dividida em atualizações trimestrais mandatórias (Ex: Releases de Updates como 24A, 24B, 25A, etc.).

* **Cloud Readiness:** A Oracle fornece documentação cumulativa de prontidão com semanas de antecedência, detalhando as novas funcionalidades incluídas.
* **Mecanismo Opt-In:** Muitas novas ferramentas ou melhorias arquiteturais profundas vêm desativadas por padrão, permitindo que a equipe de RH e TI realize testes em ambientes de homologação (*Test*) antes de ativá-las em produção.

---
