FROM python:3.11-slim

# Instalar pacotes essenciais
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Instalar dependências Python
RUN pip install --no-cache-dir jupyter pandas numpy sentence-transformers chromadb fastapi uvicorn

# Criar diretório de trabalho
WORKDIR /workspace

# Expor porta do Jupyter
EXPOSE 8888

# Comando padrão: iniciar Jupyter
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
