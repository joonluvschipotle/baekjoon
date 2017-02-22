#65~90
#97~122
a = input()
b = ''
for num in range(0,len(a)):
    if ord(a[num]) > 64 and ord(a[num]) < 78:
        b += chr(ord(a[num])+13)
    elif ord(a[num]) > 77 and ord(a[num]) < 91:
        b += chr(ord(a[num])-13)
    elif ord(a[num]) > 96 and ord(a[num]) < 110:
        b += chr(ord(a[num])+13)
    elif ord(a[num]) > 109 and ord(a[num]) < 123:
        b += chr(ord(a[num])-13)
    else:
        b += a[num]
print (b)
