a = input()
inta = int(a)
ans = ""
next = 0

def checkNull(df,x):
    try:
        return df[x]
    except IndexError:
        return None

for i in range(0,len(a)):
    if next == 1:
        ans += "7"
        if checkNull(a,i+1) is not None:
            next = 1
        else:
            next = 0
    elif int(a[i]) < 4:
        next = 1
    else:
        if int(a[i]) >= 7 or checkNull(a,i+1) is not None:
            ans += "7"
        else:
            ans += "4"

print(ans)