ex = str(input('Digite sua expressão: '))
es = []
di = []
h = True
for sim in ex:
    if sim == '(':
        es.append('(')
    if sim == ')':
        if len(es) > 0:
            es.pop()
        else:
            h = False
            break

print('Errado' if h == False else 'Certo')