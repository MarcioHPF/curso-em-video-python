num = int(input('Digite um número: '))

print(f'Análise do número {num}:')
print(f'''Unidade: {num // 1 % 10}
Dezena: {num // 10 % 10}
Centena: {num // 100 % 10}
Milhar: {num // 1000 % 10}
''')