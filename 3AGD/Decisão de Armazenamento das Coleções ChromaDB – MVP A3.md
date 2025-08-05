

## **1. Contexto**
Durante o desenvolvimento do MVP A3, foi necessário definir como as coleções ChromaDB (`a3_embeddings` e `a3_support_embeddings`) seriam disponibilizadas dentro do container Docker que compõe a solução.

Duas opções técnicas foram avaliadas:

1. **Embutir as coleções diretamente na imagem Docker.**
2. **Manter as coleções em um volume externo, acessado pelo container via caminho relativo.**

---

## **2. Opções Avaliadas**

### **Opção 1 – Coleções Embutidas na Imagem**
- As coleções são copiadas para dentro da imagem durante o `docker build`.
- O container já contém todos os dados no momento da entrega.

**Vantagens:**
- Simplicidade extrema na entrega (basta rodar o container).
- Nenhuma configuração de volume necessária.

**Desvantagens:**
- Qualquer rebuild da imagem apaga e exige reindexação das coleções.
- Backup das coleções exige exportação da imagem inteira.
- Escalabilidade e manutenção prejudicadas.

---

### **Opção 2 – Coleções em Volume Externo Montado**
- As coleções permanecem fora da imagem, em um volume persistente.
- O container apenas monta e acessa esses dados no runtime.

**Vantagens:**
- Persistem após rebuilds e atualizações de imagem.
- Atualizações de índice sem rebuild do container.
- Backup simples e escalável.
- Arquitetura já preparada para produção.

**Desvantagens:**
- Requer montagem de volume no `docker-compose.yml`.
- Um pouco mais de configuração inicial.

---

## **3. Comparativo Resumido**

| **Critério**                 | **Embutidas na Imagem**                              | **Volume Externo**                                      |
|------------------------------|-----------------------------------------------------|--------------------------------------------------------|
| **Complexidade de Entrega**  | Muito baixa – apenas a imagem é entregue.           | Média – requer configuração de volume.                 |
| **Persistência em Rebuilds** | Dados são apagados com rebuild.                     | Dados permanecem intactos.                             |
| **Atualização das Coleções** | Necessário rebuild.                                 | Independente do container.                             |
| **Backup**                   | Exporta a imagem inteira.                           | Basta copiar o volume.                                 |
| **Escalabilidade**           | Limitada.                                           | Alta, compatível com ambientes produtivos.             |
| **Adequado para MVP?**       | Sim, se simplicidade for prioridade.                | Sim, se priorizada a portabilidade e manutenção.       |
| **Adequado para Produção?**  | Não.                                                | Sim, recomendado.                                      |

---

## **4. Decisão Tomada (05/08/2025)**

Após análise técnica e considerando a evolução futura do projeto:

- As coleções **não serão embutidas dentro da imagem Docker**.
- Elas serão mantidas em um **diretório relativo** dentro do projeto (`3AGD/chroma_ssot_a3`).
- O `docker-compose.yml` montará a pasta do projeto do host em `/app` dentro do container.
- O backend usará sempre um **caminho relativo fixo** para acessar as coleções:

```python
PERSIST_DIR = "./3AGD/chroma_ssot_a3"
````

---

## **5. Motivos da Escolha**

1. **Portabilidade** – não há dependência de caminhos absolutos do host.
    
2. **Persistência** – os dados não são perdidos em rebuilds.
    
3. **Escalabilidade** – arquitetura já pronta para evolução.
    
4. **Manutenção Simples** – atualizações e backups são triviais.
    

---

## **6. Conclusão**

Essa abordagem garante que o MVP A3 seja:

- **Simples de rodar** (volume configurado no `docker-compose`).
    
- **Pronto para manutenção futura** sem retrabalho.
    
- **Compatível com produção**, eliminando a necessidade de revisitar esta decisão.
    

**Decisão consolidada e não sujeita a reavaliação.**
