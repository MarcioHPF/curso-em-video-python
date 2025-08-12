def área(larg, compr):
    area = larg * compr
    print(f'A área de um terreno com {larg}m de largura e {compr}m de comprimento é igual a {area}m²')


largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

área(largura,comprimento)