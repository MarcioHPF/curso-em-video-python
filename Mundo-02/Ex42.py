ladoA = float(input('Digite o valor da reta A: '))
ladoB = float(input('Digite o valor da reta B: '))
ladoC = float(input('Digite o valor da reta C: '))

if ladoA + ladoB > ladoC and ladoB + ladoC > ladoA and ladoA + ladoC > ladoB:
    print('As três retas podem formar um triângulo',end=' ')
    if ladoA == ladoB and ladoB == ladoC:
        print('EQUILÁTERO!')
    elif (ladoA == ladoB and ladoB != ladoC) or (ladoA == ladoC and ladoC != ladoB) or (ladoB == ladoC and ladoC != ladoA):
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else: 
    print('As três retas não podem formar um triângulo!')