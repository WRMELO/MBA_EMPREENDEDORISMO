# ============================================================
# BACKEND A3 - FastAPI (Sempre usa Gemini para reescrita fluida)
# ============================================================

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

# Importa a função buscar_hierarquico do módulo externo
from a3_busca import buscar_hierarquico  # ajuste conforme o nome real do arquivo

# Inicializa app FastAPI
app = FastAPI(title="A3 - Assistente Cognitivo", version="1.0")

# Modelo de entrada
class QueryRequest(BaseModel):
    pergunta: str
    n_results: int = 3  # mantém apenas o número de resultados configurável

# Modelo de resposta
class QueryResponse(BaseModel):
    origem: str
    pergunta: str
    distancia: float | None
    resposta_fluida: str | None
    respostas: list
    metadata: dict | None

# Endpoint de saúde
@app.get("/health")
def health_check():
    return {"status": "ok", "service": "A3 Backend"}

# Endpoint principal (sempre usa Gemini)
@app.post("/query", response_model=QueryResponse)
def query_rag(req: QueryRequest):
    resultado = buscar_hierarquico(
        pergunta_pt=req.pergunta,
        n_results=req.n_results,
        use_gemini=True  # <<< SEMPRE TRUE
    )

    return QueryResponse(
        origem=resultado["origem"],
        pergunta=req.pergunta,
        distancia=resultado.get("distancia"),
        resposta_fluida=resultado.get("resposta_fluida"),
        respostas=resultado.get("respostas", []),
        metadata=resultado.get("metadata")
    )

# Execução local
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
