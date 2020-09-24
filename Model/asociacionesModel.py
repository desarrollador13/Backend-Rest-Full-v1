from sqlalchemy import create_engine, MetaData, Table, Text, Integer, String, Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AsociacionesModel(Base):

	__tablename__ = "Asociaciones"
	Id = Column(Integer, primary_key=True, autoincrement=True)
	NomAsociacion = Column(Text(), nullable=False, unique=True)
	Tipo = Column(Text(), nullable=False)
	NIT = Column(Text(), nullable=False, unique=True)
	Direcciones = Column(Text(), nullable=False)
	Telefonos = Column(Text(), nullable=False)