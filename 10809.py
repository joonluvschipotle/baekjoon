alist = [-1] * 26
a = input()
for num in range(0,len(a)):
    if (alist[ord(a[num])-97] == -1):
        alist[ord(a[num])-97] = num

for ele in alist:
    print (str(ele) + ' ',end='')
