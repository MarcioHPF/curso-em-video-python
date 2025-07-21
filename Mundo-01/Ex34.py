sal = float(input('Digite o valor do salário para calcular o reajuste: '))

if sal > 1250:
    print(f'O salário teve um aumento de 10%. O novo salário é de R${sal + (sal * 0.1)}')
else:
    print(f'O salário teve um aumento de 15%. O novo salário é de R${sal + (sal * 0.15)}')
