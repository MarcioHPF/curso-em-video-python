from time import sleep

def maior(* num):
    maior = 0
    print('-=' * 20)
    print('Analisando os valores ', end='')
    for c in range(0,len(num)):
        print(num[c], end= ' ', flush=True)
        sleep(0.5)
        if c == 1:
            maior = num[c]
        else:
            if num[c] > maior:
                maior = num[c]
    print(f'\nForam informados {len(num)} valores.')
    print(f'O maior valor foi o {maior}.')

maior(4,7,0)
maior(5)
maior(10,4,5,66,7,8)