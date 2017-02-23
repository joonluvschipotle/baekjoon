a = input()
b = input()
c = a.split()
sec = (int(c[2]) + int(b))%60
mn = int(c[1]) + int((int(c[2]) + int(b))/60)%60
hr = int(int(int(int(c[1]) + int((int(c[2]) + int(b))/60))/60) + int(c[0]))

if hr > 23:
    hr %= 24

if mn > 59:
    mn %= 60

print (str(hr) + " " + str(mn) + " " + str(sec))
