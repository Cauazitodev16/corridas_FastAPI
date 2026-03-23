from sqlalchemy import Column, Integer, Numeric, ForeignKey
from app.database import Base

class PassageiroModel(Base):
    __tablename__ = "passageiro"

    id_passageiro = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))
    media_avaliacao = Column(Numeric(3, 2))