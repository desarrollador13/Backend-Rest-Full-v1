from sqlalchemy import create_engine, MetaData, Table, Text, Integer, String, Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UsuariosAppModel(Base):
	
	__tablename__ = "UsuariosApp"
	Id = Column(Integer, primary_key=True, autoincrement=True)
	NombreApp = Column(Text(), nullable=False, unique=True)
	Correo = Column(Text(), unique=True)
	IdRoles = Column(Integer, nullable=False)
	Clave = Column(Text(), nullable=False)