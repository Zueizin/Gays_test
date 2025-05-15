n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
def binomial(n, k):
    return fatorial(n)/(fatorial(k)*fatorial(n-k))
print(binomial(n, k))