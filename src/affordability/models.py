from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class LoanApplication:
    annual_income: Decimal | None
    monthly_essential_expenditure: Decimal | None
    existing_monthly_commitment: Decimal | None
    requested_loan_amount: Decimal | None
    loan_term_months: int | None
    annual_interest_rate: Decimal | None
    applicant_note: str

@dataclass(frozen=True)
class CompletenessResult:
    is_complete: bool
    missing_fields: tuple[str, ...]
    invalid_fields: tuple[str, ...]
