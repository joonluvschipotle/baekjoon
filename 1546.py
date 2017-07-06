n = int(input())
dfdf = input().split()
list1 = []
for i in range(0,n):
    list1.append(int(dfdf[i]))

maxi = max(list1)
total = 0

for i in range(0,n):
    total += (list1[i]/maxi)*100

ans = total/n


print("%.2f" % round(ans,2))