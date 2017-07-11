secs = 0
for i in range(0,4):
    secs += int(input())

print(secs//60)
secs %= 60
print(secs)