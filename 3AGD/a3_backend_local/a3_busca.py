# ============================================================
# MÓDULO a3_busca.py – Busca Hierárquica com Gemini (versão standalone)
# ============================================================

import os
import chromadb
import google.generativeai as genai

# Configura Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
modelo_gemini = genai.GenerativeModel("gemini-1.5-flash")

# Função de tradução / reescrita via Gemini
def traduzir_texto_gemini(texto: str, origem: str, destino: str) -> str:
    prompt = f"Traduza ou reescreva o texto abaixo de {origem} para {destino}, mantendo precisão técnica:\n\n{texto}"
    try:
        resposta = modelo_gemini.generate_content(prompt)
        return resposta.text.strip()
    except Exception as e:
        print(f"[ERRO] Gemini: {e}")
        return texto

# Conexão com índice ChromaDB persistente
persist_dir = "/content/drive/Shareddrives/TRABALHO/GEMEO_DIGITAL/chroma_ssot_a3/"
client = chromadb.PersistentClient(path=persist_dir)
col_ref = client.get_collection("ssot_ref")
col_apoio = client.get_collection("ssot_apoio")

# Função de busca
def buscar_hierarquico(pergunta_pt: str, n_results: int = 3, max_dist: float = 0.8, use_gemini: bool = True):
    """
    Busca hierárquica no índice ChromaDB com tradução e reescrita fluida usando Gemini.
    """
    # --- Busca na referência técnica ---
    try:
        ref_result = col_ref.query(
            query_texts=[pergunta_pt],
            n_results=n_results,
            include=["documents", "metadatas", "distances"]
        )
        if ref_result.get("documents") and ref_result["documents"][0]:
            best_dist = ref_result["distances"][0][0]
            if best_dist <= max_dist:
                respostas = ref_result["documents"][0]
                resposta_fluida = traduzir_texto_gemini(
                    "Reescreva o texto abaixo, melhorando fluidez e clareza sem adicionar novas informações:\n\n" +
                    "\n".join(respostas),
                    "português", "português"
                ) if use_gemini else None
                return {
                    "origem": "referencia_tecnica",
                    "pergunta": pergunta_pt,
                    "distancia": round(best_dist, 3),
                    "respostas": respostas,
                    "resposta_fluida": resposta_fluida,
                    "metadata": ref_result["metadatas"][0]
                }
    except Exception as e:
        print(f"[ERRO] Falha na busca ref: {e}")

    # --- Busca nos documentos de apoio ---
    try:
        pergunta_en = traduzir_texto_gemini(pergunta_pt, "português", "inglês")
        apoio_result = col_apoio.query(
            query_texts=[pergunta_en],
            n_results=n_results,
            include=["documents", "metadatas", "distances"]
        )
        if apoio_result.get("documents") and apoio_result["documents"][0]:
            best_dist = apoio_result["distances"][0][0]
            if best_dist <= max_dist:
                respostas_en = apoio_result["documents"][0]
                respostas_pt = [traduzir_texto_gemini(r, "inglês", "português") for r in respostas_en]
                resposta_fluida = traduzir_texto_gemini(
                    "Reescreva o texto abaixo, melhorando fluidez e clareza sem adicionar novas informações:\n\n" +
                    "\n".join(respostas_pt),
                    "português", "português"
                ) if use_gemini else None
                return {
                    "origem": "documentos_apoio",
                    "pergunta_original": pergunta_pt,
                    "pergunta_traduzida": pergunta_en,
                    "distancia": round(best_dist, 3),
                    "respostas": respostas_pt,
                    "resposta_fluida": resposta_fluida,
                    "metadata": apoio_result["metadatas"][0]
                }
    except Exception as e:
        print(f"[ERRO] Falha na busca apoio: {e}")

    # --- Nenhum resultado ---
    return {
        "origem": "nenhum_resultado",
        "pergunta": pergunta_pt,
        "distancia": None,
        "respostas": [],
        "resposta_fluida": None
    }
