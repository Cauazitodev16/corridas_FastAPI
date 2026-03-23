from sqlalchemy import Column, Integer, String, CHAR, Date, SmallInteger
from app.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255))
    cpf = Column(CHAR(11), unique=True)
    data_nascimento = Column(Date)
    idade = Column(SmallInteger)
    senha = Column(CHAR(64))
    email = Column(String(255), unique=True)  
    usuario = Column(String(50), unique=True)