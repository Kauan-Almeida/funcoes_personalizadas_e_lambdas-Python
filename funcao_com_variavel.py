import math
#função personalizada sobre Mensagem e Raiz
def mensagem():
    print("A raiz quadrada é: ")

def raizQuadrada(num):
    num = math.sqrt(num)
    mensagem()
    print(num)

raizQuadrada(81)

#função lambda
num = lambda: math.sqrt(9)
print(num())



