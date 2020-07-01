num = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
c = 11
con = 1
quantidade = c - 1
while c >= 0:
    while con != c:
        print(f'{num}',end=' > ' if con != c - 1 else ' > PAUSE\n')
        num += raz
        con += 1
    con = 1
    c = int(input('Mais quantos termos? ')) + 1
    quantidade += c
print(f'FIM!!!\nForam {quantidade} vezes.')