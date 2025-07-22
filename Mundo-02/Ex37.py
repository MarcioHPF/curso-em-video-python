num = int(input('Digite um número inteiro: '))
print(''' Opções para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
''')
opc = int(input('Digite a opção desejada: '))

if opc == 1:
    print(f'O valor {num} em binário é igual a {bin(num)[2:]}')
elif opc == 2:
    print(f'O valor {num} em octal é igual a {oct(num)[2:]}')
elif opc == 3:
    print(f'O valor {num} em hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção inválida! Reinicie o programa.')
