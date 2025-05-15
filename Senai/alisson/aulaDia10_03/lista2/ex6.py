import math
x1 = int(input("Digite o valor no eixo x do primeiro ponto: "))
y1 = int(input("Digite o valor no eixo y do primeiro ponto: "))
x2 = int(input("Digite o valor no eixo x do segundo ponto: "))
y2 = int(input("Digite o valor no eixo y do segundo ponto: "))
d = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
print(d)