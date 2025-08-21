def leiaInt(txt):
    num = 0
    while True:
        try:
            n = int(input(txt))
        except (TypeError,ValueError):
            print(f'\033[31mERRO! Digite um número inteiro válido! \033[m')
            continue
        else:   
            return n
def leiaFloat(txt):
    num = 0
    while True:
        try:
            n = float(input(txt))
        except (TypeError, ValueError):
            print(f'\033[31mERRO! Digite um  valor real válido!\033[m')
            continue
        else:
            return n
        

n = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n} e o número real {f}')