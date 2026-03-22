from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.corrida import CorridaModel
from app.Schema.corrida import CorridaSchema

corrida = APIRouter(prefix="/corrida", tags=["Corrida"])


@corrida.post("/")
async def criar_corrida(dados: CorridaSchema, db: Session = Depends(get_db)):
    nova_corrida = CorridaModel(**dados.model_dump())

    db.add(nova_corrida)
    db.commit()
    db.refresh(nova_corrida)

    return nova_corrida


@corrida.get("/")
async def listar_corridas(db: Session = Depends(get_db)):
    return db.query(CorridaModel).all()


@corrida.get("/{id}")
async def buscar_corrida(id: int, db: Session = Depends(get_db)):
    corrida_encontrada = db.query(CorridaModel).filter(
        CorridaModel.id_corrida == id
    ).first()

    return corrida_encontrada


@corrida.put("/{id}")
async def atualizar_corrida(id: int, dados: CorridaSchema, db: Session = Depends(get_db)):
    corrida_existente = db.query(CorridaModel).filter(
        CorridaModel.id_corrida == id
    ).first()

    for campo, valor in dados.model_dump().items():
        setattr(corrida_existente, campo, valor)

    db.commit()
    return corrida_existente


@corrida.delete("/{id}")
async def deletar_corrida(id: int, db: Session = Depends(get_db)):
    corrida_existente = db.query(CorridaModel).filter(
        CorridaModel.id_corrida == id
    ).first()

    db.delete(corrida_existente)
    db.commit()

    return {"msg": "Corrida deletada"}