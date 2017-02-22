trial = input()
ans = [0] * int(trial)
for num in range(int(trial)):
    a = input()
    b = a.split()
    ans[num] = (int(b[0])+int(b[1]))

for num in range(int(trial)):
    print (ans[num])
