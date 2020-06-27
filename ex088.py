from random import randint
from time import sleep as s
qj = int(input('Digite a quantidade de jogos: '))
Jogos = []
nums = []
b = 0
couint = 0
for c in range(1,qj+1):
    print('Jogo {}: '.format(c),end=' ')
    for c in range(0,6):
        while True:
            couint += 1
            b = randint(1, 60)
            if b not in nums and couint > 1:
                nums.append(b)
                break
    print(nums)
    s(0.4)
    Jogos.append(nums[:])
    nums.clear()
print('{:-<31}'.format('Good Luck!!!'))
