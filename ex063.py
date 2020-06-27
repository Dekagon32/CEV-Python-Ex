termos = ['',1,2]
tm = []
num = int(input('Quantos termos? '))

for c in range(3,num+1):
    termos.append(termos[len(termos)-1]+termos[len(termos)-2])

for c in range(1,len(termos)):
    tm.append(str(termos[c]))
    tm.append(' > ' if c < len(termos) - 1 else ' > Fim!')
junto = ' '.join(tm)
print('Os {} termos são: {}'.format(num,junto))