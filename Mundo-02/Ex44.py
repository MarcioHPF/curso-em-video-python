print(f'{'Mercadinho':-^40}')
valor = float(input('Digite o valor da compra: R$'))
print('''CONDIÇÕES DE PAGAMENTO:
[ 1 ] À vista (Dinheiro ou PIX)     
[ 2 ] À vista (Cartão)      
[ 3 ] Parcelado no cartão (2x)     
[ 4 ] Parcelado no cartão (3x ou mais)          
''')
opc = int(input('Digite a opção desejada: '))

if opc == 1:
    print(f'A compra de R${valor:.2f} tem 10% de desconto e sai por {valor * 0.9:.2f}')
elif opc == 2:
    print(f'A compra de R${valor:.2f} tem 5% de desconto e sai por {valor * 0.95:.2f}')
elif opc == 3:
    print(f'O valor final da compra é de 2x de R${valor/2:.2f}')
elif opc == 4:
    print(f'A compra de R${valor:.2f} tem 20% de juros.')
    parcelas = int(input('Deseja pagar em quantas parcelas? '))
    print(f'O valor total é de {parcelas}x de R${(valor * 1.2)/parcelas:.2f}')
