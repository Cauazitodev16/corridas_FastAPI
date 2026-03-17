from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class TipoCombustivelSchema(BaseModel):
    id_combustivel: Optional[int] = None
    descricao: str
    fator_carbono: Decimal

    class Config:
        from_attributes = True