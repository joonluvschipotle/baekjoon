sizes = input().split()
a = input().split()
b = input().split()

merge = []
for i in a:
    merge.append(int(i))

for i in b:
    merge.append(int(i))

merge.sort()

for i in merge:
    print(i, end=" ")