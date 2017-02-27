a = int(input())
left = 0
right = 0
answer = []
total = 0
nope = []

for i in range(0,a):
    par = input()
    for j in range(0,len(par)):
        if ord(par[j]) == 40:
            total +=1
            left +=1
        elif ord(par[j]) == 41:
            total -=1
            right +=1
        if total < 0:
            nope.append("nope")

    if left != right:
        answer.append("NO")
    elif len(nope) != 0:
        answer.append("NO")
    else:
        answer.append("YES")
    left = 0
    right = 0
    total = 0
    nope = []

for i in answer:
    print (i)
