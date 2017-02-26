b = input()
java = 0
c = 0
a = []

for i in range(0,len(b)):
    a.append(b[i])


for i in a:
    if i == "_":
        c +=1
    elif ord(i) > 64 and ord(i) < 91:
        java +=1

if c != 0 and java != 0:
    print ("Error!")
elif c != 0 and java == 0:
    for i in range(0,len(a)):
        if a[i] == "_":
            a[i+1] = chr(ord(a[i+1])-32)
            del a[i]
        if a.count("_") == 0:
            break
elif java != 0 and c == 0:
    for i in range(0,len(a)):
        if ord(a[i]) > 64 and ord(a[i]) < 91:
            a[i] = chr(ord(a[i])+32)
            a.insert(i,"_")

if c != 0 and java != 0:
    print ("Error!")
elif c != 0 and java == 0:
    for i in range(0,len(a)):
        if a[i] == "_":
            a[i+1] = chr(ord(a[i+1])-32)
            del a[i]
        if a.count("_") == 0:
            break
elif java != 0 and c == 0:
    for i in range(0,len(a)):
        if ord(a[i]) > 64 and ord(a[i]) < 91:
            a[i] = chr(ord(a[i])+32)
            a.insert(i,"_")

for i in a:
    print (i,end="")
