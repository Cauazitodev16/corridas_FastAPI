from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.metodo_pagamento import MetodoPagamentoModel
from app.Schema.metodo_pagamento import MetodoPagamentoSchema

metodo_pagamento = APIRouter(prefix="/metodo_pagamento", tags=["MetodoPagamento"])

@metodo_pagamento.post("/")
async def criar_metodo(dados: MetodoPagamentoSchema, db: Session = Depends(get_db)):
    novo_metodo = MetodoPagamentoModel(**dados.model_dump())
    db.add(novo_metodo)
    db.commit()
    db.refresh(novo_metodo)
    return novo_metodo

@metodo_pagamento.get("/")
async def listar_metodos(db: Session = Depends(get_db)):
    return db.query(MetodoPagamentoModel).all()

@metodo_pagamento.get("/{id}")
async def buscar_metodo(id: int, db: Session = Depends(get_db)):
    metodo_encontrado = db.query(MetodoPagamentoModel).filter(
        MetodoPagamentoModel.id_metodo_pagamento == id
    ).first()
    return metodo_encontrado

@metodo_pagamento.put("/{id}")
async def atualizar_metodo(id: int, dados: MetodoPagamentoSchema, db: Session = Depends(get_db)):
    metodo_existente = db.query(MetodoPagamentoModel).filter(
        MetodoPagamentoModel.id_metodo_pagamento == id
    ).first()

    for campo, valor in dados.model_dump().items():
        setattr(metodo_existente, campo, valor)

    db.commit()
    return metodo_existente

@metodo_pagamento.delete("/{id}")
async def deletar_metodo(id: int, db: Session = Depends(get_db)):
    metodo_existente = db.query(MetodoPagamentoModel).filter(
        MetodoPagamentoModel.id_metodo_pagamento == id
    ).first()

    db.delete(metodo_existente)
    db.commit()
    return {"msg": "Método deletado"}