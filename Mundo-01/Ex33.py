a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

maior = a
menor = a

if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

print (f'O maior número é {maior} e o menor é {menor}')
