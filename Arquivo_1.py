arquivo = open('C:\\Users\\Aluno\\Desktop\\saudacao.txt','w')

for e in range(10,-1,-1):
    
    arquivo.write(str(e)+'\n')

arquivo.close()