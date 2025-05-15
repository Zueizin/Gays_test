n = int(input('Digite um número inteiro: '))
def maior_primo(n):
    def e_primo(num):
        if num < 2:
            return False
        i = 2
        while i >= 2 and i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    while n >= 2:
        if e_primo(n,2):
            return n
        n -= 1
print(maior_primo(n))