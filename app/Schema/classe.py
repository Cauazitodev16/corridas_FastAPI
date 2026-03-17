from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class ClasseSchema(BaseModel):
    id_classe: Optional[int] = None
    nome_classe: str
    fator_preco: Decimal

    class Config:
        from_attributes = True