from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioSchema(BaseModel):
    id_usuario: Optional[int] = None
    nome: str
    cpf: str
    data_nascimento: date
    idade: int
    senha: str
    email: str
    usuario: str

    class Config:
        from_attributes = True