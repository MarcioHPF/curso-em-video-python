lista = []

for c in range(1,6):
    num = int(input('Digite um número: '))
    if c == 1 or num > lista[-1]:
        lista.append(num)
        
    elif num < min(lista):
        lista.insert(0,num)