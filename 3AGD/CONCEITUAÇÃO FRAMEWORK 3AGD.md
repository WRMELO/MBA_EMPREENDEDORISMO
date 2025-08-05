
# Framework 3AGD – Conceito Atualizado

## Visão Geral
O **Framework 3AGD** é a base tecnológica e metodológica do projeto de Gêmeo Digital, estruturado em **três pilares complementares (3A’s)**.  
Cada pilar atua sobre **informações curadas** provenientes de dois repositórios centrais:

1. **Banco NoSQL raw curado** – armazena dados operacionais (históricos e em tempo real) tratados e validados.  
2. **Banco de Artigos Curados (SSOT)** – repositório de documentos técnicos e normas alinhadas à **Bíblia de Operação**, atuando como **Single Source of Truth**.

---

## A1. Aprendizado Profundo Contínuo
- **Função:** processa e analisa exclusivamente **dados curados** do banco NoSQL.  
- **Principais Entregas:**
  - Modelos de *machine learning* e *deep learning* treinados apenas com dados validados.  
  - Insights confiáveis sobre eficiência operacional e previsão de falhas.  
  - Evolução contínua do modelo à medida que o repositório curado cresce.

---

## A2. Alerta Inteligente em Tempo Real
- **Função:** monitora variáveis críticas utilizando **somente dados curados**.  
- **Principais Entregas:**
  - Detecção robusta de anomalias, sem ruídos ou falsos positivos.  
  - Emissão de alertas priorizados conforme criticidade.  
  - Geração de eventos baseada em pipelines validados, sem dependência de dados brutos.

---

## A3. Assistente Cognitivo de Operação
- **Função:** atua como interface inteligente, consultando:
  1. **Banco curado de operação** (NoSQL) para dados operacionais.  
  2. **Banco de artigos curados** em conformidade com a **Bíblia de Operação (SSOT)**.

- **Principais Entregas:**
  - Recomendações que combinam análise de dados com diretrizes normativas.  
  - Respostas em linguagem natural, sempre alinhadas ao SSOT.  
  - Suporte ao treinamento e à gestão estratégica, com total rastreabilidade das fontes.

---

## Integração dos 3A’s
Os três módulos do Framework 3AGD operam de forma integrada, sempre sobre **informações curadas e auditáveis**, garantindo:

- **Precisão preditiva** (A1)  
- **Ação preventiva confiável** (A2)  
- **Decisão operacional alinhada ao SSOT** (A3)  

Este modelo assegura que todas as recomendações e insights estejam **baseados em dados e normas oficiais**, promovendo segurança, eficiência e governança.



![[desenho conceitual.svg]]




# Framework 3AGD – Atualização com Implementação do MVP (A3 com LLM + RAG)

## Atualizações Recentes

### 1. Evolução da Estratégia para o A3
- Inicialmente, o **NotebookLM** foi avaliado como motor cognitivo provisório, usando os documentos `.md` do SSOT A3.  
- Após análise, optou-se por **desenvolver uma solução própria baseada em LLM + RAG**, garantindo:
  - Uso exclusivo do corpus curado;
  - Controle total do fluxo e escalabilidade;
  - Independência de serviços externos.

---

### 2. Estruturação do **SSOT A3**
- Criado o diretório `ssot_a3` como **repositório único** de documentos que alimentam o A3:
  - **Artigos relevantes** → deduplicados, filtrados e convertidos para `.md`;
  - **Referência Técnica Oficial (CFB)** → convertida para `referencia_tecnica_cfb.md`;
  - **Capítulos complementares** → anexados ao final da referência técnica.

---

### 3. Curadoria e Filtragem de Artigos
- **Ranking inicial** gerado por embeddings (cosine similarity) e reclassificação com base em:
  - Expressões-chave extraídas da referência técnica (PT);
  - Equivalentes semânticos em inglês para análise dos artigos.
- **Deduplicação implementada** via hash SHA256, eliminando múltiplas cópias.

---

### 4. Conversão para `.md`
- Desenvolvido conversor automático **PDF → Markdown** que:
  - Extrai texto com segmentação lógica;
  - Insere metadados (título, origem, data de conversão);
  - Garante legibilidade para processamento por LLM.
- Status:
  - Todos os artigos relevantes e a referência técnica foram convertidos e estão salvos no `ssot_a3`.

