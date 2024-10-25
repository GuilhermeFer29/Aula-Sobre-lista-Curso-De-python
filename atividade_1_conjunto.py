# 1. Implementar um programa que verifique quais estudantes praticam simultaneamente atletismo e basquete. 
# O usuário deve informar os estudantes de atletismo e, depois, os de basquete. 
# O programa deve exibir os alunos que participam de ambas as atividades.

option = int(input('Selecione a Opçao A seguir : 1 - Atletismo  2- Basquete '))

i = 0 

athletics_conj = set()
basktball_conj = set()

if option == 1 :
    student_athletics = input('Qual os nomes dos studantes de Atletismo: ')
    if student_athletics != 'sair':
        while student_athletics != 'sair'  :
            
            print('Digite "sair" para Finalizar ')
            athletics_conj.add(student_athletics)
            student_athletics = input('Qual os nomes dos studantes de Atletismo: ')

            if student_athletics == 'sair':
                break

        
        
if option == 2 :
    student_basktball = input('Qual os nomes dos studantes de Basquete: ')
    while student_basktball != 'sair' :
        print('Digite sair para Sair ')
        basktball_conj.add(student_basktball)
        student_basktball = input('Qual os nomes dos studantes de Basquete: ')
        if student_athletics == 'sair':
            break

       


