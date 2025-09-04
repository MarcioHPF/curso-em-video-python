def checa_palindromo(frase):
    inverso = ''
    frase = frase.replace(" ", "")
    
    # if frase == frase[::-1]              ->  Substitui o for da função com uma linha
    for c in range(len(frase) -1, -1, -1):
        inverso += frase[c]

    if inverso == frase:
        return 'É um palíndromo!'
    else:
        return 'Não é um palíndromo!'
    
print(checa_palindromo(str(input('Digite uma frase: ')).strip().lower()))
