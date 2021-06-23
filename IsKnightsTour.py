
def checkLeft(i,j,val,board):
    a = i-1
    b=j-2
    c = i+1
    up=-1
    down=-1
    if(a>=0 and b>=0):
        up = board[i-1][j-2]
    if(c<len(board) and b>=0):
        down = board[i+1][j-2]
    if(up == val or down == val):
        return True
    return False

def checkRight(i,j,val,board):
    a =i+1
    b=j+2
    c=i-1
    up=-1
    down=-1
    if(a<len(board) and b <len(board[0])):
        down = board[i+1][j+2]
    if(c>=0 and  b <len(board[0])):
        up = board[i-1][j+2]
    if(up==val or down==val):
        return True
    else:
        return False   

def checkDown(i,j,val,board):
    a = i+2
    b= j-1
    c= j+1
    left = -1
    right = -1
    if(a<len(board) and b>=0):
        left = board[i+2][j-1]
    if(a<len(board) and c<len(board[0])):
        right = board[i+2][j+1]
    if(left == val or right == val):
        return True
    return False

def checkUp(i,j,val,board):
    a = i-2
    b = j-1
    c = j+1
    left = -1
    right = -1
    if(a>=0 and b>=0):
         left = board[i-2][j-1]
    if(a>=0 and c<len(board[0])):
        right = board[i-2][j+1]
    if(left == val or right == val):
        return True
    return False

def isKnightsTour():
    board =   [ [  1, 60, 39, 34, 31, 18,  9, 64 ],[ 38, 35, 32, 61, 10, 63, 30, 17 ],[ 59,  2, 37, 40, 33, 28, 19,  8 ],[ 36, 49, 42, 27, 62, 11, 16, 29 ],[ 43, 58,  3, 50, 41, 24,  7, 20 ],[ 48, 51, 46, 55, 26, 21, 12, 15 ], [ 57, 44, 53,  4, 23, 14, 25,  6 ],[ 52, 47, 56, 45, 54,  5, 22, 13 ], ]
    # print(board)
    rows = len(board)
    columns = len(board[0])
    total = rows * columns
    # print(total)
    res = True
    # for i in range(1,total):
    for i in range(0,rows):
        for j in range(0,columns):
            val = board[i][j]
            if(val!=total):
                one=checkRight(i,j,val+1,board)
                two = checkDown(i,j,val+1,board)
                three = checkUp(i,j,val+1,board)
                four = checkLeft(i,j,val+1,board)
                if(one == True or two == True or three == True or four == True):
                    continue
                else:
                    return False
    return True

print(isKnightsTour())
