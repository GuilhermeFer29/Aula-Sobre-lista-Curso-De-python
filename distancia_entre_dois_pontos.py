import math

def calcular_distancia(p1, p2):
   
    dist = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2 )

    return dist

x1 = float(input('Informe O valor de x1 : '))

y1 = float(input('Informe O valor de y1 : '))

z1 = float(input('Informe O valor de z1 : '))

ponto1 = (x1, y1, z1)

x2 = float(input('Informe O valor de x2 : '))

y2 = float(input('Informe O valor de y2 : '))

z2 = float(input('Informe O valor de z2 : '))

ponto2 = (x2, y2, z2)


distancia = calcular_distancia(ponto1, ponto2)

print(distancia)