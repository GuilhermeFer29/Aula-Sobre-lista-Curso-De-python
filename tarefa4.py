# Implementar um programa que, a partir do usuário, receba um conjunto de nomes de pessoas e os apresente em ordem alfabética.
#  O usuário deverá informar inicialmente qual é a quantidade de nomes.

n = int(input('Qual é a quantidade De Nomes ? '))
list =[]

for e in range(n):

    name = input('Qual nome a ser adicionado: ')
    list.append(name)
list.sort()
print('Os nomes na sequencia Sao esses : ',list ) 