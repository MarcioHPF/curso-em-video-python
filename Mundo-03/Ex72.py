numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
dezenas = ('vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')

while True:
    num = int(input('Insira um número de 0 a 99: '))
    if num >= 0 and num <= 99:
        break
    else: 
        print('Valor fora do limite!', end=' ')

if num < 20:
    print(f'Você digitou o número {numeros[num]}')
else:
    dezena = num // 10
    unidade = num % 10
    print(f'Você digitou o número {dezenas[dezena-2]} e {numeros[unidade]}')
