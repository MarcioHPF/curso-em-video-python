def confere_num(num):
    if num < 2:
        return 'Não é primo'

    for c in range(2, num):
        if num % c == 0:
            return 'Não é primo'
            
    return 'É primo'
            
print(confere_num(int(input('Digite um número: '))))    
