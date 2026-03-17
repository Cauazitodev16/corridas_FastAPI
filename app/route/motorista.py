Entendido! Vou criar o código completo para os arquivos da sua pasta route, seguindo rigorosamente o padrão que você usa (com Depends(get_db), model_dump() e o estilo do seu CRUD de Séries).

Como você tem muitos arquivos, vou começar pelos principais (os que formam o "coração" do sistema).

1. Rota de Passageiro (app/route/passageiro.py)
Este lida com quem pede a corrida.

Python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.passageiro import PassageiroModel
# from app.schema.passageiro import PassageiroSchema # Descomente quando criar o schema

passageiro = APIRouter(prefix="/passageiros", tags=["Passageiros"])

@passageiro.post("/", status_code=status.HTTP_201_CREATED)
async def criar_passageiro(dados: dict, db: Session = Depends(get_db)):
    # Nota: Quando tiver o Schema, use: dados.model_dump()
    novo_passageiro = PassageiroModel(**dados)
    db.add(novo_passageiro)
    db.commit()
    db.refresh(novo_passageiro)
    return novo_passageiro

@passageiro.get("/")
async def listar_passageiros(db: Session = Depends(get_db)):
    return db.query(PassageiroModel).all()

@passageiro.put("/{id}/update")
async def atualizar_passageiro(id: int, dados: dict, db: Session = Depends(get_db)):
    passageiro_encontrada = db.query(PassageiroModel).filter(PassageiroModel.id_passageiro == id).first()

    if not passageiro_encontrada:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Passageiro com id {id} não encontrado",
        )

    for chave, valor in dados.items():
        setattr(passageiro_encontrada, chave, valor)

    db.commit()
    db.refresh(passageiro_encontrada)
    return passageiro_encontrada

@passageiro.delete("/{id}/delete")
async def deletar_passageiro(id: int, db: Session = Depends(get_db)):
    item = db.query(PassageiroModel).filter(PassageiroModel.id_passageiro == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Passageiro não encontrado")
    
    db.delete(item)
    db.commit()
    return {"message": "Passageiro apagado com sucesso"}
2. Rota de Motorista (app/route/motorista.py)
Python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.motorista import MotoristaModel

motorista = APIRouter(prefix="/motoristas", tags=["Motoristas"])

@motorista.post("/", status_code=status.HTTP_201_CREATED)
async def criar_motorista(dados: dict, db: Session = Depends(get_db)):
    novo = MotoristaModel(**dados)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@motorista.get("/")
async def listar_motoristas(db: Session = Depends(get_db)):
    return db.query(MotoristaModel).all()

@motorista.delete("/{id}/delete")
async def deletar_motorista(id: int, db: Session = Depends(get_db)):
    item = db.query(MotoristaModel).filter(MotoristaModel.id_motorista == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    db.delete(item)
    db.commit()
    return {"message": "Motorista removido"}