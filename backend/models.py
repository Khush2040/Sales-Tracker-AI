# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    month = Column(String)
    sales = Column(Integer)
    region = Column(String)
    product = Column(String)
