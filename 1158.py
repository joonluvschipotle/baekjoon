def queue(command):
    if command[0] == "push":
        q.append(int(command[1]))
    elif command[0] == "pop":
        if len(q) == 0:
            return -1
        else:
            dum = q[0]
            del q[0]
            return dum
    elif command[0] == "size":
        print (len(q))
    elif command[0] == "empty":
        if len(q) == 0:
            print (1)
        else: print (0)
    elif command[0] == "front":
        if len(q) == 0:
            print (-1)
        else:
            print (q[0])
    elif command[0] == "back":
        if len(q) == 0:
            print (-1)
        else:
            print (q[-1])


dfdf = input().split()
n = int(dfdf[0])
m = int(dfdf[1])

a = n
q = []
ans = []
for i in range(1,n+1):
    q.append(i)
turn = 1

while(len(q)>0):
    if turn < m:
        returned = int(queue(["pop"]))
        queue(["push", returned])
        turn += 1

    else:
        ans.append(queue(["pop"]))
        turn = 1

print("<", end='')
for i in range(0,len(ans)-1):
    print(str(ans[i]) + ", ", end='')
print(str(ans[-1]) + ">")
