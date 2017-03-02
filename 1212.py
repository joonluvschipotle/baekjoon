octal = input()
binary = ""
for i in range(0,len(octal)):
    if len(binary)==0 and int(int(octal[i])/4) ==0:
        dummy = int(octal[i])
    else:
        binary += str(int(int(octal[i])/4))
        if int(octal[i]) > 3:
            dummy = abs(int(octal[i])-4)
        else:
            dummy = int(octal[i])

    if len(binary)==0 and int(dummy/2)==0:
        pass
    else:
        binary += str(int(dummy/2))

    if len(binary)==0 and int(dummy%2)==0:
        pass
    else:
        binary += str(int(dummy%2))

if len(binary) == 0:
    binary += "0"

print (binary)
