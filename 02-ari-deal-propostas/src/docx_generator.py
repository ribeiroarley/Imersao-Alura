"""
ARI DEAL — Gerador de Proposta Comercial em Formato Word (.docx)
ARI Consulting | Módulo 2

Este script consome a proposta validada pelo deal_validator.py (caso Vetria Embalagens)
e preenche o documento mestre template-proposta-comercial.docx com precisão milimétrica,
respeitando integralmente o Brand Book e as diretrizes corporativas da ARI Consulting.
"""

from datetime import date
from decimal import Decimal
import os
from pathlib import Path
from typing import Dict, List, Optional
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Importação do validador determinístico do Módulo 2
from deal_validator import (
    build_vetria_proposal_082,
    CommercialProposalProposal,
    format_currency_brl,
    OFFICIAL_CATALOG_2026,
    ServiceCode,
)

# ---------------------------------------------------------------------------
# 1. Configuração de Caminhos
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = BASE_DIR / "base-conhecimento" / "template-proposta-comercial.docx"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DOCX_PATH = OUTPUT_DIR / "Proposta_Comercial_Vetria_Embalagens.docx"


# ---------------------------------------------------------------------------
# 2. Funções Auxiliares de Substituição no python-docx
# ---------------------------------------------------------------------------

def replace_in_paragraph(paragraph: docx.text.paragraph.Paragraph, old_text: str, new_text: str) -> bool:
    """
    Substitui old_text por new_text preservando formatação existente
    (estilo, negrito, fonte) sempre que possível.
    """
    if old_text not in paragraph.text:
        return False

    # Caso 1: o texto a substituir está inteiramente contido em um único run
    for run in paragraph.runs:
        if old_text in run.text:
            run.text = run.text.replace(old_text, new_text)
            return True

    # Caso 2: o texto está fragmentado entre múltiplos runs do parágrafo
    full_text = paragraph.text.replace(old_text, new_text)
    if paragraph.runs:
        first_run = paragraph.runs[0]
        first_run.text = full_text
        for run in paragraph.runs[1:]:
            run.text = ""
    else:
        paragraph.text = full_text
    return True


def replace_in_cell(cell: docx.table._Cell, old_text: str, new_text: str) -> bool:
    """Substitui texto em células de tabela preservando a formatação do run."""
    found = False
    for p in cell.paragraphs:
        if replace_in_paragraph(p, old_text, new_text):
            found = True
    return found


def set_cell_content(cell: docx.table._Cell, text: str, bold: Optional[bool] = None, align=None) -> None:
    """Define o conteúdo textual de uma célula preservando estilo de run existente."""
    if cell.paragraphs:
        p = cell.paragraphs[0]
        if align is not None:
            p.alignment = align
        if p.runs:
            first_run = p.runs[0]
            first_run.text = text
            if bold is not None:
                first_run.bold = bold
            for r in p.runs[1:]:
                r.text = ""
        else:
            r = p.add_run(text)
            if bold is not None:
                r.bold = bold
        # Remove parágrafos adicionais se houver
        for extra_p in cell.paragraphs[1:]:
            p_elem = extra_p._p
            p_elem.getparent().remove(p_elem)
    else:
        p = cell.add_paragraph()
        if align is not None:
            p.alignment = align
        r = p.add_run(text)
        if bold is not None:
            r.bold = bold


# ---------------------------------------------------------------------------
# 3. Gerador Principal da Proposta Word
# ---------------------------------------------------------------------------

