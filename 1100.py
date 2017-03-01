board = []
for i in range(0,8):
    board.append(input())

pieces = 0
for i in range(0,8):
    if i%2 == 0:
        for j in range(0,8):
            if j%2 == 0 and board[i][j] == "F":
                pieces+=1
    else:
        for j in range(0,8):
            if j%2 != 0 and board[i][j] == "F":
                pieces +=1

print (pieces)
