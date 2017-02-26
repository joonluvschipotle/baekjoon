cases = int(input())
inputs = []
for i in range(0,cases):
    inputs.append(input())

for i in range(0,cases):
    dummylist = cases[i].split()
    if ord(inputs[i][0]) > 96 and ord(inputs[i][0]) < 123:
        dummy = inputs[i][0]
        inputs[i][0] = chr(ord(dummy)-32)
    for j in range(0,len(inputs[i])):
        if ord(inputs[i][j]) == 32:
            dummy = inputs[i][j]
            inputs[i][j+1] == chr(ord(j)-32)

for i in inputs:
    print (i)
