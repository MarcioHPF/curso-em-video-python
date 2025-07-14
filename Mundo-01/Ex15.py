dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
km = float(input('Digite a quantidade de quilômetros rodados: '))

print(f'O valor total do aluguel de um carro por {dias} dias com a distância de {km}km é de R${(60 * dias) + (0.15 * km):.2f}')
