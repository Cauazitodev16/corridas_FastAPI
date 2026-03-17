from sqlalchemy import Column, BigInteger, Text, String, CHAR, Date, SmallInteger
from app.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuario"

    id_usuario = Column(BigInteger, primary_key=True, autoincrement=True)
    nome = Column(Text)
    cpf = Column(CHAR(11), unique=True)
    data_nascimento = Column(Date)
    idade = Column(SmallInteger)
    senha = Column(CHAR(64))
    email = Column(Text, unique=True)
    usuario = Column(String(50), unique=True)