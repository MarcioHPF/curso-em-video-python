total = contmais = cont = 0
barato = ' '
print('-' * 30)
print(f'{'MERCADINHO':^30}')
print('-' * 30)

while True:
    print('-' * 30)
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: '))
    cont += 1
    total += preco

    if preco > 1000:
        contmais += 1

    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Continuar[S/N]? ')).strip().upper()[0]  
    if continua == 'N':
        break

print(f'{'FIM DO PROGRAMA':-^30}')
print(f'O total do valor da compra é R${total:.2f}')
print(f'Foram comprados {contmais} produtos por mais de R$1000,00')
print(f'O produto mais barato foi o(a) {barato}')
    