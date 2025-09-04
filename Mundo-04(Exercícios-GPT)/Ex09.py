def recebe_num():
    lista = []
    while True:
        lista.append(int(input('Digite um número: ')))
        opc = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
        if opc == 'N':
            break
    return lista

def inverte_lista(lista):
    return lista[::-1]

lista = recebe_num()
print(f'Lista invertida: {inverte_lista(lista)}')