def generate_vetria_commercial_proposal() -> Path:
    """
    Carrega o template oficial, aplica os dados validados da Proposta nº 082/2026
    da Vetria Embalagens Industriais S.A. e salva o arquivo .docx final.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("ARI DEAL — Gerador de Propostas Comerciais (.docx)")
    print(f"Template Base: {TEMPLATE_PATH.name}")
    print("Obtendo dados validados via Pydantic para Vetria Embalagens S.A....")
    print("=" * 70)

    # 1. Carrega e valida os dados de negócio (Proposta 082/2026)
    proposal = build_vetria_proposal_082()

    # 2. Abre o modelo de documento corporativo
    if not TEMPLATE_PATH.exists():
        raise FileNotFoundError(f"Template não encontrado em: {TEMPLATE_PATH}")

    doc = docx.Document(str(TEMPLATE_PATH))

    # -----------------------------------------------------------------------
    # A. Atualização da Capa e Cabeçalhos
    # -----------------------------------------------------------------------
    # Parágrafo 4: Nº [XXX/2026]
    for p in doc.paragraphs[:10]:
        replace_in_paragraph(p, "[XXX/2026]", proposal.proposal_number)
        replace_in_paragraph(p, "Nº [XXX/2026]", f"Nº {proposal.proposal_number}")

    # Tabela 1: Metadados da Capa (Datas)
    table_meta = doc.tables[1]
    replace_in_cell(table_meta.rows[0].cells[1], "[DD/MM/AAAA]", proposal.emission_date.strftime("%d/%m/%Y"))
    replace_in_cell(table_meta.rows[1].cells[1], "[DD/MM/AAAA] — 30 dias corridos", f"{proposal.validity_date.strftime('%d/%m/%Y')} — 30 dias corridos")

    # Tabela 2: Dados do Cliente
    table_client = doc.tables[2]
    set_cell_content(table_client.rows[0].cells[1], proposal.client_name)
    set_cell_content(table_client.rows[1].cells[1], proposal.cnpj or "78.901.234/0001-56")
    set_cell_content(table_client.rows[2].cells[1], proposal.sector)
    set_cell_content(table_client.rows[3].cells[1], "Roberto Alencar (CFO) | Eng. Paulo Nagata (CIO)")
    set_cell_content(table_client.rows[4].cells[1], "roberto.alencar@vetria.com.br")
    set_cell_content(table_client.rows[5].cells[1], "(47) 3451-8900 / Joinville — SC")

    # Tabela 3: Dados da ARI Consulting
    table_ari = doc.tables[3]
    set_cell_content(table_ari.rows[0].cells[1], proposal.consultant_name)
    set_cell_content(table_ari.rows[1].cells[1], proposal.consultant_email)
    set_cell_content(table_ari.rows[2].cells[1], "(11) 3045-8800")
    set_cell_content(table_ari.rows[3].cells[1], "Mariana Prado (Diretora de Contas Enterprise)")
    set_cell_content(table_ari.rows[4].cells[1], "São Paulo — SP, Capital")

    # -----------------------------------------------------------------------
    # B. Seção 01 — Entendimento do Contexto
    # -----------------------------------------------------------------------
    context_text_1 = (
        "Compreendemos que a Vetria Embalagens Industriais S.A. consolidou-se como uma das maiores fabricantes "
        "de embalagens plásticas e flexíveis da Região Sul do Brasil, operando 5 plantas industriais distribuídas em "
        "Santa Catarina, Paraná e Rio Grande do Sul, faturamento anual de aproximadamente R$ 680 milhões e mais de 1.450 colaboradores. "
        "O crescimento acelerado por aquisições entre 2022 e 2025 agregou escala de mercado, mas também gerou uma arquitetura tecnológica "
        "fragmentada: a coexistência simultânea de três ERPs distintos (Totvs Protheus na matriz, Sankhya em duas unidades e um sistema "
        "proprietário em Delphi na planta mais antiga). Atualmente, a controladoria corporativa atua como um 'tradutor manual' contínuo entre esses três ambientes."
    )
    context_text_2 = (
        "Essa dispersão de sistemas acarreta dores operacionais críticas para a governança corporativa: (1) O fechamento contábil mensal "
        "consome 14 dias úteis decorrente da consolidação manual de planos de contas incompatíveis via planilhas — muito distante da meta do CFO "
        "Roberto Alencar de 5 dias úteis; (2) Contas a Pagar descentralizado e sem alçadas unificadas gerou 23 pagamentos duplicados no último ano, "
        "totalizando R$ 340 mil recuperados com esforço jurídico; (3) A apuração da posição de caixa consome 3 horas diárias cruzando 11 contas bancárias, "
        "sendo finalizada após as 11h, inviabilizando decisões ideais de tesouraria; (4) O parque de 4.200 ativos industriais é depreciado em planilhas "
        "heterogêneas, gerando apontamentos em auditorias externas."
    )
    context_text_3 = (
        "A presente proposta visa sanear integralmente esses gargalos através da implantação do Oracle Fusion Cloud Financials e da "
        "integração inteligente de sistemas legados, garantindo governança contábil unificada antes do início do ciclo orçamentário de 2027 "
        "(1º de setembro de 2026), respeitando a transição gradual sem ruptura operacional fabril."
    )

    # Injeção no bloco de texto da Seção 01
    doc.paragraphs[10].text = context_text_1
    doc.paragraphs[11].text = context_text_2
    doc.paragraphs[12].text = context_text_3
    doc.paragraphs[13].text = (
        "Com esse diagnóstico preciso, a ARI CONSULTING desenhou uma solução sob medida para garantir estabilidade, "
        "automação e visibilidade contínua para a diretoria executiva da Vetria."
    )

    # -----------------------------------------------------------------------
    # C. Seção 02 — Solução Proposta
    # -----------------------------------------------------------------------
    doc.paragraphs[16].text = (
        "Para responder com precisão às prioridades da Vetria Embalagens, recomendamos a contratação de dois serviços "
        "complementares do catálogo oficial da ARI CONSULTING, assegurando modernização com risco zero:"
    )

    # Serviço 01: ERP Cloud Financials
    doc.paragraphs[18].text = "Implementação Oracle ERP Cloud (Financials)"
    doc.paragraphs[18].runs[0].bold = True
    doc.paragraphs[20].text = (
        "Implantar uma espinha dorsal contábil e financeira única em nuvem para as 5 plantas da Vetria, centralizando "
        "a governança corporativa, acelerando o fechamento fiscal e blindando o contas a pagar contra pagamentos indevidos."
    )
    doc.paragraphs[22].text = "• General Ledger (GL): Plano de contas corporativo único, estrutura de centros de custos padronizada e consolidação contábil automática para fechamento em até 5 dias úteis."
    doc.paragraphs[23].text = "• Accounts Payable (AP): Centralização de pagamentos, governança por alçadas rígidas de aprovação e conferência preventiva contra faturas em duplicidade."
    doc.paragraphs[24].text = "• Cash Management: Conciliação bancária automatizada para as 11 contas bancárias, projetando fluxo de caixa consolidado logo no início da manhã."

    # Serviço 02: Integração de Sistemas Legados
    doc.paragraphs[26].text = "Integração Oracle com Sistemas Legados"
    doc.paragraphs[26].runs[0].bold = True
    doc.paragraphs[28].text = (
        "Garantir a operação contínua e a convivência das plantas industriais durante a transição de 6 a 12 meses, "
        "conforme diretriz do CIO Eng. Paulo Nagata, eliminando qualquer abordagem de 'big bang'."
    )
    doc.paragraphs[30].text = "• Oracle Integration Cloud (OIC): Desenvolvimento de conectores seguros e homologados entre o Oracle Cloud e os sistemas Totvs Protheus, Sankhya e Delphi."
    doc.paragraphs[31].text = "• Fluxo Automatizado de Dados: Recepção em lote e em tempo real de notas fiscais, movimentações de compras e partidas contábeis sem redigitação manual."
    doc.paragraphs[32].text = "• Monitoramento & Resiliência: Painel de gestão de mensageria com reprocessamento automático de falhas e trilha de auditoria completa de cada integração."

    # -----------------------------------------------------------------------
    # D. Seção 03 — Metodologia e Cronograma (OCIM)
    # -----------------------------------------------------------------------
    doc.paragraphs[37].text = "FASE 1 — DESCOBERTA   Semanas 1 a 3"
    doc.paragraphs[37].runs[0].bold = True
    doc.paragraphs[38].text = "Alinhamento de escopo executivo, formação do comitê de projeto, levantamento detalhado das especificidades contábeis das 5 plantas e mapa de requisitos de integração."

    doc.paragraphs[39].text = "FASE 2 — DESIGN   Semanas 4 a 7"
    doc.paragraphs[39].runs[0].bold = True
    doc.paragraphs[40].text = "Desenho do plano de contas corporativo unificado, validação do modelo contábil TO-BE com a controladoria e especificação técnica dos conectores OIC para Protheus, Sankhya e Delphi."

    doc.paragraphs[41].text = "FASE 3 — BUILD   Semanas 8 a 13"
    doc.paragraphs[41].runs[0].bold = True
    doc.paragraphs[42].text = "Parametrização integral dos módulos GL, AP e Cash Management no Oracle Cloud, desenvolvimento dos fluxos de integração OIC e esteira de carga de saldos históricos."

    doc.paragraphs[43].text = "FASE 4 — TESTES   Semanas 14 a 16"
    doc.paragraphs[43].runs[0].bold = True
    doc.paragraphs[44].text = "Testes integrados ponta a ponta (SIT), homologação dos fluxos com key users fabris (UAT) e simulação assistida de fechamento contábil mensal em 5 dias."

    doc.paragraphs[45].text = "FASE 5 — GO-LIVE   Semana 17 (31/08/2026)"
    doc.paragraphs[45].runs[0].bold = True
    doc.paragraphs[46].text = "Virada de chave e entrada oficial em produção do Oracle Financials antes de 01/09/2026, com suporte operacional intensivo (hypercare presencial e remoto) nas 2 primeiras semanas."

    doc.paragraphs[47].text = "FASE 6 — HIPERESCALADA   Semanas 18 a 20 (3 semanas pós go-live)"
    doc.paragraphs[47].runs[0].bold = True
    doc.paragraphs[48].text = "Acompanhamento do primeiro fechamento contábil oficial, validação de conciliações, transferência de conhecimento aos administradores e encerramento formal do projeto."

    # Tabela 4: Cronograma Sintético
    table_sched = doc.tables[4]
    set_cell_content(table_sched.rows[0].cells[1], "04/05/2026 (ou a confirmar na assinatura)")
    set_cell_content(table_sched.rows[1].cells[1], "31/08/2026 (Go-live operacional antes de 01/09/2026)")
    set_cell_content(table_sched.rows[2].cells[1], "120 dias corridos (17 semanas de implementação + 3 semanas de estabilização)")

    # -----------------------------------------------------------------------
    # E. Seção 04 — Investimento, Desconto e Condições de Pagamento
    # -----------------------------------------------------------------------
    # Tabela 5: Tabela Financeira
    table_finance = doc.tables[5]
    # Linha 1: Serviço 01 (Financials)
    set_cell_content(table_finance.rows[1].cells[0], "Implementação Oracle ERP Cloud (Financials)")
    set_cell_content(table_finance.rows[1].cells[1], "120 dias corridos")
    set_cell_content(table_finance.rows[1].cells[2], "R$ 255.000,00", bold=False)

    # Linha 2: Serviço 02 (Integração)
    set_cell_content(table_finance.rows[2].cells[0], "Integração Oracle com Sistemas Legados (OIC)")
    set_cell_content(table_finance.rows[2].cells[1], "60 dias corridos")
    set_cell_content(table_finance.rows[2].cells[2], "R$ 90.000,00", bold=False)

    # Linha 3: Desconto Comercial Combinado (10%)
    set_cell_content(table_finance.rows[3].cells[0], "Desconto Comercial Especial (10% — Pacote Combinado 2+ Serviços)")
    set_cell_content(table_finance.rows[3].cells[1], "—")
    set_cell_content(table_finance.rows[3].cells[2], "- R$ 34.500,00", bold=False)

    # Linha 4: Total do Projeto (Líquido)
    set_cell_content(table_finance.rows[4].cells[0], "TOTAL DO PROJETO (INVESTIMENTO LÍQUIDO)", bold=True)
    set_cell_content(table_finance.rows[4].cells[1], "120 dias corridos", bold=True)
    set_cell_content(table_finance.rows[4].cells[2], "R$ 310.500,00", bold=True)

    # Texto de desconto e teto orçamentário
    doc.paragraphs[54].text = (
        "POLÍTICA COMERCIAL & TETO ORÇAMENTÁRIO:\n"
        "Valor Bruto Consolidado: R$ 345.000,00. Pela contratação simultânea de 2 serviços estratégicos "
        "(Financials + Integração), aplicamos o Desconto Comercial de Pacote de 10% (-R$ 34.500,00), fixando o "
        "Investimento Líquido Total em R$ 310.500,00. Esse valor respeita rigorosamente o teto orçamentário aprovado "
        "pelo Conselho de Administração da Vetria de R$ 350.000,00, gerando uma economia imediata de R$ 39.500,00 sobre o orçamento autorizado."
    )

    # Condições de Pagamento Fixas (30% / 40% / 30%)
    doc.paragraphs[56].text = "• 30% na Assinatura do Contrato: R$ 93.150,00 (mobilização e início da Fase de Descoberta)"
    doc.paragraphs[57].text = "• 40% na Conclusão da Fase de Build: R$ 124.200,00 (entrega de módulos parametrizados e conectores OIC)"
    doc.paragraphs[58].text = "• 30% na Homologação e Go-Live confirmado: R$ 93.150,00 (corte operacional em 31/08/2026)"

    # Alçada Executiva e Governança (> R$ 200k)
    p_governanca = doc.paragraphs[59]
    p_governanca.text = (
        "GOVERNANÇA & ALÇADA EXECUTIVA (CONTRATO > R$ 200.000,00):\n"
        "Em estrita observância à política de governança da ARI CONSULTING para propostas com investimento superior a "
        "R$ 200.000,00, esta oferta inclui o Estudo de Caso de Referência (Benchmarking Proposta 047 - Banco Central Sul e "
        "Proposta 061 - Logística Norte) disponibilizado pela diretoria de Marketing e conta com a revisão e aprovação formal "
        "da Gerência de Contas Enterprise antes do envio ao cliente."
    )
    p_governanca.runs[0].bold = True

    doc.paragraphs[60].text = "Validade desta proposta: 30 dias corridos a partir da emissão (válida até 31/10/2026)."
    doc.paragraphs[61].text = "Valores em Reais (BRL). Não incluem impostos sobre serviços (ISS)."

    # -----------------------------------------------------------------------
    # F. Seção 05 — Próximos Passos & Assinatura
    # -----------------------------------------------------------------------
    doc.paragraphs[65].text = "01  Revisão e validação interna desta proposta pelo CFO Roberto Alencar e conselho da Vetria"
    doc.paragraphs[66].text = "02  Reunião de alinhamento técnico-executivo com o consultor responsável (Carlos Silveira) e CIO Paulo Nagata"
    doc.paragraphs[67].text = "03  Assinatura do contrato de prestação de serviços e respectiva ordem de serviço"
    doc.paragraphs[68].text = "04  Kickoff oficial do projeto em Joinville / remoto (até 10 dias após a assinatura)"

    # Assinatura
    doc.paragraphs[72].text = proposal.consultant_name
    doc.paragraphs[72].runs[0].bold = True
    doc.paragraphs[73].text = "Consultor Sênior de Soluções Oracle Cloud"
    doc.paragraphs[74].text = "ARI CONSULTING"
    doc.paragraphs[75].text = "São Paulo — Capital"
    doc.paragraphs[76].text = f"{proposal.consultant_email}  |  (11) 3045-8800"

    # Salva o arquivo gerado
    doc.save(str(OUTPUT_DOCX_PATH))

    file_size_kb = OUTPUT_DOCX_PATH.stat().st_size / 1024
    print(f"[SUCESSO] Proposta Comercial gerada com sucesso:")
    print(f" -> Arquivo: {OUTPUT_DOCX_PATH}")
    print(f" -> Tamanho: {file_size_kb:.2f} KB")
    print("=" * 70)
    return OUTPUT_DOCX_PATH


if __name__ == "__main__":
    generate_vetria_commercial_proposal()
