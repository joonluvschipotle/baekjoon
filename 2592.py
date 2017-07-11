df = []
for i in range(0,10):
    df.append(int(input()))

df.sort()
mostfreq = [0]*1001

avg = 0
for i in df:
    avg += i
    mostfreq[i]+=1

ans = max(mostfreq)

print(avg//10)
print(mostfreq.index(ans))
