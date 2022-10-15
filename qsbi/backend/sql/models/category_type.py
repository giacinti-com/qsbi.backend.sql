# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class CategoryType(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(String)

    categories: relationship = relationship("Category", back_populates="type")
