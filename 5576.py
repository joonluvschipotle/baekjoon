collegeA = []
collegeB = []
for i in range(0,10):
    collegeA.append(int(input()))

for i in range(0,10):
    collegeB.append(int(input()))

collegeA.sort()
collegeB.sort()

a = collegeA[9] + collegeA[8] + collegeA[7]
b = collegeB[9] + collegeB[8] + collegeB[7]

print(a,b)
