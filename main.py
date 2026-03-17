from fastapi import FastAPI
from app.database import Base, engine
# Importações das rotas
from app.route.pagamentos import pagamento
from app.route.usuario import usuario
from app.route.corrida import corrida
from app.route.veiculo import veiculo
from app.route.passageiro import passageiro
from app.route.motorista import motorista
from app.route.motorista_veiculo import motorista_veiculo
from app.route.avaliacao import avaliacao
from app.route.servico import servico
from app.route.classe import classe
from app.route.tipo_combustivel import tipo_combustivel
from app.route.modelo_veiculo import modelo_veiculo
from app.route.metodo_pagamento import metodo_pagamento

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registro individual de cada rota
app.include_router(pagamento),
app.include_router(usuario),
app.include_router(corrida),
app.include_router(veiculo),
app.include_router(passageiro),
app.include_router(motorista),
app.include_router(motorista_veiculo),
app.include_router(avaliacao),
app.include_router(servico),
app.include_router(classe),
app.include_router(tipo_combustivel),
app.include_router(modelo_veiculo),
app.include_router(metodo_pagamento),

@app.get("/")
async def health_check():
    return {"status": "API online!"}