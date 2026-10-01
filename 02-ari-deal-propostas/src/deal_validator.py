"""
ARI DEAL — Motor de Validação de Regras de Negócio e Compliance Comercial
ARI Consulting | Módulo 2

Este módulo implementa a validação determinística de propostas comerciais
utilizando Pydantic v2, assegurando conformidade estrita com:
1. Catálogo Oficial de Serviços 2026 (8 serviços fechados).
2. Faixas de investimento permitidas por serviço.
3. Teto orçamentário do cliente (Budget Ceiling).
4. Política de descontos combinados (10% a 15% apenas para 2+ serviços).
5. Condições fixas de pagamento (30% Assinatura / 40% Build / 30% Go-Live).
6. Regras de alçada e governança corporativa (> R$ 200k exige case de referência).
"""

from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, field_validator, model_validator


# ===========================================================================
# 1. Catálogo Oficial de Serviços 2026 (ARI CONSULTING)
# ===========================================================================

class ServiceCode(str, Enum):
    SRV_01_HCM = "SRV-01"
    SRV_02_ERP = "SRV-02"
    SRV_03_SCM = "SRV-03"
    SRV_04_CX = "SRV-04"
    SRV_05_INTEGRACAO = "SRV-05"
    SRV_06_PROCESSOS = "SRV-06"
    SRV_07_TREINAMENTO = "SRV-07"
    SRV_08_SUPORTE = "SRV-08"


class CatalogService(BaseModel):
    """Definição canônica de um serviço no catálogo oficial 2026."""
    code: ServiceCode
    name: str
    description: str
    min_investment: Decimal
    max_investment: Decimal
    typical_duration_min_days: int
    typical_duration_max_days: int
    modules: List[str]


# Base de dados oficial dos 8 serviços canônicos da ARI Consulting
OFFICIAL_CATALOG_2026: Dict[ServiceCode, CatalogService] = {
    ServiceCode.SRV_01_HCM: CatalogService(
        code=ServiceCode.SRV_01_HCM,
        name="Implementação Oracle HCM Cloud",
        description="Implementação completa do módulo de Recursos Humanos da Oracle Cloud.",
        min_investment=Decimal("80000.00"),
        max_investment=Decimal("150000.00"),
        typical_duration_min_days=60,
        typical_duration_max_days=90,
        modules=["Core HR", "Folha de Pagamento", "Gestão de Ausências", "Recrutamento e Seleção", "Gestão de Talentos", "Benefícios"]
    ),
    ServiceCode.SRV_02_ERP: CatalogService(
        code=ServiceCode.SRV_02_ERP,
        name="Implementação Oracle ERP Cloud (Financials)",
        description="Implementação do módulo financeiro completo da Oracle Cloud.",
        min_investment=Decimal("120000.00"),
        max_investment=Decimal("260000.00"),
        typical_duration_min_days=90,
        typical_duration_max_days=120,
        modules=["General Ledger", "Accounts Payable", "Accounts Receivable", "Fixed Assets", "Expense Management", "Cash Management"]
    ),
    ServiceCode.SRV_03_SCM: CatalogService(
        code=ServiceCode.SRV_03_SCM,
        name="Implementação Oracle SCM Cloud (Supply Chain)",
        description="Implementação dos módulos de cadeia de suprimentos e logística integrada.",
        min_investment=Decimal("90000.00"),
        max_investment=Decimal("160000.00"),
        typical_duration_min_days=60,
        typical_duration_max_days=90,
        modules=["Inventory Management", "Purchasing", "Order Management", "Logistics"]
    ),
    ServiceCode.SRV_04_CX: CatalogService(
        code=ServiceCode.SRV_04_CX,
        name="Implementação Oracle CX Cloud (Customer Experience)",
        description="Implementação dos módulos de vendas, CRM omnichannel e marketing automation.",
        min_investment=Decimal("70000.00"),
        max_investment=Decimal("130000.00"),
        typical_duration_min_days=45,
        typical_duration_max_days=75,
        modules=["Sales Cloud", "Service Cloud", "Marketing Automation"]
    ),
    ServiceCode.SRV_05_INTEGRACAO: CatalogService(
        code=ServiceCode.SRV_05_INTEGRACAO,
        name="Integração Oracle com Sistemas Legados",
        description="Desenvolvimento e implementação de conectores OIC, REST APIs e middlewares.",
        min_investment=Decimal("40000.00"),
        max_investment=Decimal("90000.00"),
        typical_duration_min_days=30,
        typical_duration_max_days=60,
        modules=["Oracle Integration Cloud (OIC)", "REST APIs", "Middleware Customizado", "Conectores Protheus/Sankhya/SAP"]
    ),
    ServiceCode.SRV_06_PROCESSOS: CatalogService(
        code=ServiceCode.SRV_06_PROCESSOS,
        name="Consultoria de Processos (Pré-Implementação)",
        description="Diagnóstico AS-IS, mapa de processos TO-BE e roadmap priorizado de módulos Oracle.",
        min_investment=Decimal("25000.00"),
        max_investment=Decimal("55000.00"),
        typical_duration_min_days=15,
        typical_duration_max_days=30,
        modules=["Diagnóstico AS-IS", "Desenho TO-BE", "Roadmap de Arquitetura", "Estimativa de Esforço"]
    ),
    ServiceCode.SRV_07_TREINAMENTO: CatalogService(
        code=ServiceCode.SRV_07_TREINAMENTO,
        name="Treinamento de Usuários e Administradores",
        description="Capacitação de key users, administradores de sistema e gestores pós-go-live.",
        min_investment=Decimal("12000.00"),
        max_investment=Decimal("35000.00"),
        typical_duration_min_days=5,
        typical_duration_max_days=15,
        modules=["Capacitação Key Users", "Administração OCI/SaaS", "Trilha E-learning"]
    ),
    ServiceCode.SRV_08_SUPORTE: CatalogService(
        code=ServiceCode.SRV_08_SUPORTE,
        name="Suporte Pós-Implementação",
        description="Atendimento contínuo, sustenção e resolução de incidentes (Básico, Padrão ou Premium).",
        min_investment=Decimal("24000.00"),  # Pacote Básico: 3 meses x R$ 8.000
        max_investment=Decimal("240000.00"), # Pacote Premium: 12 meses x R$ 20.000
        typical_duration_min_days=90,
        typical_duration_max_days=365,
        modules=["Sustentação Operacional", "Ajustes de Configuração", "Atualizações Semestrais de Release"]
    ),
}