---

### 5. Transição para a Arquitetura A3 com LLM + RAG
- Decisão final: **adotar arquitetura própria** com:
  - **Frontend** em Streamlit (IHM profissional);
  - **Backend** em FastAPI, responsável por:
    - Indexação vetorial do SSOT (FAISS/ChromaDB);
    - Busca semântica (RAG);
    - Chamada para LLM barata (Gemini 1.5 Flash como prioridade);
  - **Rastreabilidade total** das fontes utilizadas na resposta.

---

## Fluxo Atualizado do A3 no MVP

```

Usuário → Interface Streamlit (MVP) → Backend FastAPI  
↳ Busca no Índice Vetorial (FAISS/ChromaDB)  
↳ Chamada RAG para LLM (Gemini 1.5 Flash)  
↳ Base SSOT_A3: referencia_tecnica_cfb.md + artigos curados

```

---

## Próximos Passos
1. **Construção do índice vetorial** com os `.md` do SSOT A3.  
2. **Desenvolvimento do backend FastAPI** para orquestração das buscas e integração com a LLM.  
3. **Integração do frontend Streamlit** ao backend.  
4. **Testes piloto** com perguntas reais, avaliando precisão e rastreabilidade.  
5. **Documentação completa** do MVP para transição futura ao A3 definitivo.

---


![[Untitled diagram _ Mermaid Chart-2025-07-30-181109.svg]]


# Framework 3AGD – Continuidade do MVP A3 (Atualização 30/07/2025)

## 6. Implementação do MVP A3 – Etapa de Indexação e Busca Hierárquica

### 6.1 Estrutura de Indexação Definida
Foi definida a criação de **dois índices vetoriais separados** usando **ChromaDB**:
- **`ssot_ref`** – contendo exclusivamente o arquivo `referencia_tecnica_cfb.md` (documento oficial em português).
- **`ssot_apoio`** – contendo todos os demais `.md` de artigos técnicos em inglês.

A decisão técnica garante **busca hierárquica**, priorizando a referência oficial antes de consultar documentos de apoio.

---

### 6.2 Persistência e Proteção contra Perdas
Durante o desenvolvimento, detectou-se a vulnerabilidade do ambiente Colab em relação à perda de dados salvos em `/content`.  
Foi adotado como diretório oficial persistente:

```

/content/drive/Shareddrives/TRABALHO/GEMEO_DIGITAL/chroma_ssot_a3/

```

Todos os índices (`.duckdb`, `.parquet`) e logs de auditoria (`indexados.log`, `falhas.log`) agora são salvos diretamente neste local.

---

### 6.3 Indexação Segura
A indexação foi implementada com:
- **Segmentação de texto com agregação mínima de 300 caracteres** para reduzir a quantidade de chunks.
- **Envio controlado em batches de 1000 chunks** (abaixo do limite interno do Chroma).
- **Logs incrementais persistentes** para retomar em caso de falha.
- **Separação correta** entre referência e artigos de apoio.

**Resultado:**  
- 118 arquivos `.md` indexados com sucesso.  
- Logs gerados e salvos no diretório persistente do projeto.

---

### 6.4 Função de Busca Hierárquica
Foi implementada a função `buscar_hierarquico()`, responsável por:

1. Consultar primeiro a coleção `ssot_ref` (respostas oficiais em português).  
2. Caso não encontre resultado relevante:
   - Traduz a pergunta PT → EN;
   - Busca na coleção `ssot_apoio`;
   - Traduz a resposta EN → PT;
   - Sinaliza que a resposta veio de documentos de apoio.

O mecanismo já está pronto para integração com modelos de tradução semântica (Gemini API).

---

## Status Atual do MVP A3

- ✅ **Corpus segmentado e indexado** com sucesso em ChromaDB.  
- ✅ **Estratégia RAG hierárquica** implementada (prioriza a referência técnica).  
- ✅ **Função `buscar_hierarquico()` pronta para integração**.  
- ✅ **Ambiente protegido contra perda de dados** (uso exclusivo do Google Drive).  

---

## Próximos Passos
1. Integrar tradução semântica real via API Gemini.  
2. Desenvolver backend FastAPI para orquestrar consultas.  
3. Criar frontend Streamlit conectado ao backend.  
4. Testes piloto com perguntas reais.  
5. Documentar integração e fluxos finais para o MVP A3.

