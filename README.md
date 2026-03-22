# Energia Global

## 1. Integrantes
* Jônatas Vieira (https://github.com/jonatasssv)
* Igor martins Lima (https://github.com/igor8472)
* Antônio Dorneles (https://github.com/Antonio-Dorneles)

## 2. Objetivo da Análise
O objetivo desta análise é explorar a capacidade de geração de energia mundial, comparando a presença de fontes renováveis versus combustíveis fósseis, permitindo visualizar quais regiões lideram a transição para energias limpas.

## 3. Base de Dados
* **Fonte:** Global Power Plant Database - Kaggle
* **Descrição:** Este conjunto de dados contém informações sobre aproximadamente 35.000 usinas de energia em 167 países. Ele inclui dados sobre a localização (latitude/longitude), tipo de combustível utilizado (Fuel Type), capacidade de geração em Megawatts (MW) e o histórico de produção

## 4. Planejamento de Tarefas e Cronograma
| Tarefa | Responsável | Prazo | Status |
| :--- | :--- | :--- | :--- |
| Estrutura do Git | Jônatas Vieira | 19/03 | Concluído |
| Extração de Dados | Jônatas Vieira | 19/03 | Concluído |
| Limpeza (Pandas) | Igor Lima | 22/03 | Pendente |
| Dashboard | Integrante Z | 05/04 | Pendente |

## 5. Transformações Pretendidas
Descreva o que vocês vão fazer com os dados brutos:
* Limpeza de valores nulos.
* Tratamento de Nulos: Decidir o que fazer com usinas que não têm o valor de geração de energia preenchido.
* Cálculo de médias.

## 6. Ideia Inicial do Dashboard
* **Métricas:** Preço médio, menor preço encontrado, inflação por categoria.
* **Visualizações:** Gráfico de barras comparativo, linha do tempo de preços, filtros por marca ou região.
* **Mapa Mundial:** Mostrando a localização das usinas
* **Ferramentas:** Python, Streamlit, Pandas
