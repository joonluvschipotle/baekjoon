a = input()
bin = []
dummy = ""
for i in range(0,len(a)):
    if len(dummy) == 3:
        bin.append(dummy)
        dummy=""
    dummy+=a[len(a)-i-1]
    print(dummy)
if len(dummy) == 1:
    dummy2 ="00"+dummy
    bin.append(dummy2)
elif len(dummy) == 2:
    dummy2 = "0"+dummy
    bin.append(dummy2)


octa = []
for i in bin:
    octa.append(int(i[0])*4 + int(i[1])*2 + int(i[2]))

print (octa)

for i in range(0,len(octa)):
    print(octa[len(octa)-i-1],end="")

