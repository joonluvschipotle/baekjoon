a = [0]*31

for i in range(0,28):
    a[int(input())] = 1

df = []

for i in range(0,30):
    if a[i] == 0:
        df.append(i)

print (df[1])
print (df[2])