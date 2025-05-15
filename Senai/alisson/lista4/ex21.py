h = 0
n = int(input("Digite ate qual denominador ira: "))
for i in range(1,n+1):
    if i % 2 == 0:
        h -= 1/i
    else:
        h += 1/i
print(h)