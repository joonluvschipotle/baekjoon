a = input()
text = []
for i in range(0,len(a)):
    text.append(a[i])
trials = int(input())
cursor = len(text)

for i in range(0,trials):
    command = input().split()
    if command[0] == "L":
        if cursor==0:
            pass
        else:
            cursor -=1
    elif command[0] == "D":
        if cursor==len(text):
            pass
        else:
            cursor +=1
    elif command[0] == "B":
        if cursor==0:
            pass
        else:
            del text[cursor-1]
            cursor -=1
    elif command[0] == "P":
        text.insert(cursor,command[1])
        cursor +=1

for i in text:
    print (i,end="")

print ("")
