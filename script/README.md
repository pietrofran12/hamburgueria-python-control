# 🍔 Sistema de Controle e Pedidos - Hamburgueria Python

Este é um sistema de automação para painel de cozinha e gerenciamento de estoque desenvolvido em **Python**. O projeto foi criado com o objetivo de consolidar conceitos fundamentais de lógica de programação, manipulação de coleções de dados estruturados (matrizes) e controle de fluxo.

## 🚀 Funcionalidades do Sistema

*   **Alerta Automático de Insumos:** Assim que o sistema inicia, ele faz uma varredura completa na matriz de estoque e emite alertas visuais para qualquer ingrediente que esteja abaixo de 5 unidades.
*   **Gerenciamento de Fila de Clientes:** Registra a entrada de clientes na fila de atendimento, aplicando formatação rigorosa de strings (`.strip().lower().capitalize()`) para evitar duplicidade.
*   **Mecanismo de Checagem Antecipada (Sinalizadores):** Antes de confirmar qualquer pedido e alterar o estoque, o sistema valida se há insumos disponíveis, garantindo que o estoque nunca fique negativo.
*   **Baixa Dinâmica em Matriz:** Atualiza em tempo real as quantidades de matéria-prima consumidas (Pão, Carne, Queijo, Refrigerante) acessando diretamente os índices bidimensionais `[linha][coluna]`.
*   **Lógica de Manufatura Integrada:** Simula o fluxo real de uma linha de produção através do incremento e decremento sequencial no produto final transformado.

## 🛠️ Tecnologias e Conceitos Aplicados

*   **Controle de Loops:** Estruturas dinâmicas com `while True`, loops infinitos controlados por interrupções (`break`) e varreduras com `for`.
*   **Estruturas de Decisão Avançadas:** Combinação de `match/case` com condições compostas (`if / and`).
*   **Coleções de Dados (Listas e Matrizes):** Manipulação dinâmica de arrays estruturados em linhas e colunas, além de controle de tamanho com `len()` e inserções com `.append()`.
*   **Clean Code:** Código limpo e otimizado, evitando repetições desnecessárias e utilizando operadores simplificados de atribuição como `-=`.

## 📁 Estrutura do Repositório

```text
hamburgueria-python-control/
└── src/
    ├── painel_pedidos.py  # Arquivo principal com o código-fonte do sistema
    └── README.md          # Documentação do projeto
```

## 🧠 Aprendizado Desenvolvido
Este projeto marcou a transição do desenvolvimento puramente sequencial para a construção de arquiteturas lógicas resilientes, preparando a base conceitual para o estudo de novos métodos de listas (como `.pop()`, `.insert()` e `.clear()`) e a implementação futura de um sistema de Carrinho de Compras.
