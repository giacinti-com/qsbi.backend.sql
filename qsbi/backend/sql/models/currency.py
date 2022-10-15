# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Currency(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nickname = Column(String)
    code = Column(String)

    accounts: relationship = relationship("Account", back_populates="currency")
    exchanges: relationship = relationship(
        "CurrencyLink", primaryjoin="or_(CurrencyLink.cur1_id==Currency.id," "CurrencyLink.cur2_id==Currency.id)"
    )
