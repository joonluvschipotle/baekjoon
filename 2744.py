a = input()
b = ""

for i in range(0,len(a)):
    if ord(a[i]) > 64 and ord(a[i]) < 91:
        b += chr(ord(a[i])+32)
    else:
        b += chr(ord(a[i])-32)

print(b)
