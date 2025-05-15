n = int(input("Digite ate qual denominador ira: "))
s = 0
for i in range(1,n+1):
    s += 1/i**i
print(s)