from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class MotoristaModel(Base):
    __tablename__ = "motorista"

    id_motorista = Column(Integer, primary_key=True, autoincrement=True) 
    cpf = Column(String(11), unique=True)
    data_nascimento = Column(Date)