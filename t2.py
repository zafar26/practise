n = 5
arr = []#[[" "]*n]*n

b =3
c =3
for i in range(n):
    arr.append([])
    

for i in range(n):
    for j in range(i+1):
        arr[i].append(j+1)
    for k in range(n-i-1):
        arr[i].append(i+1)

for i in range(n):
    for j in range(n-i-1):
        arr[i].append(i+1)

for i in range(n):
    for j in range(i,0,-1):
        arr[i].append(j)
        
      
for j in range(1,n,1):
    arr.append(arr[n-j-1].copy())
    
      
        #i+1 0







# for i in range(n):
#    for j in range(i):
#        arr[i].append(i)
   
   
   
   # for j in range(n):


# for i in range(n,0,-1):
#     for j in range(i+1):
#         arr[i-1].append(j+1)
#     for k in range(n-i-1):
#         arr[i-1].append(i+1)
    







for i in range(len(arr)):
    print(arr[i])