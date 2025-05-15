s1 = 0
n = int(input("Digite ate qual denominador ira: "))
s2= 0
subtracao = 0
for i in range(1,n+1):
    s1 += i/(n-subtracao)
    subtracao += 1
subtracao = 0
for i in range(1,n+1):
    s2 += (n-subtracao)/i
    subtracao += 1
s = s1 + s2
print(s)