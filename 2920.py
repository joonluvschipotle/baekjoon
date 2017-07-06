a = input().split()
b = []
count = 1
yes = 0
ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]

for i in a:
    b.append(int(i))

if b == ascending:
    print("ascending")
elif b == descending:
    print("descending")
else:
    print("mixed")