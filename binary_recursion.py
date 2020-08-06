number = []
#usar recursão (retornar o resto da divisão)
def remain(num, soma = 0, consecutives = 0):
    if num == 0:
        return consecutives
    else:
        resto = int(num%2)
        soma = soma + resto if resto != 0 else resto 
        if soma > consecutives:
            consecutives = soma
        number.insert(0, resto)
        return remain(int(num/2), soma, consecutives)

if __name__ == "__main__":
    n = 30
    print(remain(n))
    print(int("".join([str(i) for i in number])))