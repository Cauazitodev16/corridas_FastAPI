from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.motorista import MotoristaModel
from app.Schema.motorista import MotoristaSchema

motorista = APIRouter(prefix="/motorista", tags=["Motorista"])


@motorista.post("/")
async def criar_motorista(dados: MotoristaSchema, db: Session = Depends(get_db)):
    novo_motorista = MotoristaModel(**dados.model_dump())

    db.add(novo_motorista)
    db.commit()
    db.refresh(novo_motorista)

    return novo_motorista


@motorista.get("/")
async def listar_motoristas(db: Session = Depends(get_db)):
    return db.query(MotoristaModel).all()


@motorista.get("/{id}")
async def buscar_motorista(id: int, db: Session = Depends(get_db)):
    motorista_encontrado = db.query(MotoristaModel).filter(
        MotoristaModel.id_motorista == id
    ).first()

    return motorista_encontrado


@motorista.put("/{id}")
async def atualizar_motorista(id: int, dados: MotoristaSchema, db: Session = Depends(get_db)):
    motorista_existente = db.query(MotoristaModel).filter(
        MotoristaModel.id_motorista == id
    ).first()

    for campo, valor in dados.model_dump().items():
        setattr(motorista_existente, campo, valor)

    db.commit()
    return motorista_existente


@motorista.delete("/{id}")
async def deletar_motorista(id: int, db: Session = Depends(get_db)):
    motorista_existente = db.query(MotoristaModel).filter(
        MotoristaModel.id_motorista == id
    ).first()

    db.delete(motorista_existente)
    db.commit()

    return {"msg": "Motorista deletado"}