# ===========================================================================
# 2. Modelos Pydantic de Validação Comercial
# ===========================================================================

def format_currency_brl(value: Decimal) -> str:
    """Formata valor Decimal para o padrão monetário brasileiro (R$ 1.234,56)."""
    val_float = float(value)
    return f"R$ {val_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


class SelectedServiceItem(BaseModel):
    """Item de serviço selecionado para a proposta comercial."""
    service_code: ServiceCode = Field(..., description="Código do serviço no catálogo oficial 2026")
    investment: Decimal = Field(..., description="Valor de investimento proposto para o serviço")
    custom_scope_notes: Optional[str] = Field(None, description="Observações de escopo específico")

    @model_validator(mode="after")
    def validate_service_against_catalog(self) -> "SelectedServiceItem":
        """Valida se o serviço pertence ao catálogo e se o valor está estritamente dentro da faixa."""
        catalog_item = OFFICIAL_CATALOG_2026.get(self.service_code)
        if not catalog_item:
            raise ValueError(f"Serviço '{self.service_code}' não encontrado no catálogo oficial 2026.")

        if self.investment < catalog_item.min_investment or self.investment > catalog_item.max_investment:
            min_fmt = format_currency_brl(catalog_item.min_investment)
            max_fmt = format_currency_brl(catalog_item.max_investment)
            inv_fmt = format_currency_brl(self.investment)
            raise ValueError(
                f"Valor {inv_fmt} fora da faixa tabelada para '{catalog_item.name}'. "
                f"Faixa permitida: {min_fmt} a {max_fmt}."
            )
        return self


class PaymentSchedule(BaseModel):
    """Cronograma financeiro fixo com 3 marcos contratuais."""
    assinatura_percentage: Decimal = Decimal("30.00")
    assinatura_amount: Decimal
    build_percentage: Decimal = Decimal("40.00")
    build_amount: Decimal
    golive_percentage: Decimal = Decimal("30.00")
    golive_amount: Decimal
    total_amount: Decimal


