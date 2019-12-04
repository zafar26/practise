position_c = 3
position_r = 3
n = 5
arr = []
count = 0
position_r -= 1
position_c -= 1

for i in range(n):
    arr.append([])
    
    for j in range(n):
        if position_r  == i and position_c  ==j:
            arr[i].append('z')
            count += 1
        # elif position_c - 1== i and  position_r - 1  == i:
        #     arr[i].append('r')
        #     count += 1
        elif position_r == i: #and position_c <= n:
            arr[i].append('r')
            count += 1
        elif position_c == j: #and position_r <= n:
            arr[i].append('c')
            count += 1
        elif i == j:
            arr[i].append('*')
            count += 1
        elif i + j == n - 1:
            count +=1
            arr[i].append('#')
        
        elif i - 1 < n and j + 1 <= n:
            count += 1
            arr[i].append(' ')

        else:
            count +=1
            arr[i].append(' ')

        # if i - 1 < n and j + 1 < n:
        #     count += 1
        # if j - 1 < n and i + 1 < n:
        #     count += 1
print(count)
for i in range(len(arr)):
    print(arr[i])


    