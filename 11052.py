n = int(input())
pdum = input().split()
p = [0]
for i in range(0,n):
    p.append(int(pdum[i]))
price = [0]*1001

for i in range(1,n+1):
    for j in range(1,i+1):
        if price[i] < price[i-j] + p[j]:
            price[i] = price[i-j] + p[j]
print (price[n])