# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Payment(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(String)
    account_id = Column(Integer, ForeignKey("account.id"))
    current = Column(Integer)  # if not None, automatic numbering
    type_id = Column(Integer, ForeignKey("paymenttype.id"))

    account: relationship = relationship("Account", back_populates="payments")
    type: relationship = relationship("PaymentType", back_populates="payments")
