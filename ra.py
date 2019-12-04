mat=[[0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,'Q',0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0]]
moves=[]#//array for successfull moves
#//update xQPos & yQPos if you change 'Q' in mat[][]
xQPos=5#//x coordinate of Queen
yQPos=2#y coordinate of Queen
#//fn. to check whether coordinates are a valid move or not
def isValidMove(r,c):
   return mat[r][c]==0
#//fn. to move upwards till move is valid
def moveUp():
   r=xQPos
   c=yQPos
   r-=1
   while(r>=0):
       if(isValidMove(r,c)):
           moves.append([r,c])
           mat[r][c]='.'
           r-=1
       else:
           return
#//fn. to move downwards till move is valid
def moveDown():
   r=xQPos
   c=yQPos
   r+=1
   while(r<8):
       if(isValidMove(r,c)):
           moves.append([r,c])
           mat[r][c]='.'
           r+=1
       else:
           return
#//fn. to move leftwards till move is valid
def moveLeft():
   r=xQPos
   c=yQPos
   c-=1
   while(c>=0):
       if(isValidMove(r,c)):
           moves.append([r,c])
           mat[r][c]='.'
           c-=1
       else:
           return
def moveRight():
   r=xQPos
   c=yQPos
   c+=1
   while(c<8):
       if(isValidMove(r,c)):
           moves.append([r,c])
           mat[r][c]='.'
           c+=1
       else:
           return
def moveUpRight():
   r=xQPos
   c=yQPos
   r-=1
   c+=1
   while(r>=0 and c<8):
       if(isValidMove(r,c)):
           moves.append([r,c])
           mat[r][c]='.'
           r-=1
           c+=1
       else:
           return
def moveUpLeft():
   r=xQPos
   c=yQPos
   r-=1
   c-=1
   while(r>=0 and c>=0):
       if(isValidMove(r,c)):
           moves.append([r,c])
           mat[r][c]='.'
           r-=1
           c-=1
       else:
           return
def moveDownRight():
   r=xQPos
   c=yQPos
   r+=1
   c+=1
   while(r<8 and c<8):
       if(isValidMove(r,c)):
           moves.append([r,c])
           mat[r][c]='.'
           r+=1
           c+=1
       else:
           return
def moveDownLeft():
   r=xQPos
   c=yQPos
   r+=1
   c-=1
   while(r<8 and c>=0):
       if(isValidMove(r,c)):
           moves.append([r,c])
           mat[r][c]='.'
           r+=1
           c-=1
       else:
           return
moveUp()
moveDown()
moveLeft()
moveRight()
moveUpRight()
moveUpLeft()
moveDownRight()
moveDownLeft()
for i in range(len(mat)):
   print(mat[i])
# print("-------------------")
# for each in mat:
#     print("|"+" "+"|")
#     print("-------------------")
# //uncomment following stmt. to see coordinates
# // console.log('x,y')
# // moves.forEach(item=>{
# //   console.log(item.join())
# // })

