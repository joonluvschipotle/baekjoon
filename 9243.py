n = int(input())
a = input()
b = input()

if n%2 == 0:
    if a == b:
        print ("Deletion succeeded")
    else:
        print ("Deletion failed")
elif n%2 != 0:
    total = 0
    for i in range(0,len(a)):
       if int(a[i])+int(b[i])==1:
           total+=1
    if total==len(a):
        print ("Deletion succeeded")
    else:
        print ("Deletion failed")