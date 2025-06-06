# Modelo de Negócio e Projeção Financeira: Consultoria & Framework 3AGD

Este documento detalha o modelo de negócio, estrutura de custos, projeção de receitas e análise de rentabilidade para uma consultoria especializada na implementação do Framework 3AGD.

(#Data Lake, #Data Driven, #Digital Twin, #Deep Learning, #Machine Learning) 

## 1. Perfis de Cliente Típicos

### 1.1. Cliente Tipo 1: Termoelétrica CFB

*   **Perfil do Cliente:**
    *   Capacidade Instalada: 345 MW
    *   Operação a Plena Carga: 180 dias/ano (equivalente a 4.320 horas/ano)
    *   Combustível Principal: Carvão mineral nacional
    *   Outros Insumos: Calcário, etc.
    *   DMT (Distância Média de Transporte): 20 km

### 1.2. Cliente Tipo 2: Fabricante de Ferro-Ligas

*   **Perfil do Cliente:**
    *   Capacidade de Produção: 100.000 toneladas/ano (100 kt/ano)
    *   Combustível Principal: Carvão vegetal (redutor) e energia elétrica.

## 2. Fases do Projeto de Consultoria

1.  **Fase 1: Diagnóstico e Prova de Conceito (PoC)**
    *   **1.A: MVP para Análise da Qualidade de Dados:** Avaliação rápida e direcionada da qualidade dos dados existentes.
    *   **1.B: Desenvolvimento de Data Lake Protótipo (Open Source):** Implementação de um Data Lake básico com ferramentas open source (MinIO, MongoDB) para demonstrar a viabilidade e coletar dados iniciais.
2.  **Fase 2: Apoio à Implementação do Data Lake Definitivo**
    *   Consultoria estratégica para auxiliar o cliente na escolha, contratação e supervisão da implementação de uma solução de Data Lake robusta e escalável por terceiros ou pela equipe interna do cliente.
3.  **Fase 3: Implementação do Framework 3AGD**
    *   Desenvolvimento e implantação dos componentes do Framework 3AGD, utilizando o Data Lake definitivo como base:
        *   **1º Componente=> Aprendizado Profundo Contínuo:** Modelos para otimização de processos, manutenção preditiva, etc.
        *   **2º Componente=> Alerta Inteligente em Tempo Real:** Sistema de monitoramento e alertas baseado em IA.
        *   **3º Componente=> Assistente Cognitivo de Operação:** Interface em linguagem natural para acesso a dados, insights e recomendações.
4.  **Fase 4: Pós-Implementação e Taxa de Sucesso**
    *   Acompanhamento dos resultados e recebimento de uma taxa de sucesso baseada nos ganhos comprovados do cliente.

## 3. Estrutura de Custos da Consultoria (Com Estimativas)

### 3.1. Custos Diretos

#### 3.1.1. Custos de Mão de Obra PJ/Terceiros (Estimativas de Mercado - Quartil Superior)

*   **Engenheiro/Arquiteto de Dados Sênior (EADS):**
    *   Custo Diário Mínimo: R$ 1.200,00
    *   Custo Diário Esperado: R$ 1.400,00
    *   Custo Diário Máximo: R$ 1.700,00
*   **Cientista de Dados/Especialista em IA/PNL Sênior (CDS):**
    *   Custo Diário Mínimo: R$ 1.100,00
    *   Custo Diário Esperado: R$ 1.350,00
    *   Custo Diário Máximo: R$ 1.650,00
*   **Engenheiro MLOps Pleno (MLOps):**
    *   Custo Diário Mínimo: R$ 700,00
    *   Custo Diário Esperado: R$ 900,00
    *   Custo Diário Máximo: R$ 1.100,00

#### 3.1.2. Custos de Ferramentas e Infraestrutura para Projetos (Estimativas)

*   **Fase 1 (Protótipo Data Lake Open Source - MinIO/Mongo):**
    *   Mínimo: R$ 200,00
    *   Esperado: R$ 500,00
    *   Máximo: R$ 1.000,00
*   **Fase 3 (Implementação do Framework 3AGD - por componente principal):**
    *   Mínimo: R$ 1.100,00
    *   Esperado: R$ 3.500,00
    *   Máximo: R$ 8.500,00

### 3.2. Custos Indiretos Fixos Mensais da Consultoria (Estimativas)

*   **Pró-labore do Diretor (PMO):** R$ 40.000,00 (R$ 480.000,00/ano)
*   **Coworking:**
    *   Mínimo: R$ 1.500,00 | Esperado: R$ 2.500,00 | Máximo: R$ 4.000,00
*   **Software:**
    *   Mínimo: R$ 500,00 | Esperado: R$ 1.000,00 | Máximo: R$ 2.000,00
*   **Marketing e Vendas Iniciais:**
    *   Mínimo: R$ 500,00 | Esperado: R$ 1.500,00 | Máximo: R$ 3.000,00
*   **Outras Despesas Administrativas:**
    *   Mínimo: R$ 300,00 | Esperado: R$ 700,00 | Máximo: R$ 1.200,00
*   **Total de Outros Custos Indiretos Fixos Mensais (Excluindo Pró-Labore):**
    *   Mínimo: R$ 2.800,00 | Esperado: R$ 5.700,00 | Máximo: R$ 10.200,00
*   **Total Geral de Custos Indiretos Fixos Mensais (Incluindo Pró-Labore):**
    *   Mínimo: R$ 42.800,00 | Esperado: R$ 45.700,00 | Máximo: R$ 50.200,00

### 3.3. Estimativa de Esforço (Dias-Homem - DH) por Fase e Perfil

#### Fase 1: MVP e Protótipo de Data Lake

**1.A. MVP para Análise da Qualidade de Dados**
*   EADS: Mín 3 DH, Esp 5 DH, Máx 7 DH
*   CDS: Mín 2 DH, Esp 3 DH, Máx 5 DH

**1.B. Desenvolvimento de Data Lake Protótipo (Open Source)**
*   EADS: Mín 5 DH, Esp 8 DH, Máx 12 DH
*   MLOps: Mín 3 DH, Esp 5 DH, Máx 7 DH

#### Fase 2: Apoio à Implementação do Data Lake Definitivo

*   EADS: Mín 8 DH, Esp 12 DH, Máx 16 DH

#### Fase 3: Implementação do Framework 3AGD (por componente)

**3.A. Componente: Aprendizado Profundo Contínuo**
*   EADS: Mín 7 DH, Esp 10 DH, Máx 15 DH
*   CDS: Mín 15 DH, Esp 20 DH, Máx 30 DH
*   MLOps: Mín 10 DH, Esp 15 DH, Máx 20 DH

**3.B. Componente: Alerta Inteligente em Tempo Real**
*   EADS: Mín 8 DH, Esp 12 DH, Máx 18 DH
*   CDS: Mín 5 DH, Esp 8 DH, Máx 12 DH
*   MLOps: Mín 7 DH, Esp 10 DH, Máx 15 DH

**3.C. Componente: Assistente Cognitivo de Operação**
*   EADS: Mín 5 DH, Esp 7 DH, Máx 10 DH
*   CDS: Mín 12 DH, Esp 18 DH, Máx 25 DH
*   MLOps: Mín 7 DH, Esp 10 DH, Máx 15 DH

### 3.4. Cálculo dos Custos de Desenvolvimento por Fase

#### 3.4.1. Custos de Mão de Obra por Fase (Exemplos - Cenário Esperado)

*   **Fase 1.A (MVP Qualidade):** EADS (5 * R$1400) + CDS (3 * R$1350) = R$7000 + R$4050 = R$11.050
*   **Fase 1.B (Protótipo DL):** EADS (8 * R$1400) + MLOps (5 * R$900) = R$11200 + R$4500 = R$15.700
*   **Fase 2 (Apoio DL):** EADS (12 * R$1400) = R$16.800
*   **Fase 3.A (Apr. Profundo):** EADS (10*1400)+CDS (20*1350)+MLOps (15*900) = 14000+27000+13500 = R$54.500
*   **Fase 3.B (Alerta Inteligente):** EADS (12*1400)+CDS (8*1350)+MLOps (10*900) = 16800+10800+9000 = R$36.600
*   **Fase 3.C (Assist. Cognitivo):** EADS (7*1400)+CDS (18*1350)+MLOps (10*900) = 9800+24300+9000 = R$43.100

*(Cálculos completos para Mín, Esp, Máx foram feitos em separado e são base para a seção de Receitas)*

#### 3.4.2. Custos Totais Diretos de Desenvolvimento por Fase (Mão de Obra + Ferramentas/Infra - Cenário Esperado)

*   **Fase 1.A:** R$ 11.050 (MO) + R$ 0 (Ferramentas) = R$ 11.050
*   **Fase 1.B:** R$ 15.700 (MO) + R$ 500 (Ferramentas) = R$ 16.200
*   **Fase 2:** R$ 16.800 (MO) = R$ 16.800
*   **Fase 3.A:** R$ 54.500 (MO) + R$ 3.500 (Ferramentas) = R$ 58.000
*   **Fase 3.B:** R$ 36.600 (MO) + R$ 3.500 (Ferramentas) = R$ 40.100
*   **Fase 3.C:** R$ 43.100 (MO) + R$ 3.500 (Ferramentas) = R$ 46.600

## 4. Estrutura de Receitas da Consultoria

**Parâmetros Chave para Precificação:**
*   **Percentual de Rateio dos Custos Indiretos (CI_Rateio):** 15% sobre os Custos Diretos da Fase.
*   **Margem de Lucro da Fase de Desenvolvimento (ML_Dev):** 30% sobre o Custo Total (Direto + Indireto Rateado).

### 4.1. Receita e Lucro das Fases de Desenvolvimento (Cenário Esperado)

| Fase                        | CDT Esperado | CIR (15%) Esperado | CTD Esperado | Preço Cliente (Receita) Esperado | Lucro Bruto Esperado |
| :-------------------------- | :----------- | :----------------- | :----------- | :------------------------------- | :------------------- |
| 1.A MVP Qualidade           | R$ 11.050,00 | R$ 1.657,50        | R$ 12.707,50 | R$ 16.519,75                     | R$ 3.812,25          |
| 1.B Protótipo DL            | R$ 16.200,00 | R$ 2.430,00        | R$ 18.630,00 | R$ 24.219,00                     | R$ 5.589,00          |
| 2 Apoio DL Definitivo       | R$ 16.800,00 | R$ 2.520,00        | R$ 19.320,00 | R$ 25.116,00                     | R$ 5.796,00          |
| 3.A Aprendizado Profundo    | R$ 58.000,00 | R$ 8.700,00        | R$ 66.700,00 | R$ 86.710,00                     | R$ 20.010,00         |
| 3.B Alerta Inteligente      | R$ 40.100,00 | R$ 6.015,00        | R$ 46.115,00 | R$ 59.949,50                     | R$ 13.834,50         |
| 3.C Assistente Cognitivo    | R$ 46.600,00 | R$ 6.990,00        | R$ 53.590,00 | R$ 69.667,00                     | R$ 16.077,00         |
| **Total por Cliente**       | **R$ 188.750,00**| **R$ 28.312,50**   | **R$ 217.062,50**| **R$ 282.181,25**                | **R$ 65.118,75**     |

### 4.2. Receita da Fase Pós-Implementação do 3AGD (Taxa de Sucesso)

*   **Modelo:** 5% sobre o Ganho Anual do Cliente, limitado a R$ 1.000.000,00/ano por cliente, durante 5 anos.
*   **Custos Anuais Associados (Monitoramento, Gestão):** Esperado R$ 10.000,00/ano por cliente.

## 5. Estimativa de Ganhos Potenciais do Cliente

### 5.1. Cliente Tipo 1: Termoelétrica CFB

*   **A. Redução do Consumo de Carvão (5%):**
    *   Redução Anual: 37.260 toneladas/ano.
    *   Ganho Financeiro Anual (R$ 400/ton): **R$ 14.904.000,00/ano**.
*   **B. Redução do Downtime (50%):**
    *   Redução Anual: 64,8 horas/ano.
    *   Ganho Financeiro Anual (R$ 250/MWh): **R$ 5.589.000,00/ano**.
*   **Ganho Total Anual Estimado (Termoelétrica): R$ 20.493.000,00/ano**.

### 5.2. Cliente Tipo 2: Fabricante de Ferro-Ligas

*   **A. Redução do Consumo de Carvão Vegetal (6%):**
    *   Redução Anual: 4.200 toneladas/ano.
    *   Ganho Financeiro Anual (R$ 700/ton): **R$ 2.940.000,00/ano**.
*   **B. Redução do Downtime do Forno (40%):**
    *   Redução Anual: 134,4 horas/ano.
    *   Ganho Financeiro Anual (Margem de R$ 4.000/ton): **R$ 6.397.440,00/ano**.
*   **Ganho Total Anual Estimado (Ferro-Ligas): R$ 9.337.440,00/ano**.

## 6. Cálculo da Receita de Sucesso da Consultoria (Pós-Implementação)

### 6.1. Para Cliente Termoelétrica:

*   Receita Sucesso Potencial Anual: R$ 20.493.000,00 * 5% = R$ 1.024.650,00
*   Receita Sucesso Efetiva Anual (Limitada): **R$ 1.000.000,00/ano**
*   Receita Total de Sucesso (5 anos): R$ 5.000.000,00
*   Lucro Líquido TS Anual (Esperado): R$ 1.000.000 - R$ 10.000 = **R$ 990.000,00/ano**

### 6.2. Para Cliente Fabricante de Ferro-Ligas:

*   Receita Sucesso Potencial Anual: R$ 9.337.440,00 * 5% = R$ 466.872,00
*   Receita Sucesso Efetiva Anual: **R$ 466.872,00/ano**
*   Receita Total de Sucesso (5 anos): R$ 2.334.360,00
*   Lucro Líquido TS Anual (Esperado): R$ 466.872 - R$ 10.000 = **R$ 456.872,00/ano**

## 7. Análise de Rentabilidade Consolidada e Demonstração do Win-Win (Cenário Esperado)

### 7.1. Investimento Total do Cliente por Projeto (Fases de Desenvolvimento)

*   Total (Fases 1.A, 1.B, 2, 3.A, 3.B, 3.C): **R$ 282.181,25 por cliente**

### 7.2. Ganhos do Cliente vs. Receita da Consultoria (5 Anos)

**Cliente Termoelétrica:**
*   Investimento Inicial (Desenvolvimento): R$ 282.181,25
*   Custo Taxa de Sucesso (5 anos): R$ 5.000.000,00
*   **Gasto Total do Cliente com Consultoria (5 anos): R$ 5.282.181,25**
*   **Ganho Total do Cliente (5 anos): R$ 102.465.000,00**
*   Retorno sobre o Investimento para o Cliente (ROI): (R$102.465.000 / R$5.282.181,25)  ~ **19,4 vezes**

**Cliente Fabricante de Ferro-Ligas:**
*   Investimento Inicial (Desenvolvimento): R$ 282.181,25
*   Custo Taxa de Sucesso (5 anos): R$ 2.334.360,00
*   **Gasto Total do Cliente com Consultoria (5 anos): R$ 2.616.541,25**
*   **Ganho Total do Cliente (5 anos): R$ 46.687.200,00**
*   Retorno sobre o Investimento para o Cliente (ROI): (R$46.687.200 / R$2.616.541,25) ~ **17,8 vezes**

O modelo demonstra um claro "win-win", onde o investimento do cliente na consultoria gera um retorno significativamente maior através dos ganhos obtidos.

## 8. Resumo das Premissas e Bases das Estimativas

Este capítulo detalha as fontes e justificativas para os valores estimados utilizados neste modelo:

*   **Custos de Mão de Obra PJ/Terceiros:**
    *   **Estimativa:** Faixas de custo diário (Mínimo, Esperado, Máximo) para Engenheiro/Arquiteto de Dados Sênior, Cientista de Dados/Especialista IA/PNL Sênior, Engenheiro MLOps Pleno.
    *   **Base:** "Pesquisas de mercado para o quartil superior de remuneração PJ no Brasil para os perfis solicitados", conforme instrução do usuário.

*   **Custos de Ferramentas e Infraestrutura para Projetos:**
    *   **Estimativa:** Faixas de custo (Mínimo, Esperado, Máximo) para o protótipo de Data Lake e para os componentes do Framework 3AGD (Plataformas de ML, APIs de Serviços Cognitivos).
    *   **Base:** Estimativas baseadas em custos típicos de serviços de nuvem para VMs/contêineres de baixo custo para protótipos e custos de plataformas de ML/APIs para desenvolvimento e implantação inicial. O usuário validou essas estimativas como "coerentes".

*   **Custos Indiretos Fixos Mensais da Consultoria:**
    *   **Estimativa:** Faixas de custo (Mínimo, Esperado, Máximo) para Coworking, Software, Marketing e Vendas Iniciais, e Outras Despesas Administrativas. O pró-labore do diretor foi um valor fixo informado.
    *   **Base:** Estimativas iniciais sugeridas pela IA e validadas pelo usuário como "coerentes". O valor do pró-labore (R$ 40.000,00/mês) foi fornecido diretamente pelo usuário.

*   **Estimativa de Esforço (Dias-Homem) por Fase e Perfil:**
    *   **Estimativa:** Faixas de dias-homem (Mínimo, Esperado, Máximo) para cada perfil profissional em cada fase e componente do projeto.
    *   **Base:** Estimativas iniciais sugeridas pela IA, "baseadas na complexidade típica dessas fases", e o usuário optou por "usá-las como estão" para prosseguir com o modelo.

*   **Ganhos Potenciais dos Clientes (Termoelétrica e Ferro-Ligas):**
    *   **Estimativa:** Percentuais de redução de consumo de carvão/insumos e redução de downtime; valores de referência para o custo de carvão, energia não gerada e margem de produto.
    *   **Base:** "Benchmarks do setor para implementações bem-sucedidas de tecnologias de otimização e manutenção preditiva." Os valores de custo/preço de insumos e energia são "estimativas que devem ser ajustadas à realidade do mercado no momento da proposta". Os percentuais de redução de consumo e downtime foram definidos como "médias conservadoras" pela IA, com base nesses benchmarks.

*   **Percentual de Rateio dos Custos Indiretos:**
    *   **Estimativa:** 15% sobre os Custos Diretos de cada fase de desenvolvimento.
    *   **Base:** Sugestão da IA como "um valor inicial para cobrir os custos indiretos proporcionalmente", com a ressalva de que "uma análise mais precisa exigiria estimar o número total de projetos/DH produtivos no ano". O usuário concordou em "fazer com sua estimativa, depois ajustamos".

*   **Margem de Lucro da Fase de Desenvolvimento:**
    *   **Estimativa:** 30% sobre o Custo Total (Direto + Indireto Rateado).
    *   **Base:** Parâmetro definido pelo usuário no início da conversa ("lucro de 30% nas fases de desenvolvimento").

*   **Taxa de Sucesso (Pós-Implementação do 3AGD):**
    *   **Estimativa:** 5% sobre o ganho anual do cliente, limitado a R$ 1.000.000,00 por ano, por cliente, durante 5 anos.
    *   **Base:** Parâmetro definido pelo usuário no início da conversa.

*   **Custos Anuais Associados à Gestão da Taxa de Sucesso (para a Consultoria):**
    *   **Estimativa:** Faixas de custo anual (Mínimo: R$ 5.000, Esperado: R$ 10.000, Máximo: R$ 20.000) por cliente.
    *   **Base:** Estimativa da IA para cobrir atividades de baixo esforço contínuo, como monitoramento, gestão do contrato e relacionamento com o cliente.

*   **Reinvestimento e Distribuição de Dividendos:**
    *   **Estimativa:** 10% do Lucro Líquido da consultoria para reinvestimento; os 90% restantes distribuídos igualmente entre os dois sócios.
    *   **Base:** Diretrizes fornecidas pelo usuário ("lucros - 10% para reinvestimento", "somos em 2 sócios que distribuem igualmente os dividendos").

## 9. Projeção Ano a Ano da Retirada dos Sócios (Com Dois Negócios Fechados - Cenário Esperado)

**Premissas Adotadas:**
*   Dois negócios (Termoelétrica e Ferro-Ligas) fechados.
*   Valores do cenário "esperado" para custos e receitas.
*   Fases de desenvolvimento concluídas e faturadas no Ano 1.
*   Taxa de sucesso e seus custos associados a partir do Ano 1 até o Ano 5.
*   Custos Indiretos Fixos Anuais da consultoria (exceto pró-labore de PMO de R$40.000/mês): R$ 68.400,00.
*   Reinvestimento: 10% do Lucro Líquido da consultoria (antes da distribuição aos sócios).
*   Dividendos: 90% do Lucro Líquido distribuídos 50/50 entre os sócios.
*   Pró-labore de PMO (R$ 480.000/ano) retirado anualmente.
*   Não considera impostos sobre lucro da empresa ou retiradas dos sócios.

**Cálculos de Base Anualizados (Cenário Esperado):**
*   Lucro Bruto Desenvolvimento (2 clientes, Ano 1): R$ 65.118,75 * 2 = R$ 130.237,50
*   Lucro Líquido TS Anual (2 clientes): (R$990.000 Termo) + (R$456.872 Ferro-Ligas) = R$ 1.446.872,00

**Tabela de Projeção de Retiradas Anuais:**

| Descrição                                         | Ano 1           | Ano 2           | Ano 3           | Ano 4           | Ano 5           |
| :------------------------------------------------ | :-------------- | :-------------- | :-------------- | :-------------- | :-------------- |
| **Receitas e Lucros da Consultoria**              |                 |                 |                 |                 |                 |
| Lucro Bruto Desenvolvimento (2 clientes)          | R$ 130.237,50   | R$ 0,00         | R$ 0,00         | R$ 0,00         | R$ 0,00         |
| Lucro Líquido Taxa de Sucesso (2 clientes)        | R$ 1.446.872,00 | R$ 1.446.872,00 | R$ 1.446.872,00 | R$ 1.446.872,00 | R$ 1.446.872,00 |
| **Subtotal Lucro Operacional Bruto**              | **R$ 1.577.109,50** | **R$ 1.446.872,00** | **R$ 1.446.872,00** | **R$ 1.446.872,00** | **R$ 1.446.872,00** |
| (-) Custos Indiretos Fixos Anuais (exceto PL)     | R$ 68.400,00    | R$ 68.400,00    | R$ 68.400,00    | R$ 68.400,00    | R$ 68.400,00    |
| **Lucro Líquido da Consultoria (antes Reinv.)**   | **R$ 1.508.709,50** | **R$ 1.378.472,00** | **R$ 1.378.472,00** | **R$ 1.378.472,00** | **R$ 1.378.472,00** |
| (-) Reinvestimento (10%)                          | R$ 150.870,95   | R$ 137.847,20   | R$ 137.847,20   | R$ 137.847,20   | R$ 137.847,20   |
| **Lucro Disponível para Distribuição**            | **R$ 1.357.838,55** | **R$ 1.240.624,80** | **R$ 1.240.624,80** | **R$ 1.240.624,80** | **R$ 1.240.624,80** |
|                                                   |                 |                 |                 |                 |                 |
| **Retiradas do PMO**                           |                 |                 |                 |                 |                 |
| Pró-Labore Anual                                  | R$ 480.000,00   | R$ 480.000,00   | R$ 480.000,00   | R$ 480.000,00   | R$ 480.000,00   |
| Participação nos Lucros (50% do Disponível)       | R$ 678.919,28   | R$ 620.312,40   | R$ 620.312,40   | R$ 620.312,40   | R$ 620.312,40   |
| **Total Retirado por PMO**                     | **R$ 1.158.919,28** | **R$ 1.100.312,40** | **R$ 1.100.312,40** | **R$ 1.100.312,40** | **R$ 1.100.312,40** |
|                                                   |                 |                 |                 |                 |                 |
| **Retiradas do Sócio**                            |                 |                 |                 |                 |                 |
| Participação nos Lucros (50% do Disponível)       | R$ 678.919,28   | R$ 620.312,40   | R$ 620.312,40   | R$ 620.312,40   | R$ 620.312,40   |
| **Total Retirado pelo Sócio**                     | **R$ 678.919,28** | **R$ 620.312,40** | **R$ 620.312,40** | **R$ 620.312,40** | **R$ 620.312,40** |

**Retiradas Totais em 5 Anos (Com Dois Negócios Fechados - Cenário Esperado):**
*   **Total Retirado por PMO:** R$ 5.560.168,88
*   **Total Retirado pelo Sócio:** R$ 3.160.168,88