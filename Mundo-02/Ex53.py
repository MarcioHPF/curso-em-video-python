frase = str(input('Digite uma frase: ')).lower().strip().replace(' ', '')
inverso = ''

for c in range(len(frase) -1, -1, -1):
    inverso += frase[c]

print(f'A frase {frase} ao contrário é igual a {inverso}')
if frase == inverso:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')
