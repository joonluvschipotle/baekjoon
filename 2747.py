zero = 0
one = 0
memo = [-1]*100
memo[0] = 0
memo[1] = 1

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

num = int(input())
print (fibonacci(num))
