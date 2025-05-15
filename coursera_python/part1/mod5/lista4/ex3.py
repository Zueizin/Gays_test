def vogal(letra):
    if letra in 'aeiouAEIOU':
        return True
    else:
        return False
letra = input('Digite uma letra: ')
print(vogal(letra))