---


# Framework 3AGD – Continuidade do MVP A3 (Atualização 31/07/2025)

## 7. Busca Hierárquica com Tradução Semântica (Gemini API)

### 7.1 Integração da Tradução Semântica
Foi integrada a **API Gemini (modelo gemini-1.5-flash)** para realizar tradução semântica:
- **Português → Inglês** para consultas nos artigos de apoio.
- **Inglês → Português** para respostas retornadas ao usuário.

A função `traduzir_texto_gemini()` garante que traduções mantenham o **contexto técnico** e **clareza operacional**, essencial para termos especializados do domínio CFB.

---

### 7.2 Filtro de Relevância
Para evitar respostas irrelevantes:
- Foi implementado um **filtro de distância** no mecanismo de busca.
- Apenas trechos com distância **≤ 0.6** são considerados relevantes.
- Caso nenhum resultado supere esse critério, a resposta retorna `nenhum_resultado`.

---

### 7.3 Estado Atual da Função `buscar_hierarquico()`
A função agora:
1. **Busca primeiro** na coleção `ssot_ref` (referência técnica).
2. **Aplica o filtro de relevância**.
3. Se não encontrar resultado, traduz a pergunta e consulta `ssot_apoio`.
4. Traduz as respostas encontradas e retorna ao usuário.
5. Caso nada relevante seja encontrado, retorna `nenhum_resultado`.

---

# 8. Arquitetura Planejada do Backend FastAPI para o MVP A3

### 8.1 Objetivo
O backend FastAPI será o **orquestrador central** do MVP A3, responsável por:
- Gerenciar consultas vindas do frontend (Streamlit).
- Conectar-se ao índice ChromaDB persistente.
- Usar a função `buscar_hierarquico()` para recuperação contextual.
- Realizar chamadas à API Gemini para tradução semântica.

---

### 8.2 Componentes do Backend

1. **API REST FastAPI**
   - Endpoints principais:
     - `GET /health` → verifica se o serviço está ativo.
     - `POST /query` → recebe uma pergunta em PT e retorna resposta hierárquica.
   - Retorna JSON estruturado contendo:
     - Origem (`referencia_tecnica`, `documentos_apoio`, `nenhum_resultado`)
     - Pergunta original
     - Respostas
     - Metadados e distância de relevância

2. **Camada de Recuperação (RAG)**
   - Conecta-se ao ChromaDB persistente.
   - Realiza busca vetorial nas coleções `ssot_ref` e `ssot_apoio`.

3. **Camada de Tradução**
   - Usa Gemini API para tradução bidirecional, integrada ao fluxo RAG.

4. **Camada de Logging**
   - Registra cada requisição e resposta em banco (para auditoria).
   - Mantém histórico de perguntas, origem da resposta e metadados.

---

### 8.3 Fluxo de Operação Planejado

![[Untitled diagram _ Mermaid Chart-2025-07-31-110401.svg]]
# Framework 3AGD – Continuidade do MVP A3 (Atualização 31/07/2025)

## 9. Método Híbrido de Resposta (RAG + Gemini)

### 9.1 Descrição do Método
Após os testes realizados, foi consolidado o uso de um método híbrido que combina:
1. **RAG (ChromaDB)** – Recupera trechos diretamente do corpus SSOT (referência técnica e artigos de apoio).
2. **Gemini API (opcional)** – Atua apenas como **pós-processador**, reescrevendo as respostas em português de forma mais fluida, sem introduzir informações externas.

### 9.2 Vantagens do Método
- **Controle de Conteúdo:** As informações vêm exclusivamente do corpus indexado.
- **Melhoria de Clareza:** Gemini organiza e melhora a legibilidade das respostas.
- **Mitigação de Riscos:** O modelo é instruído a não inventar dados, apenas reformular.

### 9.3 Fluxo Operacional do Método Híbrido
1. O usuário envia uma pergunta em português.
2. A função `buscar_hierarquico()` consulta primeiro a coleção `ssot_ref`.
3. Caso não haja resultado relevante, busca nos artigos de apoio (`ssot_apoio`) com tradução PT ↔ EN.
4. A resposta recuperada é enviada opcionalmente para o Gemini, que reescreve o texto mantendo fidelidade ao SSOT.

