from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.corrida import CorridaModel
# from app.schema.corrida import CorridaSchema # Importe quando criar o Schema

corrida = APIRouter(prefix="/corridas", tags=["Corridas"])

@corrida.post("/", status_code=status.HTTP_201_CREATED)
async def criar_corrida(dados: dict, db: Session = Depends(get_db)):
    nova_corrida = CorridaModel(**dados)
    db.add(nova_corrida)
    db.commit()
    db.refresh(nova_corrida)
    return nova_corrida

@corrida.get("/")
async def listar_corridas(db: Session = Depends(get_db)):
    return db.query(CorridaModel).all()

@corrida.get("/{id}")
async def buscar_corrida(id: int, db: Session = Depends(get_db)):
    item = db.query(CorridaModel).filter(CorridaModel.id_corrida == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")
    return item

@corrida.delete("/{id}")
async def deletar_corrida(id: int, db: Session = Depends(get_db)):
    item = db.query(CorridaModel).filter(CorridaModel.id_corrida == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")
    db.delete(item)
    db.commit()
    return {"detail": "Corrida deletada com sucesso"