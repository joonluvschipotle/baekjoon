a = input().split()
n = int(a[0])
m = int(a[1])
bot = 0
dum = []
ans = []

for i in range(0,n):
    dum.append(i+1)
while(len(ans)<n):
    for i in range(bot,len(dum)):
        if i%m == 0 and i!=0 and dum[i-1]!=1:
            ans.append(dum[i-1])
            dum[i-1] = -1
    bot = len(dum)
    for i in range(0,len(dum)):
        if dum[i] != -1:
            dum.append(dum[i])
    print (ans)
print (ans)
