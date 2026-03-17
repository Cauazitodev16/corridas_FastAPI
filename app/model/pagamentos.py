from sqlalchemy import Column, BigInteger, Numeric, SmallInteger, DateTime, ForeignKey
from app.database import Base

class PagamentoModel(Base):
    __tablename__ = "pagamentos"

    id_pagamento = Column(BigInteger, primary_key=True, autoincrement=True)
    id_corrida = Column(BigInteger, ForeignKey("corrida.id_corrida"), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    id_metodo_pagamento = Column(SmallInteger, ForeignKey("metodos_pagamentos.id_metodo_pagamento"), nullable=False)
    datahora_transacao = Column(DateTime, nullable=False)