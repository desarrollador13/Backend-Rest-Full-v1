from sqlalchemy import create_engine, MetaData, Table, Text, Integer, String, Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

Base = declarative_base()

class RolesModel(Base):
	__tablename__ = "Roles"

	Id = Column(Integer, primary_key=True, autoincrement=True)
	nombreRoll = Column(Text(), nullable=False, unique=True)