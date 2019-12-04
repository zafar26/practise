m = 7
n = m * 2
arr = []
for i in range(n):
    arr.append([])
    if i >= m:
        for j in range(abs(m-i-1)):
            arr[i].append("*")
        for k in range(((n-1)-i) *2 ):
            arr[i].append(' ')
        for l in range(abs(m - i - 1)):
            arr[i].append("*")
    else:
        for j in range(abs(m- i)):
            arr[i].append("*")
        for k in range(i*2):
            arr[i].append(' ')
        for l in range(abs(m-i)):
            arr[i].append("*")
for  i in range(len(arr)):
    print(arr[i])
    