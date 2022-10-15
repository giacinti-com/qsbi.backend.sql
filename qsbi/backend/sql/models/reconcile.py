# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Reconcile(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(String)
    account_id = Column(Integer, ForeignKey("account.id"))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    start_balance = Column(Float)
    end_balance = Column(Float)
    log_id = Column(Integer, ForeignKey("auditlog.id"))

    account: relationship = relationship("Account", back_populates="reconciles")
    log: relationship = relationship("AuditLog", back_populates="reconciles")
