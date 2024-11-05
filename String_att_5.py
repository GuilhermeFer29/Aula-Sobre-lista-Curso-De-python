# 5. Implementar um programa que conta o número de vogais em uma string informada pelo usuário. 
# Por exemplo, a entrada "Aprender Python" deve retornar 4.

entrada = input('Informe uma String: ')

total_a = entrada.lower().count('a')
total_e = entrada.lower().count('e')
total_i = entrada.lower().count('i')
total_o = entrada.lower().count('o')
total_u = entrada.lower().count('u')

total_vogais = total_a + total_e + total_i + total_o + total_u

print(total_vogais)
