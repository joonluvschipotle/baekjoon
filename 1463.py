x = int(input())
trials = 0
while (x!=1):
    if x%3 == 0:
        x /= 3
    elif x%2 == 2 and (x-1)%3 !=0:
        x /=2
    else: x -=1
    trials+=1

print (trials)
