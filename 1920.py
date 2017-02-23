n = input()
dummy = input()
listD = dummy.split()
listN = []
for i in listD:
    listN.append(int(i))
listN.sort()

m = input()
dummy2 = input()
listE = dummy2.split()
listM = []
for i in listE:
    listM.append(int(i))

def search(data, count):
    if len(data) == 0:
        return 0
    else:
        mid = int(len(data)/2)
        if data[mid]==count:
            return 1
        else:
            if count<data[mid]:
                return search(data[:mid],count)
            else:
                return search(data[mid+1:],count)

for i in listM:
    print (search(listN, i))
