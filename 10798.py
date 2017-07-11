df = []
for i in range(0,5):
    df.append(input())

def checkNull(df,j,i):
    try:
        return df[j][i]
    except IndexError:
        return None

for i in range(0,15):
    for j in range(0,15):
        if checkNull(df,j,i) is not None:
            print(df[j][i],end="")
