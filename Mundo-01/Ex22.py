nome = input('Digite o seu nome completo: ').strip()
separado = nome.split()

print(f'O seu nome com todas as letras maiúsculas é {nome.upper()}.')
print(f'O seu nome com todas as letras minúsculas é {nome.lower()}.')
print(f'O seu nome tem {len(nome.replace(' ', ''))} letras')
print(f'O seu primeiro nome é{separado[0]} e tem {len(separado[0])} letras.')
