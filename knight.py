position_r = 3-1
position_c = 3-1
moves = []
n = 5
mat = [["-"] * n for i in range(n)]

mat[position_r][position_c] ="NIGHT"

## KNIGHT##

#### MOVES ######
# U-1 = up left
# U+1 = up right
# L-1 = left up
# L+1 = left down
# D-1 = down left
# D+1 = down right
# R-1 = right up
# R+1 = right down
###################

# move down
r = position_r
c = position_c
r += 2

if r >= 0 and r < n:
    moves.append([r,c])
    if c < n and c >= 0:
        moves.append([r,c-1])
        moves.append([r,c+1])
        mat[r][c-1] = "D-1"
        mat[r][c+1] = "D+1"



# move down
r = position_r
c = position_c
r -= 2

if r >= 0 and r < n:
    if c < n and c >= 0:
        moves.append([r,c-1])
        moves.append([r,c+1])
        mat[r][c-1] = "U-1"
        mat[r][c+1] = "U+1"

# move right
r = position_r
c = position_c
c += 2

if c >= 0 and c < n:
    moves.append([r,c])
    if r < n and r >= 0:
        moves.append([r+1,c])
        moves.append([r-1,c])
        mat[r+1][c] = "R+1"
        mat[r-1][c] = "R-1"




# move left
r = position_r
c = position_c
c -= 2

if c >= 0 and c < n:
    if r < n and r >= 0:
        moves.append([r+1,c])
        moves.append([r-1,c])
        mat[r+1][c] = "L+1"
        mat[r-1][c] = "L-1"


print(moves)
for i in range(len(mat)):
    print(mat[i])