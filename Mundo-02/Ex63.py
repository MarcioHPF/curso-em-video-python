qtde_termos = int(input('Digite a quantidade de termos desejados: '))
t1 = 0
t2 = 1
cont = 3
print (f'{t1} > {t2}', end= ' ')
while cont <= qtde_termos:
    termo = t1 + t2
    print(f'> {termo}', end= ' ')
    t1 = t2
    t2 = termo
    cont+=1
print('> FIM')
