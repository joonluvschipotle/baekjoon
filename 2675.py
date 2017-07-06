t = int(input())

for k in range(0,t):
    df = input().split()
    n = int(df[0])
    string = df[1]
    for i in range(0,len(string)):
        for j in range(0,n):
            print(string[i],end="")