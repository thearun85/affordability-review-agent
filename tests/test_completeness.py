from decimal import Decimal

from affordability.models import LoanApplication
from affordability.tools.completeness import check_completeness


def test_complete_application_is_marked_complete() -> None:
    application = LoanApplication(
        annual_income=Decimal("60000"),
        monthly_essential_expenditure=Decimal("1500"),
        existing_monthly_commitments=Decimal("300"),
        requested_loan_amount=Decimal("10000"),
        loan_term_months=36,
        annual_interest_rate=Decimal("6.5"),
        applicant_note="No additional information.",
    )

    result = check_completeness(application)

    assert result.is_complete is True
    assert result.missing_fields == ()
    assert result.invalid_fields == ()
