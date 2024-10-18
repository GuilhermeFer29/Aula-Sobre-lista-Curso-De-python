# 1. Implementar um programa que permita ao usuário adicionar elementos em uma lista até que ele decida parar. 
# Em seguida, o programa deve exibir a lista resultante e a quantidade de elementos.

input_list = None
add_list = []

while input_list != 'fim' :   
    input_list = input('Adicione um Elemento a lista = ')
    if input_list.lower() != 'fim':
        
        add_list.append(input_list)

print(add_list)
print(len(add_list))