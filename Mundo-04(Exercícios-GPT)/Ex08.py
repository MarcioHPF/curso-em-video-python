def fibonacci(max):
    n1 = 0
    n2 = 1
    cont = 3
    print(n1, ',', n2, end= ' ')
    while cont <= max:
        n3 = n1 + n2
        print(',', n3, end= ' ')
        n1 = n2
        n2 = n3
        cont += 1

fibonacci(int(input('Digite a quantidade de termos da sequência: ')))
print()
