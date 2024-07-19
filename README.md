# Sistema de Cobrança e Estoque

Este projeto é um sistema simples de cobrança e gerenciamento de estoque, desenvolvido em Python. Ele permite que um usuário admin adicione, altere e remova produtos e suas quantidades em estoque, bem como altere o preço dos produtos. Usuários não-admin podem visualizar os produtos em estoque e realizar compras.

## Funcionalidades

- **Admin**:
  - Adicionar novos produtos ao estoque, incluindo nome, valor e quantidade.
  - Alterar o valor de produtos existentes.
  - Alterar a quantidade em estoque de produtos existentes.
  - Remover produtos do estoque quando a quantidade é menor ou igual a zero.

- **Cliente**:
  - Visualizar a lista de produtos em estoque, com preços e quantidades.
  - Realizar compras e calcular o valor total da compra.
  - Escolher se deseja incluir CPF na nota fiscal e calcular o imposto correspondente.

## Requisitos

- Python 3.x

## Instalação

1. Clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/seu-usuario/sistema-cobranca-estoque.git
