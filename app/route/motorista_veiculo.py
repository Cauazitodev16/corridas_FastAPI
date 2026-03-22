from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.motorista_veiculo import MotoristaVeiculoModel
from app.Schema.motorista_veiculo import MotoristaVeiculoSchema

motorista_veiculo = APIRouter(prefix="/motorista_veiculo", tags=["MotoristaVeiculo"])

@motorista_veiculo.post("/")
async def criar_relacao(dados: MotoristaVeiculoSchema, db: Session = Depends(get_db)):
    nova_relacao = MotoristaVeiculoModel(**dados.model_dump())
    db.add(nova_relacao)
    db.commit()
    return nova_relacao

@motorista_veiculo.get("/")
async def listar_relacoes(db: Session = Depends(get_db)):
    return db.query(MotoristaVeiculoModel).all()

@motorista_veiculo.delete("/")
async def deletar_relacao(id_motorista: int, id_veiculo: int, db: Session = Depends(get_db)):
    relacao_existente = db.query(MotoristaVeiculoModel).filter(
        MotoristaVeiculoModel.id_motorista == id_motorista,
        MotoristaVeiculoModel.id_veiculo == id_veiculo
    ).first()

    db.delete(relacao_existente)
    db.commit()
    return {"msg": "Relação deletada"}