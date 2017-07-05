a = int(input())
n = input().split()
nlist = []
for i in range(0,a):
    nlist.append(int(n[i]))

print(min(nlist), max(nlist))
