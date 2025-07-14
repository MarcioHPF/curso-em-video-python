import math

angulo = float(input('Digite o ângulo desejado: '))
rad = math.radians(angulo)

print(f'O seno do ângulo é igual a {math.sin(rad):.2f}')
print(f'O cosseno do ângulo é igual a {math.cos(rad):.2f}')
print(f'A tangente do ângulo é igual a {math.tan(rad):.2f}')
