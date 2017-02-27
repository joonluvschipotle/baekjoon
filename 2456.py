first = []
second = []
third []
for i in range(0,int(input())):
    dummy = input().split()
    first.append(int(dummy[0]))
    second.append(int(dummy[1]))
    third.append(int(dummy[2]))

def count(score):
    total = 0
    for i in score:
        total += int(i)
    return total

fi = count(first)
se = count(second)
th = count(third)

def countNums(score):
    threes = 0
    twos = 0
    for i in score:
        if int(i)==3:
            threes +=1
        elif int(i)==2:
            twos +=1
    return [thress,twos]

if fi > se and fi > th:
    print ("1 " + str(fi))
elif se > fi and se > th:
    print ("2 " + str(se))
elif th > fi and th > se:
    print ("3 " + str(th))
else:
    if fi == se and fi > th:
        firstone = countNums(first)
        secondone = countNums(second)
        if firstone[0] > secondone[0]:
            print ("1 " + str(fi))
    elif fi == th and fi > se:
        getthat = 2
    elif se == th and se > fi:
        getthat = 1
    elif fi == se and fi == th:
        getthat = 1
