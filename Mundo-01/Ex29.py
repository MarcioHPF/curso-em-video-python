vel = float(input('Digite a velocidade que em você está dirigindo: '))

if vel >= 80:
    print(f'Você ultrapassou a velocidade permitida de 80km/h e será MULTADO em R${vel * (vel - 80)}')
else: 
    print(f'Você está dentro do limite. Dirija com cuidado!')
