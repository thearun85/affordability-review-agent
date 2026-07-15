from affordability.models import CompletenessResult, LoanApplication


def check_completeness(application: LoanApplication) -> CompletenessResult:
    return CompletenessResult(
        is_complete=True,
        missing_fields=(),
        invalid_fields=(),
    )
