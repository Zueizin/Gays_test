def maximo(x,y):
    if x > y:
        return x
    else:
        return y
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
print("O maior número é: ", maximo(x,y))