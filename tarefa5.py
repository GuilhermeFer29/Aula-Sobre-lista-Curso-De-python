# Implementar um programa que solicite ao usuário duas listas de números. O programa deverá concatenar as listas e exibir o resultado.

n1 = int(input('Qual a quantidade de numeros na lista 1 ? '))



list1 = []




for e in range(n1):
    element1 = int(input('Qual os numeros da coluna 1 : '))

    list1.append(element1)


n2 = int(input('Qual a quantidade de numeros na lista 2? '))
list2 = []

for e in range(n2):

    element2 = int(input('Qual os numeros da coluna 2 :  '))

    list2.append(element2)

list1.extend(list2)

list1.sort()

print('Os numeros das listas é : ', list1)       
