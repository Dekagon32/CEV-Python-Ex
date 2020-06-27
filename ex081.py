nums = []
five = 0
while True:
    n = int(input('Digite um número: '))
    nums.insert(0,n)
    r = str(input('Quer continuar?[S/N]: '))
    if r[0].lower() == 'n':
        break
nums.sort(reverse=True)
print('Você digitou {} valor'.format(len(nums)),end = '\n' if len(nums) == 1 else 'es\n')

print('Os valores foram: ')
for e,c in enumerate(nums):
    print(c,end = ', ' if e < len(nums) - 1 else '\n')

print('H' if 5 in nums else 'Não h', 'ouve 5 ', sep = '' ,end=' ')
if 5 in nums:
    print('{} vez'.format(nums.count(5)),end = 'es' if nums.count(5) > 1 else '\n')