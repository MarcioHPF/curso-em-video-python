expressão = str(input('Digite uma expressão: '))
parenteses = []
for letra in expressão:
    if letra == '(':
        parenteses.append('(')
    elif letra == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break

if len(parenteses) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
