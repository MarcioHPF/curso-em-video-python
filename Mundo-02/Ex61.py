primeiro = int(input('Insira o primeiro termo da sua PA: '))
razao = int(input('Insira a razão da sua PA: '))
contador = 1
termo = primeiro

while contador <= 10:
    print(f'{termo}', end = ' ')
    termo +=razao
    contador += 1

print('Fim')