def recebe_positivo ():
    while True:
        num = int(input('Digite um número positivo: '))
        if num > 0:
            break
        else:
            print('Número inválido!')
    return num

def soma_tudo (num):
    # return sum(int(d) for d in str(num)) -> Faz tudo que a função faz em uma linha
    soma = 0
    for c in str(num):
        soma += int(c)
    
    return soma

numero = recebe_positivo()
print(soma_tudo(numero))
