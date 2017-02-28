while True:
    string = input()
    lowers = 0
    uppers = 0
    numbers = 0
    spaces = 0
    for i in range(0,len(string)):
        if ord(string[i]) == 32:
            spaces += 1
        elif ord(string[i]) > 64 and ord(string[i]) < 91:
            uppers += 1
        elif ord(string[i]) > 96 and ord(string[i]) < 123:
            lowers += 1
        elif ord(string[i]) > 47 and ord(string[i]) < 58:
            numbers += 1
    print (str(lowers) + " " + str(uppers) + " " + str(numbers) + " " + str(spaces))



# space -> 32
# A ~ Z -> 65 ~ 90
# a ~ z -> 97 ~ 122
# 0 ~ 9 -> 48 ~ 57
