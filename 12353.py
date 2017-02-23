import math

testcase = input()
ansTall = []
ansShort = []

def calcHeight():
    global ans
    inputs = input()
    data = inputs.split()
    if data[0] == "B":
        gender=5
    else: gender=-5
    height = (((int(data[1][0])*12) + (int(data[1][2:-1])) + (int(data[2][0])*12) + (int(data[2][2:-1]))) + gender)/2
    ansTall.append(str(int((height+4)/12)) + "'" + str(int((height+4)%12)) + "\"")
    ansShort.append(str(int((height-4)/12)) + "'" + str(math.ceil((height-4)%12)) + "\"")


for i in range(0,int(testcase)):
    calcHeight()

for i in range(0,int(testcase)):
    print ("Case #" + str(i+1) + ": " + str(ansShort[i]) + " to " + str(ansTall[i]))
