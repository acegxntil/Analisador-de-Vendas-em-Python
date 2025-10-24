# 🐍 Análise Exploratória (EDA) com Python Puro: Projeto de Vendas

## 💡 O Desafio e o Objetivo

Este projeto foi criado como um exercício prático para **consolidar 100% dos fundamentos de Python** aprendidos no livro *Curso Intensivo de Python*.

O principal objetivo era provar que é possível realizar uma **Análise Exploratória de Dados (EDA) eficaz** sem depender de bibliotecas externas complexas como Pandas. Ao invés disso, utilizei apenas as estruturas e funções nativas da linguagem.

**O que este projeto faz:**

1.  Lê e processa um arquivo CSV de vendas (`vendas.csv`).
2.  Manipula os dados, convertendo strings para tipos numéricos (int/float) e lidando com a formatação (simulando a "limpeza" de dados).
3.  Calcula métricas-chave de negócio, como o Total Geral e a distribuição de vendas por Categoria.

## 🛠️ Habilidades Técnicas em Ação

Em vez de apenas listar o que foi usado, vamos focar no *como*:

* **Manipulação de Arquivos e I/O:** Uso de `open()` e loops para ler o CSV linha por linha, controlando manualmente o processo.
* **Estruturas Fundamentais:** Toda a análise e armazenamento de dados foi feita com **Listas de Dicionários**, demonstrando o domínio da base da estrutura de dados Python.
* **Agregação Lógica:** O cálculo de vendas por categoria foi feito com a **lógica de agregação pura em dicionários**, essencial para a sumarização de dados.
* **Boas Práticas:** Modularização do código em funções (`carregar_e_limpar_dados`, `analisar_vendas`, etc.) para melhor organização.
