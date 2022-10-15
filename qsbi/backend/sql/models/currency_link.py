# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import Base


class CurrencyLink(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    cur1_id = Column(Integer, ForeignKey("currency.id"))
    cur2_id = Column(Integer, ForeignKey("currency.id"))
    rate = Column(Float)
    date = Column(DateTime)
    log_id = Column(Integer, ForeignKey("auditlog.id"))

    cur1: relationship = relationship("Currency", foreign_keys=[cur1_id], back_populates="exchanges")
    cur2: relationship = relationship("Currency", foreign_keys=[cur2_id], back_populates="exchanges")
    log: relationship = relationship("AuditLog", back_populates="currency_links")
