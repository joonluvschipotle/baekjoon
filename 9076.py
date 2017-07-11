n = int(input())
for i in range(0,n):
    a = input().split()
    df = []
    for i in a:
        df.append(int(i))

    del df[df.index(min(df))]
    del df[df.index(max(df))]
    if max(df)-min(df) > 3:
        print("KIN")
    else:
        print(df[0]+df[1]+df[2])