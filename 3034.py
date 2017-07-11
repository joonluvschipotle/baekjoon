a = input().split()
n = int(a[0])
w = int(a[1])
h = int(a[2])

for i in range(0,n):
    match = int(input())
    if (match*match) > (w*w)+(h*h):
        print ("NE")
    else:
        print ("DA")