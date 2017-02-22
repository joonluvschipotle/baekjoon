a = input()
b = a.split()
num1 = b[0]
num2 = b[1]
num3 = ""
num4 = ""
for i in range(0,len(b[0])):
    num3 += num1[len(b[0])-1-i]
    num4 += num2[len(b[1])-1-i]

if (int(num3)>int(num4)):
    print (num3)
else:
    print (num4)
