nums = []
for i in range(0,9):
    nums.append(input().split())

maxi = 0
index = [0]
for i in range(0,9):
    for j in range(0,9):
        if int(nums[i][j]) > maxi:
            maxi = int(nums[i][j])
            index[0] = ([i+1,j+1])

print (str(maxi) + "\n" + str(index[0][0]) + " " + str(index[0][1]))
