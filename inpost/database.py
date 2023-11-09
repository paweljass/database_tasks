"""
Inpost recruitment task by Paweł Jasińśki 
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "product"
    model = Column(String, primary_key=True)
    maker = Column(String)
    type = Column(String)


class PC(Base):
    __tablename__ = "pc"
    code = Column(Integer, primary_key=True)
    model = Column(String, ForeignKey("product.model"), unique=True)
    speed = Column(Integer)
    ram = Column(Integer)
    hd = Column(Integer)
    cd = Column(String)
    price = Column(Integer)


class Laptop(Base):
    __tablename__ = "laptop"
    code = Column(Integer, primary_key=True)
    model = Column(String, ForeignKey("product.model"), unique=True)
    speed = Column(Integer)
    ram = Column(Integer)
    hd = Column(Integer)
    screen = Column(Integer)
    price = Column(Integer)


class Printer(Base):
    __tablename__ = "printer"
    code = Column(Integer, primary_key=True)
    model = Column(String, ForeignKey("product.model"), unique=True)
    color = Column(String)
    type = Column(String)
    price = Column(Integer)


engine = create_engine("sqlite:///products.db")
Base.metadata.create_all(engine)
