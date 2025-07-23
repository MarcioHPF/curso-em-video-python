from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - nasc

print(f'O atleta tem {idade} anos de idade!')
if idade <= 9:
    print('O atleta está classificado como MIRIM')
elif idade > 9 and idade <= 14:
    print('O atleta está classificado como INFANTIL')
elif idade > 14 and idade <= 19:
    print('O atleta está classificado como JUNIOR')
elif idade > 19 and idade <= 25:
    print('O atleta está classificado como SÊNIOR')
else:
    print('O atleta está classificado como MASTER')
