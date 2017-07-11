scores = []
b = []
for i in range(0,8):
    dummy = int(input())
    scores.append(dummy)
    b.append(dummy)


store = []
total = 0
for i in range(0,5):
    maxi = max(scores)
    store.append(b.index(maxi)+1)
    total += maxi
    scores.pop(scores.index(maxi))

print(total)
store.sort()
for i in store:
    print(i,end=" ")