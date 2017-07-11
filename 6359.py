t = int(input())

for cases in range(0,t):
    n = int(input())
    rooms = [0]*(n+1)
    count = 0

def checkNull(df,j,i):
    try:
        return df[j*i]
    except IndexError:
        return None

for i in range(1,n):
    for j in range(1,n-i):
        if checkNull(rooms,j,i) == 0:
            rooms[i*j] = 1
            count+=1
        elif checkNull(rooms,j,i) == 1:
            rooms[i*j] = 0
            count-=1

    print (count)

