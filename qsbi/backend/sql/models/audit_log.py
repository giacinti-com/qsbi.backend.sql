# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class AuditLog(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    date = Column(DateTime)
    notes = Column(String)

    user: relationship = relationship("User", back_populates="logs")

    reconciles: relationship = relationship("Reconcile", back_populates="log")
    currency_links: relationship = relationship("CurrencyLink", back_populates="log")
    transacts: relationship = relationship("Transact", back_populates="log")
    schedules: relationship = relationship("Scheduled", back_populates="log")
