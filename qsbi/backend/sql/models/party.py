# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Party(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)

    schedules: relationship = relationship("Scheduled", back_populates="party")
    transacts: relationship = relationship("Transact", back_populates="party")
