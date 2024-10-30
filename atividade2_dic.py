n = int(input('Informe a quantidade de produtos: '))

produtos = [] #criando lista vazia de produtos

for e in range(n):
    produto = {}
    produto['descrição'] = input('informe a descrição: ')
    produto ['valor'] = float(input('Informe o valor: '))
    produto['codigo de barrras '] = int(input('Informe o código de barras: '))
    produtos.append(produto)
print(produtos)