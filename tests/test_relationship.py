from sqlalchemy import select

import qsbi.backend.sql.models as models


def test_relationship_one_to_one(get_test_session) -> None:
    with get_test_session as sess:
        acc = sess.execute(select(models.Account).where(models.Account.id == 2)).scalars().first()
        bnk = sess.execute(select(models.Bank).where(models.Bank.id == 2)).scalars().first()
        acc_bnk = acc.bank
        assert acc_bnk is bnk


def test_relationship_one_to_many(get_test_session) -> None:
    with get_test_session as sess:
        acc = sess.execute(select(models.Account).where(models.Account.id == 1)).scalars().first()
        trscs = sess.execute(select(models.Transact).where(models.Transact.account_id == 1)).scalars()
        for tr in trscs:
            assert tr.account is acc


def test_relationship_many_to_one(get_test_session) -> None:
    with get_test_session as sess:
        acc = sess.execute(select(models.Account).where(models.Account.id == 1)).scalars().first()
        trscs = sess.execute(select(models.Transact).where(models.Transact.account_id == 1)).scalars()
        acctr = acc.transacts
        for tr in acctr:
            assert tr in trscs
        for tr in trscs:
            assert tr in acctr
