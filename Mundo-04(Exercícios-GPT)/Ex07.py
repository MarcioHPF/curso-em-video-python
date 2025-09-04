def recebe_num():
    lista = []
    while True:
        lista.append(int(input('Digite um número: ')))
        opc = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
        if opc == 'N':
            break
    return lista

def conta_impar_par(lista):
    par = impar = 0
    for c in lista:
        if c % 2 == 0:
            par += 1
        else:
            impar += 1
    
    return par,impar

numeros = recebe_num()
pares, impares = conta_impar_par(numeros)
print('-' * 15)
print(f'Pares: {pares}\nÍmpares: {impares}')
