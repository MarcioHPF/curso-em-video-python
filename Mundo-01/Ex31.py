km = float(input('Digite a distância da viagem: '))

print(f'Você está fazendo uma viagem de {km}km.')
print (f'O valor da passagem é R${km * 0.5:.2f}') if km <= 200 else print(f'O valor da passagem é R${km * 0.45:.2f}')
