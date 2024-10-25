atletismo = set()
basquete = set()

n = int(input('Qual pe a quantidade de estudades no atletismo? '))

for e in range(n):
    estudante = input('Nme do estudante')
    atletismo.add(estudante)

n =  int(input('Qual é a quantidade de estudadntes no basquete? '))

for e in range(n):
    estudante = input('Qual o nome do aluno ?')
    basquete.add(estudante)

ambas =  basquete.intersection(atletismo)

print(ambas)