x = int(input())
a = input()
b = input()
fail = 0

for i in range(0,len(a)):
    if a[i]==b[i]:
        fail+=1
        break

if fail==0:
    print ("Deletion succeeded")
else: print ("Deletion failed")
