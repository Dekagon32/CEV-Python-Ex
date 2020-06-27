obj = ('Lapis',1.75,'Borracha',2.0,'Caderno',15.9,'Estojo',25.0,'Transferidor',4.2,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.9)
print('-'*28)
print('{:^28}'.format('Listagem do Dévoli'))
print('-'*28)
for n, mat in enumerate(obj):
    if n % 2 == 0:
        print('|{:-<15}'.format(mat),end='|')
    else:
        print('R${:>8.2f}'.format(mat),end='|\n')
print('-'*28)