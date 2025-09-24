def cria_matriz():
    matriz = [[0,0,0], [0,0,0], [0,0,0]]
    soma_par =  soma3 = maior = 0


    for linha in range(0,3):
        for coluna in range(0,3):
            while True:
                try:    
                    matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
                    break
                except(ValueError):
                    print('Valor inválido! Digite um número inteiro.')
       
    soma_par = sum(valor for linha in matriz for valor in linha if valor % 2 == 0)
    soma3 = sum(linha[2] for linha in matriz)
    maior = max(matriz[1])

    print('-'*25)
    print('Matriz montada: \n')    
    for linha in matriz:
        for valor in linha:
            print(f'{valor:^5}', end='')
        print()
    print(f'\nSoma de todos os valores pares da matriz: {soma_par}')
    print(f'Soma de todos os valores da terceira coluna: {soma3}')
    print(f'Maior valor da segunda linha: {maior}')

cria_matriz()
