valores  = [ 5, 8, 10, 3]

dobro_valores = []

for num in valores:
    if num % 2 == 0 :
        dobro = num * 2 
        dobro_valores.append(dobro)

print(dobro_valores)