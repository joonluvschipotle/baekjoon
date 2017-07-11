month = int(input())
date = int(input())

if month==2 and date==18:
    print("Special")
elif month > 2:
    print("After")
elif month == 1:
    print("Before")
else:
    if date < 18:
        print("Before")
    else:
        print("After")