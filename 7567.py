a = input()

def checkNull(df,x):
    try:
        return df[x]
    except IndexError:
        return None


for i in range(0,len(a)):
    