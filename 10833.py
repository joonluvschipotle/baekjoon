n = int(input())
list1 = []


for i in range(0,n):
    list1.append(input().split())


remnant = 0

for i in range(0,n):
    apples = int(list1[i][1])
    students = int(list1[i][0])
    if apples/students >= 1:
        remnant += apples%students
    else:
        remnant += apples

print (remnant)