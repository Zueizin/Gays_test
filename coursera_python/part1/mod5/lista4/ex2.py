def maior_primo(n):
    def eh_primo(num):
        if num < 2:
            return False
        i = 2
        while i * i <= num: 
            if num % i == 0:
                return False
            i += 1
        return True
    while n >= 2:
        if eh_primo(n):
            return n
        n -= 1
n = int(input('Digite um número inteiro: '))
print(maior_primo(n))