n = int(input())
a = 0
b = 0

for i in range(0,n):
    x = input().split()
    if int(x[0]) > int(x[1]):
        a+=1
    elif int(x[0]) < int(x[1]):
        b+=1
print(a,b)