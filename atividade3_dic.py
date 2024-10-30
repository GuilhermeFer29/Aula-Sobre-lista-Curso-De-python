def inserir_contato(contatos, nome , telefone):
    contatos[ nome ] = telefone
    

def imprimir_contatos(contatos):
    for nome , telefone in contatos.items():
        print(nome,',', telefone)

# -------------------------------------------------------------------------------- #        

contatos_telefonicos  = {}


while True :

    print(' 1- Para inserir ')
    print(' 2- Para Remover ')
    print(' 3- Para Buscar ')
    print(' 4- Para Imprimir Todos ')
    print(' 0- Para Sair')

    opcao = int(input('Insira a opção desejada: '))

    if opcao == 1 :
        nome = input('Insira o nome: ')
        telefone = input('Insira o telefone: ')
        inserir_contato(contatos_telefonicos,  nome , telefone)

    elif opcao == 2:
        pass
    elif opcao == 3 : 
        pass
    elif opcao == 4 :
        imprimir_contatos(contatos_telefonicos)
    elif opcao == 0 :
        break
    else:
        print('Opção invalida')    

