primeiro = int(input('Insira o primeiro termo da sua PA: '))
razao = int(input('Insira a razão da sua PA: '))
contador = 1
termo = primeiro
mais = 10
qtde_termos = 0
while mais != 0:
    qtde_termos += mais
    while contador <= qtde_termos:
        print(f'{termo}', end = ' ')
        termo +=razao
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Programa finalizado!')
