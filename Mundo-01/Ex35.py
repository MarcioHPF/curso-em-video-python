ladoA = float(input('Digite o valor da reta A: '))
ladoB = float(input('Digite o valor da reta B: '))
ladoC = float(input('Digite o valor da reta C: '))

if ladoA + laboB > ladoC and ladoB + ladoC > ladoA and ladoA + ladoC > ladoB:
    print('As três retas podem formar um triângulo!')