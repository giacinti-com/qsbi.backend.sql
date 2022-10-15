# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Category(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type_id = Column(Integer, ForeignKey("categorytype.id"))

    type: relationship = relationship("CategoryType", back_populates="categories")

    sub_categories: relationship = relationship("SubCategory", back_populates="category")
    schedules: relationship = relationship("Scheduled", back_populates="category")
    transacts: relationship = relationship("Transact", back_populates="category")
