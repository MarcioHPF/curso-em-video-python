def leiaInt(txt):
    ok = False
    num = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            num = int(n)
            ok = True
        else:
            print('Erro! Insira um número inteiro: ')
        if ok:
            break
    return num

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
