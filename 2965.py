x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
nums = 0

while(c-a != 2):
    if (c-b) > (b-a):
        a = b
        b += 1
    else:
        c = b
        b -= 1
    nums+=1

print (nums)
