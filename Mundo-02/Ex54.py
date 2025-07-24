from datetime import date
hoje = date.today().year
maior = menor = 0

for c in range(0,7):
    nasc = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa: '))
    if hoje - nasc >= 18:
        maior += 1
    else:
        menor += 1

print(f'Ao todo foram {menor} pessoas menores de idade e {maior} pessoas maiores de idade.')
