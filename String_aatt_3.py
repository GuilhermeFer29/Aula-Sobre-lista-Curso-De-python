# 3.  Implementar um programa que divida uma string informada pelo usuário, utilizando como delimitador o caractere espaço. 
# Por exemplo, a entrada "Eu gosto de programar" deve retornar ["Eu", "gosto", "de", "programar"].


entrada =  input(' Digite Um texto : ')

palavras = entrada.split()

for p in palavras:
    print(p)