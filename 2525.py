a = input()
b = input()
c = a.split()
mn = (int(c[1]) + int(b))%60
hr = int(c[0]) + int((int(c[1]) + int(b))/60)

if hr > 23:
    hr %= 24

print (str(hr) + " " + str(mn))
