a = input()
mirror = []
for i in range(0,int(a)):
    mirror.append(input())
mood = input()


if int(mood) == 1:
    for i in mirror:
        print (i)
elif int(mood) == 2:
    for i in mirror:
        for x in range(0,len(i)):
            print (i[len(i)-1-x],end='')
        print ("")
elif int(mood) == 3:
    for i in range(0,int(a)):
        print (mirror[int(a)-1-i])
