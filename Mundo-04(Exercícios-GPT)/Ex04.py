def calcula_fatorial(a):
    fatorial = 1
    for c in range(1,a+1):
        fatorial *= c
    
    return fatorial

num = int(input('Digite um número: '))
print(f'O fatorial de {num} é {calcula_fatorial(num)}')
