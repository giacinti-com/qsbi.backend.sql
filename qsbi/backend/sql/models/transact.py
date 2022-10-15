# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from .base import Base


class Transact(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("account.id"))
    transaction_date = Column(DateTime)
    value_date = Column(DateTime)
    party_id = Column(Integer, ForeignKey("party.id"))
    category_id = Column(Integer, ForeignKey("category.id"))
    sub_category_id = Column(Integer, ForeignKey("subcategory.id"))
    notes = Column(String)
    amount = Column(Float)
    currency_id = Column(Integer, ForeignKey("currency.id"))
    exchange_rate = Column(Float)
    exchange_fees = Column(Float)
    payment_id = Column(Integer, ForeignKey("payment.id"))
    master_id = Column(Integer, ForeignKey("transact.id"))
    reconcile_id = Column(Integer, ForeignKey("reconcile.id"))
    log_id = Column(Integer, ForeignKey("auditlog.id"))

    account: relationship = relationship("Account", back_populates="transacts")
    party: relationship = relationship("Party", back_populates="transacts")
    category: relationship = relationship("Category", back_populates="transacts")
    sub_category: relationship = relationship("SubCategory", back_populates="transacts")
    currency: relationship = relationship("Currency")
    payment: relationship = relationship("Payment")
    #    master = relationship("Transact")
    reconcile: relationship = relationship("Reconcile")
    log: relationship = relationship("AuditLog", back_populates="transacts")

    subs: relationship = relationship("Transact", backref=backref("master", remote_side=[id]))
