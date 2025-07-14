cato = float(input('Digite a medida do cateto oposto: '))
cata = float(input('Digite a medida do cateto adjacente: '))

print(f'O valor da hipotenusa de um triângulo com os catetos {cato} e {cata} é igual a {((cato ** 2) + (cata ** 2)) ** 1/2:.2f}')
