# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class PaymentType(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(String)

    payments: relationship = relationship("Payment", back_populates="type")
