def cria_matriz():
    matriz = [[0,0,0], [0,0,0], [0,0,0]]
    somas = [0, 0, 0]

    for linha in range(0,3):
        for coluna in range(0,3):
            while True:
                try:    
                    matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
                    break
                except(ValueError):
                    print('Valor inválido! Digite um número inteiro.')
    
    print('-'*25)
    print('Matriz montada: \n')

    for linha in matriz:
        for valor in linha:
            print(f'{valor:^5}', end='')
        print()
       
    for linha in range(3):
        for coluna in range(3):
            somas[coluna] += matriz[linha][coluna]

    print()
    for i, soma in enumerate(somas):
        print(f"Soma da coluna {i}: {soma}")

cria_matriz()
