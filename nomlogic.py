n = 4
s = 'zafar'
arr = []
for i in range(n):
    arr.append([])
    for j in range(n):
        if i == j:
            arr[i].append(s[i])
        else:
            arr[i].append('-')
for i in arr:
    print(i)