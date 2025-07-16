frase = str(input('Digite uma frase: ')).strip().lower()

print(f'''A frase tem {frase.count('a')} ocorrências da letra A
A letra A aparece pela primeira vez na posição {frase.find('a') + 1}      
A letra A aparece pela última vez na posição {frase.rfind('a') + 1}''')
