from sqlalchemy import Column, Integer, DateTime, String, Numeric, Enum, ForeignKey
from app.database import Base

class CorridaModel(Base):
    __tablename__ = "corrida"

    id_corrida = Column(Integer, primary_key=True, autoincrement=True)
    id_passageiro = Column(Integer, ForeignKey("passageiro.id_passageiro"), nullable=False)
    id_motorista = Column(Integer, ForeignKey("motorista.id_motorista"), nullable=True)
    id_servico = Column(Integer, ForeignKey("servico.id_servico"), nullable=False)
    id_avaliacao = Column(Integer, ForeignKey("avaliacao.id_avaliacao"), nullable=True)
    
    datahora_inicio = Column(DateTime, nullable=False)
    datahora_fim = Column(DateTime, nullable=True)
    local_partida = Column(String(100), nullable=False)
    local_destino = Column(String(100), nullable=False)
    valor_estimado = Column(Numeric(10, 2), nullable=False)
    
    status = Column(
        Enum("Pendente", "Em andamento", "Concluída", "Cancelada", name="status_corrida"),
        default="Pendente",
        nullable=False
    )