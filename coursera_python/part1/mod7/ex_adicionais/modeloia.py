def soma_hipotenusas(n):
    soma = 0
    for h in range(5, n+1):  # A menor hipotenusa possível é 5 (3-4-5)
        # Verifica se h é da forma 4k+1 ou tem fatores primos da forma 4k+1
        if any(p % 4 == 1 for p in fatores_primos(h)):
            soma += h
    return soma

def fatores_primos(num):
    """Retorna os fatores primos de um número"""
    fatores = set()
    while num % 2 == 0:
        fatores.add(2)
        num = num // 2
    i = 3
    while i * i <= num:
        while num % i == 0:
            fatores.add(i)
            num = num // i
        i += 2
    if num > 1:
        fatores.add(num)
    return fatores

n = int(input("Maximo: "))
print(soma_hipotenusas(n))