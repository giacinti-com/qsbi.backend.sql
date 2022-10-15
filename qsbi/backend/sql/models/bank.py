# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Bank(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(Integer)
    bic = Column(String)
    address = Column(String)
    tel = Column(String)
    mail = Column(String)
    web = Column(String)
    contact_name = Column(String)
    contact_fax = Column(String)
    contact_tel = Column(String)
    contact_mail = Column(String)
    notes = Column(String)

    accounts: relationship = relationship("Account", back_populates="bank")
