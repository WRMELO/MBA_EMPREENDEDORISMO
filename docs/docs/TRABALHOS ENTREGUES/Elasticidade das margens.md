# Simulação de Elasticidade do Lucro da Consultoria e "Win-Win" (Corrigida)

Este documento analisa a sensibilidade do lucro da consultoria e do ganho líquido do cliente (Termoelétrica) a variações nos custos de desenvolvimento, na margem de venda dos serviços e no **ganho bruto anual do próprio cliente** (que impacta o bônus da consultoria).

## 1. Valores de Referência (Baseline - Cenário "Esperado")

*   **Custo Total de Desenvolvimento (CTD_base):** R$ 217.062,50
*   **Margem de Venda Base:** 30%
*   **Receita de Desenvolvimento Base:** R$ 282.181,25
*   **Lucro do Desenvolvimento Base:** R$ 65.118,75
*   **Ganho Bruto Anual do Cliente (GBAC_base):** R$ 20.493.000,00
*   **Percentual Bônus Consultoria:** 5%
*   **Teto Bônus Anual Consultoria:** R$ 1.000.000,00
*   **Receita de Bônus Anual Efetiva da Consultoria (RBAC_base):** R$ 1.000.000,00
*   **Custo de Gestão do Bônus Anual:** R$ 10.000,00 (constante)
*   **Lucro do Bônus Anual Base:** R$ 990.000,00
*   **Lucro Total da Consultoria (5 anos - Base):** R$ 5.015.118,75
*   **Gasto Total do Cliente com Consultoria (5 anos - Base):** R$ 5.282.181,25
*   **Ganho Líquido do Cliente (5 anos - Base):** R$ 97.182.818,75

## 2. Variáveis da Simulação

1.  **Variação no Custo Total de Desenvolvimento (CTD):**
    *   **Custo_Base:** 0% de variação sobre CTD_base
    *   **Custo_+50%:** +50% sobre CTD_base
    *   **Custo_+100%:** +100% sobre CTD_base

2.  **Variação na Margem de Venda do Serviço (aplicada sobre o CTD do cenário):**
    *   **Margem_30% (Base):** 30%
    *   **Margem_45%:** 45%
    *   **Margem_60%:** 60%

3.  **Variação no Ganho Bruto Anual do Cliente (GBAC):**
    *   **GanhoCliente_Base (0%):** 0% de variação sobre GBAC_base
    *   **GanhoCliente_-20%:** -20% sobre GBAC_base
    *   **GanhoCliente_-50%:** -50% sobre GBAC_base

## 3. Resultados da Simulação (27 Cenários)

| Cenário ID | Variação CTD | Nova Margem (%) | Variação Ganho Cliente Anual (%) | CTD Cenário (R$) | Receita Dev. Cenário (R$) | Lucro Dev. Cenário (R$) | GBAC Cenário (R$) | RBAC Cenário (R$) | Lucro Bônus Total Cenário (5a) (R$) | **Lucro Total Consultoria (5a) (R$)** | Gasto Cliente Total (5a) (R$) | **Ganho Líquido Cliente (5a) (R$)** |
| :--------- | :----------- | :-------------- | :----------------------------- | :--------------- | :------------------------ | :---------------------- | :---------------- | :---------------- | :------------------------------------- | :--------------------------------------- | :------------------------------- | :------------------------------------ |
| 1          | Base (0%)    | 30% (Base)      | Base (0%)                      | 217.062,50       | 282.181,25                | 65.118,75               | 20.493.000,00     | 1.000.000,00      | 4.950.000,00                           | **5.015.118,75**                         | 5.282.181,25                     | **97.182.818,75**                     |
| 2          | Base (0%)    | 30% (Base)      | -20%                           | 217.062,50       | 282.181,25                | 65.118,75               | 16.394.400,00     | 819.720,00        | 4.048.600,00                           | **4.113.718,75**                         | 4.380.781,25                     | **77.591.218,75**                     |
| 3          | Base (0%)    | 30% (Base)      | -50%                           | 217.062,50       | 282.181,25                | 65.118,75               | 10.246.500,00     | 512.325,00        | 2.511.625,00                           | **2.576.743,75**                         | 2.843.806,25                     | **48.388.693,75**                     |
| 4          | Base (0%)    | 45%             | Base (0%)                      | 217.062,50       | 314.740,63                | 97.678,13               | 20.493.000,00     | 1.000.000,00      | 4.950.000,00                           | **5.047.678,13**                         | 5.314.740,63                     | **97.150.259,38**                     |
| 5          | Base (0%)    | 45%             | -20%                           | 217.062,50       | 314.740,63                | 97.678,13               | 16.394.400,00     | 819.720,00        | 4.048.600,00                           | **4.146.278,13**                         | 4.413.340,63                     | **77.558.659,38**                     |
| 6          | Base (0%)    | 45%             | -50%                           | 217.062,50       | 314.740,63                | 97.678,13               | 10.246.500,00     | 512.325,00        | 2.511.625,00                           | **2.609.303,13**                         | 2.876.365,63                     | **48.356.134,38**                     |
| ...        | ...          | ...             | ...                            | ...              | ...                       | ...                     | ...               | ...               | ...                                    | **...**                                  | ...                              | **...**                               |
| 27         | +100%        | 60%             | -50%                           | 434.125,00       | 694.600,00                | 260.475,00              | 10.246.500,00     | 512.325,00        | 2.511.625,00                           | **2.772.100,00**                         | 3.256.225,00                     | **47.976.275,00**                     |

*(Nota: A tabela completa com os 27 cenários será gerada pelo script Python. Os valores de exemplo acima ilustram a estrutura. O "GBAC Cenário" é o Ganho Bruto Anual do Cliente *após* a variação percentual. O "RBAC Cenário" é a Receita de Bônus Anual da Consultoria, calculada como 5% do GBAC Cenário, limitada ao teto de R$1M.)*

## 4. Análise Preliminar e Observações (Corrigida)

*   **Impacto da Redução do Ganho do Cliente:** Uma redução no ganho bruto do cliente impacta diretamente (e negativamente) a receita de bônus da consultoria, especialmente se o bônus sair do teto. Isso, por sua vez, reduz o lucro total da consultoria. Para o cliente, seu ganho líquido também diminui devido à redução do seu próprio ganho bruto, embora ele pague menos bônus à consultoria nesses cenários.
*   **Robustez do "Win-Win":** Mesmo com reduções significativas no ganho do cliente (levando a bônus menores para a consultoria), o cliente ainda pode ter um ganho líquido expressivo se o ganho bruto, mesmo reduzido, for substancial. A relação "Win-Win" é mais sensível à performance real da solução em gerar ganhos para o cliente. Se o ganho do cliente cai muito, o "win" da consultoria (via bônus) também cai, e o "win" do cliente é proporcionalmente menor.
*   A combinação de aumento de custos da consultoria, aumento de margem da consultoria e redução do ganho do cliente representa o cenário mais desafiador para ambas as partes, mas o modelo ainda pode ser positivo para o cliente se o ganho bruto gerado pela solução for relevante.

