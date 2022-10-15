# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class SubCategory(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("category.id"), primary_key=True)
    name = Column(String)

    category: relationship = relationship("Category", back_populates="sub_categories")
    schedules: relationship = relationship("Scheduled", back_populates="sub_category")
    transacts: relationship = relationship("Transact", back_populates="sub_category")
