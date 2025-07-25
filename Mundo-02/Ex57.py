sexo = input('Informe o seu gênero[M/F]: ').upper()
while True:
    if sexo not in 'MF':
        sexo = input(f'Valor inválido! Informe o seu gênero: ').upper()
    else:
        break
print ('Gênero masculino registrado.') if sexo == 'M' else print ('Gênero feminino registrado.') 