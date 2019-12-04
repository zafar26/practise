m = 4
n = m * 4 

arr = []
for i in range(n):
    if i < m:
        l = i
        p = m -i -1
        arr.append([])
        for r in range(2):               
            for j in range(l):
                arr[i].append(" ")
            arr[i].append("#")
            for k in range(p):
                arr[i].append(" ")
            l = m -i -1
            p = i
    elif i >= m and i < m+m:
         arr.append(arr[m+m-i-1].copy())
    
    elif i >= m + m and i < n:
         arr.append(arr[n-i-1].copy())
    
for i in range(len(arr)):
    print(arr[i])