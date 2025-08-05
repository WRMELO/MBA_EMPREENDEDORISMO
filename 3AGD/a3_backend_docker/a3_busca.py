import os
from chromadb import Client
from chromadb.config import Settings
import google.generativeai as genai

# ========================================
# Configuração do ChromaDB
# ========================================
PERSIST_DIR = os.getenv("PERSIST_DIR", "/app/GEMEO_DIGITAL/chroma_ssot_a3")
client = Client(Settings(persist_directory=PERSIST_DIR))

# ========================================
# Configuração do Gemini
# ========================================
GEMINI_KEY = os.getenv("GOOGLE_API_KEY")
genai_model = None
if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)
    genai_model = genai.GenerativeModel("gemini-1.5-flash")

# ========================================
# Utilitários de Coleção
# ========================================
def get_or_create_collection(name: str):
    try:
        return client.get_collection(name)
    except Exception:
        print(f"[INFO] Coleção '{name}' não encontrada. Criando...")
        return client.create_collection(name)

col_ref = get_or_create_collection("ssot_ref")
col_apoio = get_or_create_collection("ssot_apoio")

# ========================================
# Normalização de Metadados
# ========================================
def normalizar_metadata(meta):
    if not meta:
        return {}
    if isinstance(meta, dict):
        return meta
    if isinstance(meta, list):
        if all(isinstance(item, dict) for item in meta):
            merged = {}
            for item in meta:
                merged.update(item)
            return merged
        return {"items": meta}
    return {"value": str(meta)}

# ========================================
# Função de Reescrita com Gemini (Padrão Colab)
# ========================================
def gemini_rewrite(texto: str) -> str:
    """
    Reescreve texto usando Gemini, aplicando prompt estruturado validado no Colab.
    """
    if not genai_model:
        return texto or "Nenhum conteúdo para reescrever."

    try:
        texto_limpo = (texto or "").encode("utf-8", errors="ignore").decode("utf-8").strip()
        if not texto_limpo:
            return "Texto recuperado vazio, não foi possível reescrever."

        prompt = (
            "Reescreva o seguinte conteúdo em português técnico, de forma clara, fluida e sem alterar o significado.\n\n"
            f"CONTEÚDO ORIGINAL:\n{texto_limpo}\n\n"
            "RESPOSTA:"
        )

        response = genai_model.generate_content(prompt)
        if hasattr(response, "text") and response.text:
            return response.text.strip()

        return texto_limpo

    except Exception as e:
        print(f"[WARN] Falha ao usar Gemini: {e}")
        return texto

# ========================================
# Função Principal de Busca Hierárquica
# ========================================
def buscar_hierarquico(pergunta_pt: str, n_results: int = 3, use_gemini: bool = True):
    """
    Busca hierárquica: tenta primeiro na coleção de referência técnica,
    depois em artigos de apoio. Usa Gemini para reescrever quando disponível.
    """
    try:
        # Busca na coleção principal
        res_ref = col_ref.query(query_texts=[pergunta_pt], n_results=n_results)
        if res_ref and res_ref.get("documents"):
            resposta_bruta = " ".join([doc for docs in res_ref["documents"] for doc in docs])
            resposta_fluida = gemini_rewrite(resposta_bruta) if use_gemini else resposta_bruta
            return {
                "origem": "referencia_tecnica",
                "resposta_fluida": resposta_fluida,
                "respostas": res_ref["documents"],
                "distancia": None,
                "metadata": normalizar_metadata(res_ref.get("metadatas"))
            }

        # Caso não encontre, busca na coleção de apoio
        res_apoio = col_apoio.query(query_texts=[pergunta_pt], n_results=n_results)
        if res_apoio and res_apoio.get("documents"):
            resposta_bruta = " ".join([doc for docs in res_apoio["documents"] for doc in docs])
            resposta_fluida = gemini_rewrite(resposta_bruta) if use_gemini else resposta_bruta
            return {
                "origem": "documentos_apoio",
                "resposta_fluida": resposta_fluida,
                "respostas": res_apoio["documents"],
                "distancia": None,
                "metadata": normalizar_metadata(res_apoio.get("metadatas"))
            }

        # Nenhum resultado encontrado
        return {
            "origem": "nenhum_resultado",
            "resposta_fluida": "Nenhuma informação relevante encontrada.",
            "respostas": [],
            "distancia": None,
            "metadata": {}
        }

    except Exception as e:
        print(f"[ERRO] Falha na busca: {e}")
        return {
            "origem": "erro",
            "resposta_fluida": "Erro interno no processamento da busca.",
            "respostas": [],
            "distancia": None,
            "metadata": {"erro": str(e)}
        }
