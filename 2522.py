a = int(input())
for i in range(0,a):
    print (" "*(a-i-1) + "*"*(i+1))
for i in range(0,a-1):
    print (" "*(i+1) + "*"*(a-i-1))
