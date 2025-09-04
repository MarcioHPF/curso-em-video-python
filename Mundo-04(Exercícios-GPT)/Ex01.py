def recebeNum():
    lista = []
    while True:
        lista.append(int(input('Digite um número: ')))
        opc = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
        if opc == 'N':
            break
    return lista
def calculaPar(numeros):
    # return [num for num in numeros if num % 2 == 0] -> Faz a mesma coisa que o código abaixo inteiro com uma só linha.
    par = []
    for num in numeros:
        if num % 2 == 0:
            par.append(num)

    return par

lista = recebeNum()
print(calculaPar(lista))
