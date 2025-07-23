peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura ** 2)

print(f'Com {peso}kg e {altura}m de altura, você tem um IMC de {imc}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Você está como PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Você está no SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBITA')
