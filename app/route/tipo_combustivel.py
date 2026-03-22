from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.tipo_combustivel import TipoCombustivelModel
from app.Schema.tipo_combustivel import TipoCombustivelSchema

tipo_combustivel = APIRouter(prefix="/tipo_combustivel", tags=["TipoCombustivel"])

@tipo_combustivel.post("/")
def criar_tipo_combustivel(dados: TipoCombustivelSchema, db: Session = Depends(get_db)):
    novo_tipo = TipoCombustivelModel(**dados.model_dump())
    db.add(novo_tipo)
    db.commit()
    db.refresh(novo_tipo)
    return novo_tipo

@tipo_combustivel.get("/")
def listar_tipos(db: Session = Depends(get_db)):
    return db.query(TipoCombustivelModel).all()

@tipo_combustivel.get("/{id}")
def buscar_tipo(id: int, db: Session = Depends(get_db)):
    tipo_encontrado = db.query(TipoCombustivelModel).filter(
        TipoCombustivelModel.id_combustivel == id
    ).first()
    return tipo_encontrado

@tipo_combustivel.put("/{id}")
def atualizar_tipo(id: int, dados: TipoCombustivelSchema, db: Session = Depends(get_db)):
    tipo_existente = db.query(TipoCombustivelModel).filter(
        TipoCombustivelModel.id_combustivel == id
    ).first()

    for campo, valor in dados.model_dump().items():
        setattr(tipo_existente, campo, valor)

    db.commit()
    return tipo_existente

@tipo_combustivel.delete("/{id}")
def deletar_tipo(id: int, db: Session = Depends(get_db)):
    tipo_existente = db.query(TipoCombustivelModel).filter(
        TipoCombustivelModel.id_combustivel == id
    ).first()

    db.delete(tipo_existente)
    db.commit()
    return {"msg": "Tipo deletado"}