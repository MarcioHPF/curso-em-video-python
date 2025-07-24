tot_idade = vinte_menos = velho = 0
nome_velho = ''
for c in range(1, 5):
    print (f'---- {c} ª Pessoa ----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Gênero[M/F]: ')).upper()
    tot_idade += idade
    
    if sexo in 'Mm':
        if idade > velho:
            velho = idade
            nome_velho = nome
    else:
        if idade < 20:
            vinte_menos += 1

print(f'''A média das idades do grupo é {tot_idade/4}
O homem mais velho é o {nome_velho}
Existe(m) {vinte_menos} mulher(es) menor(es) de 20 anos
''')
  