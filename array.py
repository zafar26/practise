m = 7
n = m * 2
arr = []
for i in range(n):
    if i >= m:
        arr.append(arr[(n-i)- 1].copy())
    else:
        arr.append([])
        for j in range(m- i):
            arr[i].append("*")
        for k in range(i*2):
            arr[i].append(' ')
        for l in range(m-i):
            arr[i].append("*")
for  i in range(len(arr)):
    print(arr[i])
    