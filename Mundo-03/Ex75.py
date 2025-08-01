num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'Você digitou os números {num}')
print(f'O número 9 foi digitado {num.count(9)} vez(es).')
if 3 in num:
   print(f'O número 3 foi digitado na {num.index(3) + 1}ª posição.')
else:
   print('O número 3 não foi digitado.')
print('Os valores pares digitados foram ', end='')

for c in num:
   if c % 2 == 0:
    print(c, end=' ')
   