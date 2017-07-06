import math
b = input()
count = math.ceil(len(b)/3)

df = []
for i in range(0,len(b)):
    df.append(int(b[i]))

octa = []
for i in range(0,count):
    dummy = df[-3:]
    del df[-3:]
    if len(dummy) > 2:
        octad = dummy[0]*4 + dummy[1]*2 + dummy[2]*1
    elif len(dummy) > 1:
        octad = dummy[0]*2 + dummy[1]*1
    else:
        octad = dummy[0]*1
    octa.append(octad)

for i in range(0,len(octa)):
    print(octa[len(octa)-i-1],end="")
