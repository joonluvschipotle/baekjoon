a = int(input())
digit = int(str(a)[-1])
total = 0

if digit == 5 or digit == 0:
    total = a//5
elif digit == 3 or digit == 9:
    total += (a-digit)//5
    total += digit//3
elif digit == 6 and a < 10:
    total += a//3
elif digit == 6 and a > 10:
    a -= 16
    total += a//5
    total += 4
elif digit == 1:
    a -= 11
    total += a//5
    total += 3
elif digit == 2:
    a -= 12
    total += a//5
    total += 4
elif digit == 4 and a > 20:
    a -= 24
    total += a//5
    total += 8
elif digit == 7 and a > 20:
    a -= 27
    total += a//5
    total += 9
elif digit == 8:
    a -= 3
    total += a//5
    total += 1
else:
    total = -1

print (total)