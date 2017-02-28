a = int(input())
for i in range(0,a):
    print ((" "*(a-i-1)) + "*" + (" "*(i*2-1)),end="")
    if i == 0:
        print ("")
    else:
        print ("*")
