from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.veiculo import VeiculoModel
from app.Schema.veiculo import VeiculoSchema

veiculo = APIRouter()


@veiculo.post("/")
async def criar_veiculo(dados: VeiculoSchema, db: Session = Depends(get_db)):
    novo_veiculo = VeiculoModel(**dados.model_dump())

    db.add(novo_veiculo)
    db.commit()
    db.refresh(novo_veiculo)

    return novo_veiculo


@veiculo.get("/")
async def listar_veiculos(db: Session = Depends(get_db)):
    return db.query(VeiculoModel).all()


@veiculo.get("/{id}")
async def buscar_veiculo(id: int, db: Session = Depends(get_db)):
    veiculo_encontrado = db.query(VeiculoModel).filter(
        VeiculoModel.id_veiculo == id
    ).first()

    return veiculo_encontrado


@veiculo.put("/{id}")
async def atualizar_veiculo(id: int, dados: VeiculoSchema, db: Session = Depends(get_db)):
    veiculo_existente = db.query(VeiculoModel).filter(
        VeiculoModel.id_veiculo == id
    ).first()

    for campo, valor in dados.model_dump().items():
        setattr(veiculo_existente, campo, valor)

    db.commit()
    return veiculo_existente


@veiculo.delete("/{id}")
async def deletar_veiculo(id: int, db: Session = Depends(get_db)):
    veiculo_existente = db.query(VeiculoModel).filter(
        VeiculoModel.id_veiculo == id
    ).first()

    db.delete(veiculo_existente)
    db.commit()
    return {"msg": "Veículo deletado"}

 