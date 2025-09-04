def recebe_num():
    lista = []
    while True:
        lista.append(int(input('Digite um número: ')))
        opc = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
        if opc == 'N':
            break
    return lista

def conta_numeros(lista):
    freq = {}
    for num in lista:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    mais_freq = max(freq, key=freq.get)
    contagem = freq[mais_freq]

    print(f'O número que aparece mais vezes é o {mais_freq} que apareceu {contagem} vezes.')

numeros = recebe_num()
conta_numeros(numeros)
