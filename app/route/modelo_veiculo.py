from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.modelo_veiculo import ModeloVeiculoModel
from app.Schema.modelo_veiculo import ModeloVeiculoSchema

modelo_veiculo = APIRouter()

@modelo_veiculo.post("/")
async def criar_modelo(dados: ModeloVeiculoSchema, db: Session = Depends(get_db)):
    novo_modelo = ModeloVeiculoModel(**dados.model_dump())
    db.add(novo_modelo)
    db.commit()
    db.refresh(novo_modelo)
    return novo_modelo

@modelo_veiculo.get("/")
async def listar_modelos(db: Session = Depends(get_db)):
    return db.query(ModeloVeiculoModel).all()

@modelo_veiculo.get("/{id}")
async def buscar_modelo(id: int, db: Session = Depends(get_db)):
    modelo_encontrado = db.query(ModeloVeiculoModel).filter(
        ModeloVeiculoModel.id_modelo == id
    ).first()
    return modelo_encontrado

@modelo_veiculo.put("/{id}")
async def atualizar_modelo(id: int, dados: ModeloVeiculoSchema, db: Session = Depends(get_db)):
    modelo_existente = db.query(ModeloVeiculoModel).filter(
        ModeloVeiculoModel.id_modelo == id
    ).first()

    for campo, valor in dados.model_dump().items():
        setattr(modelo_existente, campo, valor)

    db.commit()
    return modelo_existente

@modelo_veiculo.delete("/{id}")
async def deletar_modelo(id: int, db: Session = Depends(get_db)):
    modelo_existente = db.query(ModeloVeiculoModel).filter(
        ModeloVeiculoModel.id_modelo == id
    ).first()

    db.delete(modelo_existente)
    db.commit()
    return {"msg": "Modelo deletado"}