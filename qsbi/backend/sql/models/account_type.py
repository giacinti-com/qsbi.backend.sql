# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class AccountType(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(String)
    accounts: relationship = relationship("Account", back_populates="type")