---

## 9.4 Diagrama do Fluxo (Atualizado)

![[Untitled diagram _ Mermaid Chart-2025-07-31-120203.svg]]

# **Plano Geral para Containerização do Backend A3 – MVP 3AGD**

## **1. Por que Containerizar o Backend A3?**

A containerização é adotada neste projeto para resolver problemas de:

- **Dependência de Ambiente**: elimina conflitos de bibliotecas e diferenças entre Windows, Linux ou Colab.  
- **Portabilidade**: garante que o backend possa ser executado em qualquer máquina com Docker.  
- **Persistência Segura**: separa os dados (coleções ChromaDB) do ambiente de execução, evitando perdas em rebuilds.  
- **Escalabilidade Futura**: facilita a integração com outros serviços (Streamlit, MinIO, APIs externas) sem retrabalho.  
- **Manutenção Simplificada**: reduz complexidade de paths, reinstalações e ajustes manuais.

---

## **2. Estrutura do Projeto Containerizado**

C:\Users\wilso\a3_backend_docker  
├── Dockerfile  
├── docker-compose.yml  
├── requirements.txt  
├── main.py  
├── a3_busca.py  
└── (volume externo) C:\Users\wilso\GEMEO_DIGITAL_LOCAL\


- **Código**: armazenado na imagem do container (`/app`).  
- **Coleções ChromaDB**: ficam em volume externo (`GEMEO_DIGITAL_LOCAL`) e são montadas em `/app/GEMEO_DIGITAL`.

---

## **3. Estratégia de Caminhos**

- **Interno ao container**:  
  - Código → `/app`  
  - Coleções → `/app/GEMEO_DIGITAL`

- **No host Windows**:  
  - Variável de ambiente `GEMEO_PATH` aponta para `C:\Users\wilso\GEMEO_DIGITAL_LOCAL`.  
  - `docker-compose.yml` usa esta variável para montar o volume.

---

## **4. Componentes do Ambiente**

### **4.1 Dockerfile**
- Base: `python:3.12-slim`  
- Instala dependências de `requirements.txt`  
- Copia código para `/app`  
- Define `WORKDIR /app`  
- Comando de inicialização roda `uvicorn main:app --host 0.0.0.0 --port 8000`

---

### **4.2 docker-compose.yml**
- Serviço: `a3_backend`  
- Porta exposta: `8000`  
- Volume: mapeia `GEMEO_DIGITAL_LOCAL` → `/app/GEMEO_DIGITAL`  
- Variável `GEMEO_PATH` define caminho externo do host

---

## **5. Ajustes Necessários no Código**

- `a3_busca.py` deve usar o caminho interno:

```python
PERSIST_DIR = "/app/GEMEO_DIGITAL/chroma_ssot_a3"
```

# Framework 3AGD – Atualização (Retomada 04/08/2025)

## Situação Atual

- **Repositório GitHub** corrigido, limpo e sincronizado com o estado atual do projeto.  
- **Pastas locais `base_raw`, `chroma_ssot_a3` e `venv` foram apagadas** e não puderam ser recuperadas.  
- **Documentos `.md` (SSOT A3) permanecem versionados** e podem ser reindexados.  
- Decisão consolidada: **desenvolvimento passa a ser feito exclusivamente via notebook Jupyter dentro do container VS Code**, com posterior conversão para `.py`.

---

## Mudanças Recentes

1. **Volume de Dados Reposicionado**  
   - Agora o diretório de trabalho oficial é:  
     ```
     C:\Users\wilso\MBA_EMPREENDEDORISMO\3AGD
     ```
   - Ele deve ser montado dentro do container em:  
     ```
     /app/3AGD
     ```

2. **Nova Estrutura de Arquivos Docker**  
   - `Dockerfile` e `docker-compose.yml` foram movidos para:  
     ```
     C:\Users\wilso\MBA_EMPREENDEDORISMO\3AGD\a3_backend_docker
     ```
   - Esta será a raiz da configuração Docker para o backend A3.

---

# Plano de Ajuste do Docker Compose

Para suportar o novo caminho, o `docker-compose.yml` deverá:

- Montar o volume:
  ```yaml
  volumes:
    - C:/Users/wilso/MBA_EMPREENDEDORISMO/3AGD:/app/3AGD
```

