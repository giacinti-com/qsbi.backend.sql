# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Account(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(String)
    bank_id = Column(Integer, ForeignKey("bank.id"))
    bank_branch = Column(String)
    bank_account = Column(String)
    bank_account_key = Column(String)
    bank_IBAN = Column(String)
    currency_id = Column(Integer, ForeignKey("currency.id"))
    open_date = Column(DateTime)
    close_date = Column(DateTime)
    type_id = Column(Integer, ForeignKey("accounttype.id"))
    initial_balance = Column(Float)
    mini_balance_wanted = Column(Float)
    mini_balance_auth = Column(Float)
    holder_name = Column(String)
    holder_address = Column(String)
    notes = Column(String)

    bank: relationship = relationship("Bank", back_populates="accounts")
    currency: relationship = relationship("Currency", back_populates="accounts")
    type: relationship = relationship("AccountType", back_populates="accounts")

    reconciles: relationship = relationship("Reconcile", back_populates="account")
    schedules: relationship = relationship("Scheduled", back_populates="account")
    transacts: relationship = relationship("Transact", back_populates="account")
    payments: relationship = relationship("Payment", back_populates="account")
