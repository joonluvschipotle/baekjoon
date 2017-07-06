a = int(input())
b = input().split()

count = 0
for i in b:
    if int(i) == a:
        count+=1

print(count)
