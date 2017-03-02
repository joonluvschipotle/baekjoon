n = int(input())
balls = []
for i in range(0,n):
    balls.append(input().split())

for i in range(0,n):
    nums = 0
    for j in range(0,n):
        ownerColor = int(balls[i][0])
        ownerNum = int(balls[i][1])
        playerColor = int(balls[j][0])
        playerNum = int(balls[j][1])
        if ownerColor != playerColor and ownerNum > playerNum:
            nums += playerNum
    print (nums)