class CommercialProposalProposal(BaseModel):
    """
    Estrutura completa e validadora de uma proposta comercial da ARI Consulting.
    """
    # Dados do Cliente
    client_name: str = Field(..., min_length=2, description="Razão Social da empresa cliente")
    cnpj: Optional[str] = Field(None, description="CNPJ da empresa")
    sector: str = Field(..., description="Setor de atuação")
    budget_ceiling: Optional[Decimal] = Field(None, description="Teto orçamentário aprovado pelo cliente")

    # Dados Internos ARI Consulting
    proposal_number: str = Field(..., pattern=r"^\d{3}/\d{4}$", description="Formato XXX/AAAA (ex: 047/2026)")
    consultant_name: str = Field(..., description="Nome do consultor responsável")
    consultant_email: str = Field(..., description="E-mail corporativo @ariconsulting.com.br")
    emission_date: date = Field(default_factory=date.today, description="Data de emissão da proposta")

    # Escopo e Precificação
    services: List[SelectedServiceItem] = Field(..., min_length=1, description="Lista de serviços contratados")
    discount_percentage: Decimal = Field(
        default=Decimal("0.00"),
        description="Percentual de desconto comercial (ex: 10.00 para 10%)"
    )

    # Campos Computados Gerados na Validação
    gross_total: Decimal = Field(default=Decimal("0.00"))
    discount_amount: Decimal = Field(default=Decimal("0.00"))
    net_total: Decimal = Field(default=Decimal("0.00"))
    payment_schedule: Optional[PaymentSchedule] = None
    validity_date: Optional[date] = None
    governance_alerts: List[str] = Field(default_factory=list)

    @field_validator("consultant_email")
    @classmethod
    def validate_corporate_email(cls, v: str) -> str:
        """Valida que o e-mail do consultor pertence ao domínio oficial da ARI Consulting."""
        if not v.lower().endswith("@ariconsulting.com.br"):
            raise ValueError(f"E-mail do consultor ({v}) deve pertencer ao domínio corporativo @ariconsulting.com.br")
        return v.lower()

    @model_validator(mode="after")
    def validate_business_rules(self) -> "CommercialProposalProposal":
        """
        Executa todas as regras de negócio invioláveis da ARI Consulting.
        """
        # 1. Checagem de serviços duplicados
        codes = [s.service_code for s in self.services]
        if len(codes) != len(set(codes)):
            raise ValueError("Não é permitido incluir serviços duplicados na mesma proposta.")

        # 2. Cálculo do Total Bruto
        self.gross_total = sum(s.investment for s in self.services)

        # 3. Regra Inviolável de Desconto Comercial
        # Desconto de 10% a 15% permitido EXCLUSIVAMENTE para 2 ou mais serviços combinados
        num_services = len(self.services)
        if self.discount_percentage > Decimal("0.00"):
            if num_services < 2:
                raise ValueError(
                    f"Política de Desconto Violada: Desconto de {self.discount_percentage}% foi solicitado, "
                    f"mas a proposta contém apenas {num_services} serviço. Descontos comerciais são restritos a pacotes combinados de 2 ou mais serviços."
                )
            if self.discount_percentage < Decimal("10.00") or self.discount_percentage > Decimal("15.00"):
                raise ValueError(
                    f"Faixa de Desconto Inválida: Desconto de {self.discount_percentage}% está fora da alçada permitida. "
                    f"A política comercial autoriza estritamente entre 10% e 15% para serviços combinados."
                )

        # 4. Cálculo do Desconto e Total Líquido
        discount_factor = self.discount_percentage / Decimal("100.00")
        self.discount_amount = (self.gross_total * discount_factor).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.net_total = self.gross_total - self.discount_amount

        # 5. Validação de Teto Orçamentário (Budget Ceiling)
        if self.budget_ceiling is not None:
            if self.net_total > self.budget_ceiling:
                teto_fmt = format_currency_brl(self.budget_ceiling)
                liq_fmt = format_currency_brl(self.net_total)
                diff_fmt = format_currency_brl(self.net_total - self.budget_ceiling)
                raise ValueError(
                    f"Estouro de Teto Orçamentário: O investimento líquido da proposta ({liq_fmt}) "
                    f"ultrapassa o orçamento máximo aprovado pelo cliente ({teto_fmt}) por {diff_fmt}. "
                    f"Ajuste os valores dos serviços ou reduza o escopo para respeitar a condicionante do cliente."
                )

        # 6. Cálculo das Condições Fixas de Pagamento (30% / 40% / 30%)
        # 30% na Assinatura, 40% na conclusão do Build, 30% no Go-Live
        assinatura_val = (self.net_total * Decimal("0.30")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        build_val = (self.net_total * Decimal("0.40")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        # O último marco absorve qualquer resíduo de centavos
        golive_val = self.net_total - assinatura_val - build_val

        self.payment_schedule = PaymentSchedule(
            assinatura_amount=assinatura_val,
            build_amount=build_val,
            golive_amount=golive_val,
            total_amount=self.net_total
        )

        # 7. Validade da Proposta: Fixa em 30 dias corridos
        self.validity_date = self.emission_date + timedelta(days=30)

        # 8. Alçadas e Governança de Risco
        self.governance_alerts = []
        if self.net_total > Decimal("200000.00"):
            self.governance_alerts.append(
                "ALÇADA > R$ 200.000: Obrigatório incluir Estudo de Caso de Referência (solicitar ao Marketing) "
                "e obter aprovação formal do Gerente de Contas antes do envio ao cliente."
            )
        else:
            self.governance_alerts.append(
                "REVISÃO DE ALÇADA: A Seção de Investimento deve ser revisada pelo Gerente de Contas antes do envio."
            )

        return self


# ===========================================================================
# 3. Funções Utilitárias e Relatório de Validação
# ===========================================================================

def generate_deal_validation_report(proposal: CommercialProposalProposal) -> str:
    """Gera um relatório executivo de validação pronto para exibição."""
    lines = []
    lines.append("=" * 72)
    lines.append("RELATÓRIO DE VALIDAÇÃO DE PROPOSTA COMERCIAL — ARI DEAL")
    lines.append("=" * 72)
    lines.append(f"Proposta Nº:       {proposal.proposal_number}")
    lines.append(f"Cliente:           {proposal.client_name}")
    if proposal.cnpj:
        lines.append(f"CNPJ:              {proposal.cnpj}")
    lines.append(f"Setor:             {proposal.sector}")
    lines.append(f"Consultor:         {proposal.consultant_name} <{proposal.consultant_email}>")
    lines.append(f"Data de Emissão:   {proposal.emission_date.strftime('%d/%m/%Y')}")
    lines.append(f"Validade da Oferta:{proposal.validity_date.strftime('%d/%m/%Y')} (30 dias corridos)")
    lines.append("-" * 72)
    lines.append("SERVIÇOS OFICIAIS SELECIONADOS:")
    for idx, item in enumerate(proposal.services, 1):
        cat = OFFICIAL_CATALOG_2026[item.service_code]
        lines.append(f"  {idx}. [{item.service_code.value}] {cat.name}")
        lines.append(f"     Investimento:   {format_currency_brl(item.investment)} (Faixa: {format_currency_brl(cat.min_investment)} - {format_currency_brl(cat.max_investment)})")
        lines.append(f"     Prazo Típico:   {cat.typical_duration_min_days} a {cat.typical_duration_max_days} dias corridos")
        if item.custom_scope_notes:
            lines.append(f"     Notas:          {item.custom_scope_notes}")
    lines.append("-" * 72)
    lines.append("RESUMO FINANCEIRO:")
    lines.append(f"  Total Bruto:       {format_currency_brl(proposal.gross_total)}")
    if proposal.discount_percentage > Decimal("0.00"):
        lines.append(f"  Desconto Aplicado: {proposal.discount_percentage:.1f}% ({format_currency_brl(proposal.discount_amount)}) [Pacote Combinado de {len(proposal.services)} Serviços]")
    else:
        lines.append("  Desconto Aplicado: 0.0% (Nenhum desconto aplicado)")
    lines.append(f"  Total Líquido:     {format_currency_brl(proposal.net_total)}")

    if proposal.budget_ceiling:
        saldo = proposal.budget_ceiling - proposal.net_total
        lines.append(f"  Teto Orçamentário: {format_currency_brl(proposal.budget_ceiling)}")
        lines.append(f"  Margem / Saldo:    {format_currency_brl(saldo)} [CONFORME COM TETO DO CLIENTE (OK)]")

    lines.append("-" * 72)
    lines.append("CRONOGRAMA DE PAGAMENTO OBRIGATÓRIO (30% / 40% / 30%):")
    sched = proposal.payment_schedule
    lines.append(f"  1. Assinatura do Contrato (30%):   {format_currency_brl(sched.assinatura_amount)}")
    lines.append(f"  2. Conclusão da Fase Build (40%): {format_currency_brl(sched.build_amount)}")
    lines.append(f"  3. Homologação e Go-Live (30%):    {format_currency_brl(sched.golive_amount)}")
    lines.append(f"  TOTAL CONTRATUAL:                 {format_currency_brl(sched.total_amount)}")
    lines.append("-" * 72)
    lines.append("GOVERNANÇA & ALERTAS DE ALÇADA:")
    for alert in proposal.governance_alerts:
        lines.append(f"  [!] {alert}")
    lines.append("=" * 72)
    return "\n".join(lines)


# ===========================================================================
# 4. Caso de Teste Canônico: Briefing Vetria Embalagens Industriais S.A.
# ===========================================================================

def build_vetria_sample_proposal() -> CommercialProposalProposal:
    """
    Constrói e valida a proposta para a Vetria Embalagens Industriais S.A.
    baseada nas regras extraídas do briefing de cliente:
    - Escopo Core: Oracle Financials (GL, AP, Cash) + Integração OIC
    - Teto Orçamentário: R$ 350.000,00
    - Desconto de pacote combinado (2 serviços): 10%
    """
    return CommercialProposalProposal(
        client_name="Vetria Embalagens Industriais S.A.",
        cnpj="78.901.234/0001-56",
        sector="Indústria — Embalagens plásticas e flexíveis",
        budget_ceiling=Decimal("350000.00"),
        proposal_number="048/2026",
        consultant_name="Carlos Eduardo Silveira",
        consultant_email="carlos.silveira@ariconsulting.com.br",
        discount_percentage=Decimal("10.00"),
        services=[
            SelectedServiceItem(
                service_code=ServiceCode.SRV_02_ERP,
                investment=Decimal("210000.00"),
                custom_scope_notes="Oracle Fusion Financials: GL (plano único), AP (aprovação centralizada) e Cash Management."
            ),
            SelectedServiceItem(
                service_code=ServiceCode.SRV_05_INTEGRACAO,
                investment=Decimal("80000.00"),
                custom_scope_notes="Oracle Integration Cloud (OIC) conectando Protheus, Sankhya e sistema legado em Delphi."
            )
        ]
    )


def build_vetria_proposal_082() -> CommercialProposalProposal:
    """
    Constrói e valida a Proposta Comercial oficial nº 082/2026 para a Vetria Embalagens Industriais S.A.:
    - Cliente: Vetria Embalagens Industriais S.A. | Contato: Roberto Alencar (CFO)
    - Escopo: Implantação de Oracle Fusion Cloud Financials e Integração de Sistemas Legados
    - Valor Bruto: R$ 345.000,00
    - Desconto de Pacote Comercial (10%): R$ 34.500,00
    - Valor Líquido: R$ 310.500,00 (dentro do teto de R$ 350.000,00)
    - Condição de Pagamento: 30% Assinatura (R$ 93.150,00) / 40% Build (R$ 124.200,00) / 30% Go-Live (R$ 93.150,00)
    """
    return CommercialProposalProposal(
        client_name="Vetria Embalagens Industriais S.A.",
        cnpj="78.901.234/0001-56",
        sector="Indústria — Embalagens plásticas e flexíveis",
        budget_ceiling=Decimal("350000.00"),
        proposal_number="082/2026",
        consultant_name="Carlos Eduardo Silveira",
        consultant_email="carlos.silveira@ariconsulting.com.br",
        discount_percentage=Decimal("10.00"),
        services=[
            SelectedServiceItem(
                service_code=ServiceCode.SRV_02_ERP,
                investment=Decimal("255000.00"),
                custom_scope_notes="Oracle Fusion Financials: GL (plano de contas unificado multi-planta), AP (fluxo centralizado), Cash Management (tesouraria automatizada)."
            ),
            SelectedServiceItem(
                service_code=ServiceCode.SRV_05_INTEGRACAO,
                investment=Decimal("90000.00"),
                custom_scope_notes="Oracle Integration Cloud (OIC) conectando Protheus (matriz), Sankhya e sistema Delphi legado durante a transição operacional."
            )
        ]
    )


if __name__ == "__main__":
    # Teste de execução controlada do validador determinístico
    vetria_deal = build_vetria_proposal_082()
    print(generate_deal_validation_report(vetria_deal))
