a = int(input())
for i in range(0,a):
    print ("*"*(i+1) + " "*((a*2)-(i*2)-2) + "*"*(i+1))
for i in range(1,a):
    print ("*"*(a-i) + " "*((i*2)) + "*"*(a-i))
