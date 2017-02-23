testcase = input()
cases = []
ans = ""

for i in range(0,int(testcase)):
    cases.append(input())

for i in range(0,len(cases[0])):
    dum = 0
    for j in range(0,int(testcase)-1):
        if cases[j][i] != cases[j+1][i]:
            dum+=1
            break
    if dum == 0:
        ans += cases[0][i]
    else:
        ans += "?"

print (ans)
