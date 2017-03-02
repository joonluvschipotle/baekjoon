trial = int(input())
ans = 0
for i in range(0,trial):
    dum = input().split()
    a = pow(int(dum[0]),int(dum[1]))
    print (str(a)[-1])
