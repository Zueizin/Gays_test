def e_hipotenusa(num):
    if num % 5 == 0:
        return True

def soma_hipotenusas(n):
    num = 5
    somatorio = 0 
    while num <= n:
        if n < num:
            print("Nao possui hipotenusas.")
        else:
            if e_hipotenusa(num):
                somatorio = num + somatorio
            num += 1
    return somatorio


n = int(input("Digite o valor limtite: "))
print(soma_hipotenusas(n))    