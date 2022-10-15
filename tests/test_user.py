from sqlalchemy import select

import qsbi.backend.sql.models as models


def test_user_scopes(get_test_session) -> None:
    with get_test_session as sess:
        user: models.User = sess.execute(select(models.User).where(models.User.id == 1)).scalars().first()
        assert user.scopes == ["login", "read"]
        user.scopes = ["write", "create"]
        assert user.scopes_str == '["write", "create"]'
        sess.add(user)
        sess.commit()
        sess.refresh(user)
        assert user.scopes_str == '["write", "create"]'
