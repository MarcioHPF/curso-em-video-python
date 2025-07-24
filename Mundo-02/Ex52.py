num = int(input('Digite um número: '))
cont = 0

for c in range(1, num + 1):
   if num % c == 0:
      print(f'\033[32m{c}', end = ' ')
      cont+= 1
   else:
      print(f'\033[31m{c}', end= ' ')

print(f'\n\033[mO número {num} é divisível por {cont} números') 

if cont == 2:
    print('Portanto, ele é considerado um número PRIMO.')
else:
   print(f'Portanto, ele é considerado um número COMPOSTO.')
