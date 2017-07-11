n = int(input())
dummyR = input().split()
result = 0
count = 1

for i in dummyR:
    result += int(i)*count
    if int(i) == 0:
        count = 1
    else:
        count += 1
print (result)