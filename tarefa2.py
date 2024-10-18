# Implementar um programa que, a partir do usuário, receba um conjunto de números e troque o primeiro e o último número informados de posição. 
# O usuário deverá informar inicialmente qual é a quantidade de números da lista.

n = int(input('Qual a quantidade de Elementos'))
list = []

for e in range(n):

    num = int(input('Informe um numero'))

    list.append(num)
troca = list[-1]
list[-1] = list[0] 
list[ 0 ] = troca   