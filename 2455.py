first = input().split()
second = input().split()
third = input().split()
fourth = input().split()

train = 0
maxi = 0
train = int(first[1])
maxi = train
train = train - int(second[0]) + int(second[1])
if train > maxi:
    maxi = train
train = train - int(third[0]) + int(third[1])
if train > maxi:
    maxi = train
train = train - int(fourth[0]) + int(fourth[1])
if train > maxi:
    maxi = train

print (maxi)
