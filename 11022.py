trial = input()
ans = [0] * int(trial)
alist = []
for num in range(int(trial)):
    a = input()
    alist.append(a)
    b = a.split()
    ans[num] = (int(b[0])+int(b[1]))

for num in range(int(trial)):
    print ("Case #" + str(num+1) + ": " + alist[num][0] + " + " + alist[num][2] + " = " + str((ans[num])))
