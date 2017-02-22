a = input()
alph = [0] * 26
for num in range(0,len(a)):
    alph[ord(a[num])-97] += 1

for alpha in alph:
    print (str(alpha) + " ",end='')
