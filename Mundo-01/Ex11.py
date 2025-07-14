larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

area = larg * alt
tinta = area / 2

print(f'A área da parede medindo {larg}x{alt} é igual a {area:.2f}m²')
print(f'Para pintá-la, serão necessários {tinta}l de tinta')
