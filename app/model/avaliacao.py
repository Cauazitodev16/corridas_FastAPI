from sqlalchemy import Column, BigInteger, Integer, DateTime
from app.database import Base

class AvaliacaoModel(Base):
    __tablename__ = "avaliacao"

    id_avaliacao = Column(BigInteger, primary_key=True, autoincrement=True)
    nota_passageiro = Column(Integer)
    nota_motorista = Column(Integer)
    datahora_limite = Column(DateTime)