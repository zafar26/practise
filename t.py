n = 4
b = 0
for i in range(n):
    v = n - i
    if i == 0:
        b = 1
    else:
        b += 2
    for j in range(b):
        print(v,end ="")
    print()
for i in range(n-1,0,-1):
    v = n - i + 1
    if i == 0:
        b = 1
    else:
        b -= 2
    for j in range(b):
        print(v,end ="")
    print()