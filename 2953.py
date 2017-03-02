score = []
for i in range(0,5):
    score.append(input().split())
sums = []
for i in range(0,5):
    dum = 0
    for j in range(0,4):
        dum += int(score[i][j])
    sums.append(dum)

print (sums.index(max(sums))+1, max(sums))
