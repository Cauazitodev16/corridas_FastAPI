from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.classe import ClasseModel
from app.Schema.classe import ClasseSchema

classe = APIRouter()

@classe.post("/")
async def criar_classe(dados: ClasseSchema, db: Session = Depends(get_db)):
    nova_classe = ClasseModel(**dados.model_dump())
    db.add(nova_classe)
    db.commit()
    db.refresh(nova_classe)
    return nova_classe

@classe.get("/")
async def listar_classes(db: Session = Depends(get_db)):
    return db.query(ClasseModel).all()

@classe.get("/{id}")
async def buscar_classe(id: int, db: Session = Depends(get_db)):
    classe_encontrada = db.query(ClasseModel).filter(
        ClasseModel.id_classe == id
    ).first()
    return classe_encontrada

@classe.put("/{id}")
async def atualizar_classe(id: int, dados: ClasseSchema, db: Session = Depends(get_db)):
    classe_existente = db.query(ClasseModel).filter(
        ClasseModel.id_classe == id
    ).first()

    for campo, valor in dados.model_dump().items():
        setattr(classe_existente, campo, valor)

    db.commit()
    return classe_existente

@classe.delete("/{id}")
async def deletar_classe(id: int, db: Session = Depends(get_db)):
    classe_existente = db.query(ClasseModel).filter(
        ClasseModel.id_classe == id
    ).first()

    db.delete(classe_existente)
    db.commit()
    return {"msg": "Classe deletada"}