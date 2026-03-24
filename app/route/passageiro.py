from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.passageiro import PassageiroModel
from app.Schema.passageiro import PassageiroSchema

passageiro = APIRouter()


@passageiro.post("/")
def criar_passageiro(dados: PassageiroSchema, db: Session = Depends(get_db)):
    novo_passageiro = PassageiroModel(**dados.model_dump())

    db.add(novo_passageiro)
    db.commit()
    db.refresh(novo_passageiro)

    return novo_passageiro


@passageiro.get("/")
def listar_passageiros(db: Session = Depends(get_db)):
    return db.query(PassageiroModel).all()