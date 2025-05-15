def e_hipotenusa(num):
    b = 1
    while b < num:
        c = 1
        while c < num:
            if pow(num,2) == pow(b,2) + pow(c,2):
                return True
                break
            c += 1
        b += 1
def soma_hipotenusas(n):
    somatoria = 0
    if n < 5:
        return 0
    num = 5
    while num <= n:
        if e_hipotenusa(num):
            somatoria = num + somatoria
        num += 1
    return somatoria
print("Digite um valor negativo para sair")
while True:
    n = int(input("Digite o limite: "))
    if n < 0:
        print("Fechando o programa")
        break
    soma = soma_hipotenusas(n)
    print(f"A soma das possiveis hipotenusas inteiras ate o {n}: {soma}")
    print()  