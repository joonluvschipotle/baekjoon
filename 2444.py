a = int(input())
for i in range(0,a):
    print (" "*(a-i-1) + "*"*((1+i)*2-1))
for i in range(1,a):
    print (" "*i + "*"*(a*2-(i*2)-1))