- Garantir que o backend aponte para o índice:
    
    ```python
    PERSIST_DIR = "/app/3AGD/chroma_ssot_a3"
    ```
    

---

## Novo Fluxo de Desenvolvimento

1. **Criação do notebook de desenvolvimento `a3_dev.ipynb` dentro do container**.
    
2. **Células encadeadas**, seguindo esta ordem:
    
    1. Configuração inicial (dependências, API Gemini, paths).
        
    2. Conexão com ChromaDB e carregamento de coleções.
        
    3. Funções auxiliares (tradução e reescrita via Gemini 1.5 Flash).
        
    4. Função principal `buscar_hierarquico()`.
        
    5. Teste unitário da busca.
        
    6. Auditoria e logging de consultas.
        
3. **Após validação**, conversão para módulo `.py` e integração ao backend FastAPI.
    

---

## Integração Gemini 1.5 Flash

- A API Gemini será utilizada tanto para:
    
    - **Tradução PT ↔ EN** (quando buscar nos artigos de apoio).
        
    - **Reescrita final das respostas** (pós-processamento).
        
- A variável de ambiente `GOOGLE_API_KEY` deve ser lida no notebook, evitando exposição de segredos.
    

---

## Próximos Passos

1. Ajustar `docker-compose.yml` para montar corretamente `C:\Users\wilso\MBA_EMPREENDEDORISMO\3AGD` dentro do container.
    
2. Criar o notebook `a3_dev.ipynb` dentro do container e implementar a **primeira célula de configuração**.
    
3. Reindexar o corpus SSOT A3 no novo volume.
    
4. Validar buscas hierárquicas com Gemini 1.5 Flash.
    

---

**Este documento está agora atualizado até o estado atual do projeto e já reflete as novas decisões de caminho, arquitetura e método de desenvolvimento.**


  

# Framework 3AGD – Atualização (05/08/2025)

  

## Estado Atual após Reestruturação Completa do Ambiente

  

### 1. Separação Definitiva das Bases

- **Base Principal (SSOT)**: contém exclusivamente o documento `0_referencia_tecnica_cfb.md`.

- **Base de Apoio**: inclui todos os demais artigos técnicos em inglês, processados separadamente.

  

Esta divisão garante que o A3 priorize o **SSOT oficial** e somente recorra aos artigos de apoio quando necessário, aplicando tradução PT ↔ EN.

  

---

  

### 2. Novo Ambiente de Desenvolvimento

- Desenvolvimento agora é feito **exclusivamente dentro de notebooks Jupyter** rodando no container `a3_jupyter_local`.

- O volume montado `C:/Users/wilso/MBA_EMPREENDEDORISMO/3AGD` é acessível em `/workspace` dentro do container.

- Apenas após validação as funções serão convertidas para módulos `.py`.

  

---

  

### 3. Indexação Atualizada

- Reindexação completa das duas bases foi realizada diretamente a partir de `ssot_a3`.

- Coleções criadas:

  - `a3_embeddings` → Base Principal.

  - `a3_support_embeddings` → Base de Apoio.

- Logs gerados:

  - `base_principal_index.csv`

  - `base_apoio_index.csv`

  

---

  

### 4. Pipeline de Consulta Atual

O fluxo de consulta definido:

  

1. **Busca primária** no SSOT (`a3_embeddings`).

2. Se não houver resultado relevante:

   - Tradução da pergunta (PT → EN) via **API Gemini Flash**.

   - Busca na base de apoio (`a3_support_embeddings`).

   - Tradução da resposta (EN → PT) e apresentação ao usuário.

3. Resposta final opcionalmente reescrita pelo Gemini para maior clareza, sem adição de informações externas.

  

---

  

### 5. Próximas Etapas Definidas

1. **Finalizar a função `buscar_hierarquico()`** dentro do notebook, já integrada ao ChromaDB e Gemini.

2. **Implementar camada de auditoria** que registre todas as consultas e respostas.

3. **Após validação**, conversão do notebook em módulo `.py` para integração no backend FastAPI.

4. Desenvolvimento do **frontend Streamlit** para interação final com o usuário.

  

---

  

**Com esta atualização, o documento reflete fielmente o estado atual do projeto, já alinhado com a nova estratégia de desenvolvimento containerizado e o uso das duas bases vetoriais separadas.**