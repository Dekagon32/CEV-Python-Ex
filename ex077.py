palavras =  ('apreder', 'programar', 'linguagem', 'python', 'curso','gratis', 'estudar', 'praticar', 'trabalhar', 'mercado','programador', 'futuro')
let = ('a','e','i','o','u','A','E','I','O','U')
print('As palavras foram: ')
for c in palavras:
    print('Na palavra {} tem as vogais: '.format(c.upper()),end='')
    for f in c:
       if f in let:
           print(f,end=' ')
    print('')