def conta_vogal(frase):
    # return sum(1 for letra in frase if letra in 'aeiou') -> faz tudo que a função faz em uma linha
    tot_vogal = 0
    for letra in frase:
        if letra in 'aeiou':
            tot_vogal += 1
    return tot_vogal

print(f"Quantidade de vogais: {conta_vogal(input('Digite uma frase: ').strip().lower())}")
