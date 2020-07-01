from random import choice,randint
import time
contagem = 0
alunos_l = []
aluno = []
note = []
numa = 1000
sleeper = 0
nomes_alunos = ['Alice','Sofia','Beatriz','Laura','Júlia','Victor','Devilyn','Artur','Gabriel','Guilherme','Pedro','Kevin','Eliel','Frajola']
sobrenomes_alunos = ['Silva','Souza','de Oliveira','Santos','Rodrigues','Nascimento','Lima','Carvalho','Gomes','Alves','Marra','Elize','Thiago','Marques','Garcia','Gribos']
for al in range(0,numa):
    aluno.append(choice(nomes_alunos)+' '+choice(sobrenomes_alunos))
    note.append(randint(4,10))
    note.append(randint(4,10))
    note.append(randint(4,10))
    note.append(randint(4,10))
    aluno.append(note[:])
    alunos_l.append(aluno[:])
    aluno.clear()
    note.clear()
print('{:<2} |{:<23}| {:<6} | {:<6} | {:<6} | {:<6} | {:<6} |'.format('Nº','NOME','NOTA 1','NOTA 2','NOTA 3','NOTA 4','MÉDIA'))
for alun in alunos_l:
    contagem += 1
                                           
    print('{:<2} |{:<23}| {:^6} | {:^6} | {:^6} | {:^6} | {:^6} |'.format(contagem,alun[0],alun[1][0],alun[1][1],alun[1][2],alun[1][3],(alun[1][0]+alun[1][1]+alun[1][2]+alun[1][3])/4))
    time.sleep(sleeper)
continuarug = input('Digite <enter> para finalizar...')
