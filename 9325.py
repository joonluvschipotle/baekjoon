testcase = input()
caseAns = []
def solve():
    global caseAns
    price = int(input())
    options = input()
    for i in range(0,int(options)):
        option = input()
        calc = option.split()
        price += (int(calc[0]) * int(calc[1]))
    caseAns.append(price)


for dk in range(0,int(testcase)):
    solve()

for dk in range(0,int(testcase)):
    print (caseAns[dk])
