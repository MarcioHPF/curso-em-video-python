def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return(f'Com {idade} anos o voto é negado.')
    elif (idade >= 16 and idade < 18) or idade > 60:
        return(f'Com {idade} anos o voto é opcional.')
    else:
        return(f'Com {idade} anos o voto é obrigatório.')


ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))
