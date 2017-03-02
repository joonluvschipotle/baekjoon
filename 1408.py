
current = input()
start = input()

if int(start[0:2]) > int(current[0:2]):
    print ("00:"+ calcTime(int(current[2:4]),int(start[2:4])))



def calcTime(x,y):
    if y > x:
        if y-x < 10:
            return "0" + str(y-x)
        else:
            return str(y-x)
    else:
