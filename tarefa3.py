# 3. Implementar um programa que verifique se um número está presente em uma lista de números informados pelo usuário. 
# O programa deve solicitar inicialmente a lista de números e depois o número a ser buscado

n = int(input('Qual é a quantidade De elemntos? '))
list =[]

for e in range(n):
    num = int(input('Informe um numero'))

    list.append(num)

chave = int(input('Informe o numero a ser buscado '))

if chave in list :
    print('Numero encontrado')
else :
    print('Numero Encontrado')    