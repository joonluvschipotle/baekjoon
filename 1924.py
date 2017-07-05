n = input().split()
a = int(n[0])
b = int(n[1])
days = b
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(1,a):
    days+=month[i]

print (day[days%7])
