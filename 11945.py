a = input()
size = a.split()
width = int(size[1])
height = int(size[0])

fish = []
for i in range(0,height):
    fish.append(input())

for i in range(0,height):
    for j in range(0,width):
        print (fish[i][width-j-1],end="")
    print ("")
