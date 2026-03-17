from sqlalchemy import Column, BigInteger, Integer, DateTime, String, Numeric, Enum, ForeignKey
from app.database import Base

class CorridaModel(Base):
    __tablename__ = "corrida"

    id_corrida = Column(BigInteger, primary_key=True, autoincrement=True)
    
    # Chaves Estrangeiras (Foreign Keys)
    # Certifique-se que o nome antes do ponto (ex: 'passageiro') 
    # seja o __tablename__ definido nos outros arquivos.
    id_passageiro = Column(BigInteger, ForeignKey("passageiro.id_passageiro"), nullable=False)
    id_motorista = Column(BigInteger, ForeignKey("motorista.id_motorista"), nullable=True)
    id_servico = Column(Integer, ForeignKey("servico.id_servico"), nullable=False)
    id_avaliacao = Column(BigInteger, ForeignKey("avaliacao.id_avaliacao"), nullable=True)
    
    datahora_inicio = Column(DateTime, nullable=False)
    datahora_fim = Column(DateTime, nullable=True)
    local_partida = Column(String(100), nullable=False)
    local_destino = Column(String(100), nullable=False)
    valor_estimado = Column(Numeric(10, 2), nullable=False)
    
    # O Enum define as opções fixas para o status
    status = Column(
        Enum("Pendente", "Em andamento", "Concluída", "Cancelada", name="status_corrida"),
        default="Pendente",
        nullable=False
    )