total = []
for i in range(0,5):
    total.append(int(input()))

score = 0
for i in total:
    if i > 40:
        score += i
    else:
        score += 40

print(score//5)