times = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Bragantino', 'Botafogo', 'Misassol', 
        'São Paulo', 'Ceará', 'Internacional', 'Corinthians', 'Fluminense', 'Atlético-MG', 
        'Grêmio', 'EC Vitória', 'Vasco da Gama', 'Santos', 'Fortaleza', 'Juventude', 'Sport Recife')

print('-' * 30)
print(f'Top 20 times da série A: {times}')
print('-' * 30)
print(f'Os cinco primeiros são {times[0:5]}')
print('-' * 30)
print(f'Os últimos quatro são {times[-4:]}')
print('-' * 30)
print(f'Os time em ordem alfabética são {sorted(times)}')
print('-' * 30)
print(f'O time do Cruzeiro está na posição {times.index('Cruzeiro') + 1}')
