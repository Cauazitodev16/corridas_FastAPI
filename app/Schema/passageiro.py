from pydantic import BaseModel
from typing import Optional

class PassageiroSchema(BaseModel):
    id_passageiro: Optional[int] = None
    id_usuario: int

    class Config:
        from_attributes = True