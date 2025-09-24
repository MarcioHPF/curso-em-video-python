def cria_lista():
    lista = []
    while True:
        try:
            lista.append(int(input('Digite um número: ')))
        except(ValueError):
            print('Valor inválido!')
            continue
        opc = str(input('Deseja continuar?[S/N] ')).strip().capitalize()[0]
        if opc == 'N':
            return lista
        
def confere_numero(numeros):
    unicos = []
    for numero in numeros:
        if numero not in unicos:
            unicos.append(numero) 
    return unicos

lista = cria_lista()
print(confere_numero(lista))
