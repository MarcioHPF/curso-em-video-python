def fatorial(num, show=False):
    fat = 1
    for c in range (num, 0, -1):
        fat = fat*c
        if c != 1:
            if show:
                print(f'{c} x', end=' ')
        else:
            if show:
                print(f'{c} = {fat}')
            else:
                print (fat)


fatorial(9)
