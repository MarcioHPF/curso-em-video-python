maior = homem = menina = 0
print('-' * 30)
print(f'{'Cadastro de pessoas':^30}')
print('-' * 30)

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Gênero[F/M]: ')).strip().upper()[0]
    
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    print('-' * 30)
    if sexo == 'M':
        homem += 1
    else:
        if idade < 20:
            menina += 1
    if idade > 18:
        maior += 1
    if opc == 'N':
        break

print(f'Total de pessoa com mais de 18 anos: {maior},')
print(f'Ao todo temos {homem} homens cadastrado(s),')
print(f'Ao todo temos {menina} mulheres com menos de 20 anos.')