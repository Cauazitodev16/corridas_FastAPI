from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.usuario import UsuarioModel

usuario = APIRouter()

@usuario.post("/", status_code=status.HTTP_201_CREATED)
async def criar_usuario(dados: dict, db: Session = Depends(get_db)):
    novo = UsuarioModel(**dados)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@usuario.get("/")
async def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()

@usuario.delete("/{id}/delete")
async def deletar_usuario(id: int, db: Session = Depends(get_db)):
    item = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(item)
    db.commit()
    return {"detail": "Usuário removido"}