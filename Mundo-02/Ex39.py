from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = ano - nasc
if idade == 18:
    print(f'Quem nasceu em {nasc} tem {idade} anos de idade. Alistamento obrigatório.')
elif idade > 18:
    print(f'Quem nasceu em {nasc} tem {idade} anos de idade.\nDeveria ter se alistado há {idade - 18} anos.')
elif idade > 16:
    print(f'Quem nasceu em {nasc} tem {idade} anos de idade.\nAlistamento opcional. Será obrigado a se alistar em {18 - idade} anos.')
else:
    print(f'Quem nasceu em {nasc} tem {idade} anos de idade.\nNão pode se alistar. Poderá se alistar em {16 - idade} anos e será obrigatório em {18 - idade} anos.')
