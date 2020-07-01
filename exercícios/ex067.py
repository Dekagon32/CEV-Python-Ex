def lin():
    print('-'*30)


while True:
    lin()
    num = int(input('Digite um número: '))
    lin()
    if num < 0:
        break
    for c in range(1,11):
        print('{} Χ {:2.0f} = {}'.format(num,c,c*num))