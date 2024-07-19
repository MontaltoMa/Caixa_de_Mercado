'''
A ideia é montar um sistema de cobrança de caixa e stock
1 - Tera uma lista de produtos e outra lista com seus valores e quantidade em estoque
2 - Criar uma condição onde ira identificar se o usuario é o admin, se for pode alterar os valores dos produtos e sua quantidade em estoque
3 - Se não for o admin escolher quais produtos vai comprar, sua quantidade e calcular o valor final da compra
'''
from time import sleep

def remover_produto(indice):
    '''Remove o produto das listas.'''
    produto_removido = produtos.pop(indice)
    quantidade.pop(indice)
    valores.pop(indice)
    print(f'O produto {produto_removido} foi removido do estoque.')

usuario = 'admin'
produtos = ['doritos', 'coca-cola', 'pao', 'leite', 'arroz']
quantidade = [2, 10, 15, 5, 3]
valores = [5.50, 3.50, 1.0, 2.5, 35.0]

entrada = str(input('Digite seu nome: \n')).strip().lower()

while True:

    if entrada == usuario:
        pergunta = int(input('''Digite o que gostaria de fazer:
                             1 - Adicionar novos produtos no estoque seus valores e quantidade.
                             2 - Alterar o valor de um produto.
                             3 - Alterar a quantidade em estoque de um produto.
                             4 - Sair do sistema.\n'''))
        print('Processando sua entrada...')
        sleep(1)
        try:
            if pergunta == 1:

                # Adicionando novos produtos no estoque, seus valores e quantidade
                novo_produto = str(input('Digite o nome do novo produto: \n')).strip().lower()
                
                if novo_produto == '':
                    print('Nome do produto não pode estar vazio.')
                    continue
                if novo_produto in produtos:
                    print('Produto já existente em estoque...')
                    continue

                try:
                    novo_valor = float(input('Digite o valor deste produto: \nR$'))
                    if novo_valor <= 0:
                        print('O valor não pode ser zero ou negativo.')
                        continue
                except ValueError:
                    print('Valor inválido.')
                    continue

                try:
                    nova_quantidade = int(input('Digite a quantidade em estoque: \n'))
                    if nova_quantidade <= 0:
                        print('A quantidade não pode ser zero ou negativo')
                        continue
                except ValueError:
                    print('Quantidade inválido.')
                    continue

                produtos.append(novo_produto)
                valores.append(novo_valor)
                quantidade.append(nova_quantidade)

            elif pergunta == 2:

                # Alterar valor de um produto específico
                produto = str(input('Digite o nome do produto que tera seu valor alterado: \n')).strip().lower()

                if produto in produtos:
                    indice = produtos.index(produto)
                    try:
                        novo_valor = float(input('Digite o novo valor deste produto: \nR$'))
                        if novo_valor <= 0:
                            print('O valor deve ser positivo.')
                            continue
                    except ValueError:
                        print('Valor inválido.')
                        continue
                    valores[indice] = novo_valor
                else:
                    print('Produto não encontrado.')

            elif pergunta == 3:

                # Alterar quantidade de um produto específico
                produto = str(input('Digite o nome do produto que tera seu estoque alterado: \n')).strip().lower()

                if produto in produtos:
                    indice = produtos.index(produto)
                    try:
                        nova_quantidade = int(input('Digite a quantidade em estoque deste produto: \n'))
                        if nova_quantidade < 0:
                            print('A quantidade não pode ser negativa.')
                            continue
                    except ValueError:
                        print('Valor inválido.')
                        continue
                    quantidade[indice] = nova_quantidade

                    # Removendo produto se a quantidade for menor ou igual a zero
                    if quantidade[indice] <= 0:
                        remover_produto(indice)
                else:
                    print('Produto não encontrado.')

            elif pergunta == 4:
                # Sair do loop
                break
        except ValueError:
            print('Digite uma das opções acima.')

        # Exibir os produtos, valores e quantidades atualizados
        print('Produtos: ', produtos)
        print('Valores: R$', valores)
        print('Quantidades: ', quantidade)
        

    else:
        # Menu cliente
        print('Lista de produtos em estoque:\n')
        for i, produto in enumerate(produtos):
            print(f'{produto} - R${valores[i]:.2f} - Estoque: {quantidade[i]} unidades')
        print()

        carrinho = []
        total_compra = 0

        while True:

            produto = str(input('Digite o produto que deseja comprar, ou digite "sair" para sair do sistema: \n')).strip().lower()

            if produto == 'sair':
                break
            if produto in produtos:
                indice = produtos.index(produto)
                quantidade_desejada = int(input('Quantas unidades deseja comprar? \n'))
                if quantidade_desejada <= quantidade[indice]:
                    quantidade[indice] -= quantidade_desejada
                    total_compra += valores[indice] * quantidade_desejada
                    carrinho.append((produto, quantidade_desejada, valores[indice] * quantidade_desejada))
                else:
                    print('Quantidade em estoque insuficiente!\n')
            else:
                print('Produto não encontrado!\n')
                
        # Exibir o resumo da compra
        print('Resumo da compra...\n')
        sleep(1)
        for item in carrinho:
            print(f'{item[1]} unidade(s) de {item[0]} ficou:\n R${item[2]:.2f}')

        nota_fiscal = str(input('Deseja CPF na nota fiscal? [S/N]\n')).strip().upper()

        imposto = (total_compra * 22) / 100

        if nota_fiscal == 'N':
            print(f'''---Nota fiscal Paulista---
Obrigado por comprar no mercado python.
            
CPF: NAO INFORMADO
O total da sua compra ficou R${total_compra:.2f}
O valor do imposto sobre sua compra foi de aproximadamente: R${imposto:.2f}''')
        else:
            while True:
                
                cpf = int(input('Digite sem CPF sem usar (. e -):\n'))
                
                if len(cpf) == 11 and cpf.isdigit():
                    break
                else:
                    print('CPF inválido. Por favor, digite um CPF válido com 11 dígitos.')

            print(f'''---Nota fiscal Paulista---
Obrigado por comprar no mercado python.
            
CPF:{cpf}.
O total da sua compra ficou R${total_compra:.2f}
O valor do imposto sobre sua compra foi de aproximadamente: R${imposto:.2f}''')
        break