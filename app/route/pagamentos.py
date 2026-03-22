from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.pagamentos import PagamentoModel
from app.Schema.pagamentos import PagamentoSchema

pagamento = APIRouter(prefix="/pagamento", tags=["Pagamento"])


@pagamento.post("/")
async def criar_pagamento(dados: PagamentoSchema, db: Session = Depends(get_db)):
    novo_pagamento = PagamentoModel(**dados.model_dump())

    db.add(novo_pagamento)
    db.commit()
    db.refresh(novo_pagamento)

    return novo_pagamento


@pagamento.get("/")
async def listar_pagamentos(db: Session = Depends(get_db)):
    return db.query(PagamentoModel).all()


@pagamento.get("/{id}")
async def buscar_pagamento(id: int, db: Session = Depends(get_db)):
    pagamento_encontrado = db.query(PagamentoModel).filter(
        PagamentoModel.id_pagamento == id
    ).first()

    return pagamento_encontrado


@pagamento.put("/{id}")
async def atualizar_pagamento(id: int, dados: PagamentoSchema, db: Session = Depends(get_db)):
    pagamento_existente = db.query(PagamentoModel).filter(
        PagamentoModel.id_pagamento == id
    ).first()

    for campo, valor in dados.model_dump().items():
        setattr(pagamento_existente, campo, valor)

    db.commit()
    return pagamento_existente


@pagamento.delete("/{id}")
async def deletar_pagamento(id: int, db: Session = Depends(get_db)):
    pagamento_existente = db.query(PagamentoModel).filter(
        PagamentoModel.id_pagamento == id
    ).first()

    db.delete(pagamento_existente)
    db.commit()

    return {"msg": "Pagamento deletado"}