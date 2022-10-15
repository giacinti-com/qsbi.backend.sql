import filecmp
import json

from sqlalchemy import select

import qsbi.backend.sql.models as models

MODEL_ALL = (
    "Account",
    "AccountType",
    "AuditLog",
    "Bank",
    "Category",
    "CategoryType",
    "Currency",
    "CurrencyLink",
    "Party",
    "Payment",
    "PaymentType",
    "Reconcile",
    "Scheduled",
    "SubCategory",
    "Transact",
    "User",
)


def test_all_models(get_test_session, example_json, tmp_path) -> None:
    output = tmp_path / "test.json"
    with open(output, "w") as file:
        with get_test_session as sess:
            for mod in MODEL_ALL:
                stmt = select(models.__dict__[mod])
                result = sess.execute(stmt)
                for acc in result.scalars():
                    print(json.dumps(acc.as_dict(), default=str), file=file)
    assert filecmp.cmp(example_json, output, False)
