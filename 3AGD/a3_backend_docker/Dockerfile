# Imagem base
FROM python:3.12-slim

# Diretório de trabalho
WORKDIR /app

# Copia arquivos de dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir google-generativeai

# Copia o código do backend para o container
COPY main.py a3_busca.py ./

# Variável de ambiente para ChromaDB
ENV PERSIST_DIR=/app/GEMEO_DIGITAL/chroma_ssot_a3

# Porta exposta
EXPOSE 8000

# Comando padrão para iniciar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
