from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class CorridaSchema(BaseModel):
    id_corrida: Optional[int] = None
    id_passageiro: int
    id_motorista: int
    id_servico: int
    datahora_inicio: datetime
    local_partida: str
    local_destino: str
    valor_estimado: Decimal
    status: str

    class Config:
         from_attributes = True