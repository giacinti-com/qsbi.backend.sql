# coding: utf-8
import json
from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    login = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    password = Column(String)
    active = Column(Integer)
    scopes_str = Column(String)
    notes = Column(String)

    @property
    def scopes(self) -> List:
        lst: List = []
        if self.scopes_str:
            lst = json.loads(str(self.scopes_str))
        return lst

    @scopes.setter
    def scopes(self, lst) -> None:
        setattr(self, "scopes_str", json.dumps(lst))

    logs: relationship = relationship("AuditLog", back_populates="user")
