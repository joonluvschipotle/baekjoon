zero = 0
one = 0
memo = [-1] * 100

def testcase():
    global zero
    global one
    input1 = input()
    input2 = []
    for nums in range(int(input1)):
        input2.append(input())
    maximum = max(input2)
    for nums in input2:
        fibonacci(int(nums))
        print (str(zero) + " " + str(one))
        zero = 0
        one = 0

def fibonacci(n):
    if (n==0):
        addNum(0)
        return 0
    elif (n==1):
        addNum(1)
        return 1
    else:
        if (memo[n] != -1):
            return memo[n];
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
