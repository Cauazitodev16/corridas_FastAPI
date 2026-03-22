from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.avaliacao import AvaliacaoModel
from app.Schema.avaliacao import AvaliacaoSchema

avaliacao = APIRouter(prefix="/avaliacao", tags=["Avaliacao"])

@avaliacao.post("/")
async def criar_avaliacao(dados: AvaliacaoSchema, db: Session = Depends(get_db)):
    nova_avaliacao = AvaliacaoModel(**dados.model_dump())
    db.add(nova_avaliacao)
    db.commit()
    db.refresh(nova_avaliacao)
    return nova_avaliacao

@avaliacao.get("/")
async def listar_avaliacoes(db: Session = Depends(get_db)):
    return db.query(AvaliacaoModel).all()

@avaliacao.get("/{id}")
async def buscar_avaliacao(id: int, db: Session = Depends(get_db)):
    avaliacao_encontrada = db.query(AvaliacaoModel).filter(
        AvaliacaoModel.id_avaliacao == id
    ).first()
    return avaliacao_encontrada

@avaliacao.put("/{id}")
async def atualizar_avaliacao(id: int, dados: AvaliacaoSchema, db: Session = Depends(get_db)):
    avaliacao_existente = db.query(AvaliacaoModel).filter(
        AvaliacaoModel.id_avaliacao == id
    ).first()

    for campo, valor in dados.model_dump().items():
        setattr(avaliacao_existente, campo, valor)

    db.commit()
    return avaliacao_existente

@avaliacao.delete("/{id}")
async def deletar_avaliacao(id: int, db: Session = Depends(get_db)):
    avaliacao_existente = db.query(AvaliacaoModel).filter(
        AvaliacaoModel.id_avaliacao == id
    ).first()

    db.delete(avaliacao_existente)
    db.commit()
    return {"msg": "Avaliação deletada"}