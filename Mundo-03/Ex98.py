from time import sleep

def contador(inicio, fim, passo):
    print('-' * 50)
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}:')
    sleep(1.5)
    if inicio < fim:
        if passo > 0:
            for c in range(inicio,fim+1, passo):
                print (c, end=' ', flush= True)
                sleep(0.75)
            print('Fim!')
        else:
            print(f'Impossível contar de {inicio} até {fim} com valores negativos no passo')
    elif inicio > fim and passo > 0:
        for c in range(inicio,fim+1, -passo):
            print (c, end=' ', flush= True)
            sleep(0.75)
    else:
        for c in range(inicio,fim+1, passo):
            print (c, end=' ', flush= True)
            sleep(0.75)
        print('Fim!')

contador(1,10,1)
contador(10, 0, 2)
print('-_' * 25)
print('Agora é a contagem personalizada!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Quanto em quanto: '))
contador(ini, fim, passo)
