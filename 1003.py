zero = 0
one = 0
memo = [-1] * 100
memo[0] = 0
memo[1] = 1
ansZero = [-1] * 100
ansOne = [-1] * 100

def testcase():
    global zero
    global one
    input1 = input()
    cases = []
    dummy = []
    for nums in range(int(input1)):
        input2 = input()
        cases.append(int(input2))
    dummy = sorted(cases)
    for trial in dummy:
        fibonacci(trial)
        ansZero[trial] = zero
        ansOne[trial] = one
        zero = 0
        one = 0
    for trial in cases:
        print (str(ansZero[trial]) + " " + str(ansOne[trial]))


def fibonacci(n):
    global zero
    global one
    if (n==0):
        addNum(0)
        return 0
    elif (n==1):
        addNum(1)
        return 1
    else:
        if (memo[n] != -1):
            zero += ansZero[n]
            one += ansOne[n]
            return memo[n]
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]

def addNum(a):
    global zero
    global one
    if (a==0):
        zero+=1
    if (a==1):
        one+=1


testcase()
