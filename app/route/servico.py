from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.servico import ServicoModel
from app.Schema.servico import ServicoSchema

servico = APIRouter(prefix="/servico", tags=["Servico"])

@servico.post("/")
async def criar_servico(dados: ServicoSchema, db: Session = Depends(get_db)):
    novo_servico = ServicoModel(**dados.model_dump())
    db.add(novo_servico)
    db.commit()
    db.refresh(novo_servico)
    return novo_servico

@servico.get("/")
async def listar_servicos(db: Session = Depends(get_db)):
    return db.query(ServicoModel).all()

@servico.get("/{id}")
async def buscar_servico(id: int, db: Session = Depends(get_db)):
    servico_encontrado = db.query(ServicoModel).filter(
        ServicoModel.id_servico == id
    ).first()
    return servico_encontrado

@servico.put("/{id}")
async def atualizar_servico(id: int, dados: ServicoSchema, db: Session = Depends(get_db)):
    servico_existente = db.query(ServicoModel).filter(
        ServicoModel.id_servico == id
    ).first()

    for campo, valor in dados.model_dump().items():
        setattr(servico_existente, campo, valor)

    db.commit()
    return servico_existente

@servico.delete("/{id}")
async def deletar_servico(id: int, db: Session = Depends(get_db)):
    servico_existente = db.query(ServicoModel).filter(
        ServicoModel.id_servico == id
    ).first()

    db.delete(servico_existente)
    db.commit()
    return {"msg": "Serviço deletado"}