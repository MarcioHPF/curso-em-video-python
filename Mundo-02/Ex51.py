primeiro = int(input('Digite o primeiro termo da sua PA: '))
razao = (int(input('Digite a razão desejada para a PA: ')))
ultimo = primeiro + (9 * razao)

for c in range(primeiro, ultimo + razao, razao):
    print (c, end = " ")
print('Fim')
