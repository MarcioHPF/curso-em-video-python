from datetime import datetime

dados = {}

dados['Nome'] = str(input('Digite o seu nome: ')).strip().capitalize()
nasc = int(input('Digite o ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Digite a sua carteira de trabalho[0 se não tiver]: '))

if dados['CTPS'] == 0:
    print('-' * 50)
    for c,v in dados.items():
        print(f'{c}: {v}')
else:
    dados['Contratação'] = int(input('Digite o ano de contratação: '))
    dados['Salário'] = float(input('Digite o seu salário: R$'))
    dados['Aposentadoria'] = ((dados['Contratação'] + 35) - datetime.now().year) + dados['Idade']  

print('-' * 50)
for c,v in dados.items():
    print(f'{c}: {v}')