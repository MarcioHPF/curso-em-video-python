def notas(*nota, sit=False):
    dicio = {}
    dicio['Total'] = len(nota)
    dicio['Maior'] = max(nota)
    dicio['Menor'] = min(nota)
    dicio['Média'] = sum(nota)/len(nota)
    if sit:
        if dicio['Média'] < 6:
            dicio['Situação'] = 'Ruim'
        elif dicio['Média'] >= 6 and dicio['Média'] < 7:
            dicio['Situação'] = 'Razoável'
        else:
            dicio['Situação'] = 'Boa'
    return dicio

resp = notas(5.5, 10, 10, 6.5, sit=True)
print(resp)
