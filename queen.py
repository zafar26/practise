position_r = 3-1
position_c =3-1
moves = []
n = 5
mat = [["-"] * n for i in range(n)]

mat[position_r][position_c] ="Q"

### QUEEN #####

######## MOVES ########
# -U- = upwards
# _D_ = downwards
# M-R = move right
# M-L = move left
# MUL = move up left
# MDR = move down right
# MUR = move up right
# MDL = move down left
#########################



# To Move Up
r=position_r
c=position_c
r-=1
while(r>=0) and r < n and c < n:
    moves.append([r,c])
    mat[r][c]='-U-'
    r-=1



# To Move Down 
r=position_r
c=position_c
r+=1
while(r<8) and r < n and c < n:
    moves.append([r,c])
    mat[r][c]='_D_'
    r+=1



# To move left 
r=position_r
c=position_c
c-=1
while(c>=0) and r < n and c < n:
    moves.append([r,c])
    mat[r][c]='M-L'
    c-=1

    
# To move Right :
r=position_r
c=position_c
c+=1
while(c<8) and r < n and c < n:
    moves.append([r,c])
    mat[r][c]='M-R'
    c+=1



# To move Up Right:
r=position_r
c=position_c
r-=1
c+=1
while(r>=0 and c<8) and r < n and c < n:
    moves.append([r,c])
    mat[r][c]='MUR'
    r-=1
    c+=1


# To move Up Left :
r=position_r
c=position_c
r-=1
c-=1
while(r>=0 and c>=0) and r < n and c < n:
    moves.append([r,c])
    mat[r][c]='MUL'
    r-=1
    c-=1


# To move Down Right :
r=position_r
c=position_c
r+=1
c+=1
while(r<8 and c<8) and r < n and c < n:
    moves.append([r,c])
    mat[r][c]='MDR'
    r+=1
    c+=1


# To Move Down Left:
r=position_r
c=position_c
r+=1
c-=1
while(r<8 and c>=0) and r < n and c < n:
    moves.append([r,c])
    mat[r][c]='MDL'
    r+=1
    c-=1



for i in range(n):
    print(mat[i])

#print(moves)