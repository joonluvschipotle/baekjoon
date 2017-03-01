n = int(input())
ans = n
cycle = 0
a = -1
while(n!=a):
    if ans < 10:
        ans = ans*11
    else:
        ans = int(str(int(str(ans)[-1])) + str(int(str(ans)[0]) + int(str(ans)[1]))[-1])
    cycle +=1
    a = ans


print (cycle)
