a = input()
total = 0
dumstring = ""
for i in range(0,len(a)):
    if a[i] == ",":
        total += int(dumstring)
        dumstring = ""
    else:
        dumstring+=a[i]
total += int(dumstring)


print (total)