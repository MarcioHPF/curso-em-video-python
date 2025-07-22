val_casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o salário do comprador: '))
tempo = int(input('Digite em quantos anos o comprador irá pagar o empréstimo: '))
prest = val_casa / (tempo * 12)

if prest  > sal * 0.3:
    print(f'Para pagar uma casa de R${val_casa:.2f} em {tempo} anos, o comprador pagará R${prest:.2f}. Empréstimo NEGADO')
else:
    print(f'Para pagar uma casa de R${val_casa:.2f} em {tempo} anos, o comprador pagará R${prest:.2f}. Empréstimo APROVADO!')
