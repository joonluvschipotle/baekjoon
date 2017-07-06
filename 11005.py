a = input().split()
n = int(a[0])
b = int(a[1])
di = chr(b+54)

digits = ""

rang = [4,3,2,1,0]

if b > 9:
    for i in rang:
        if n//(b**i) > 1:
            dummy = n//(b**i)
            print(dummy)
            if dummy > 9:
                digits+=chr(dummy+55)
            else:
                digits+=str(dummy)
        n -= dummy*b**i

    print(digits)
else:
    for i in rang:
        if n//(b**i) > 1:
            dummy = n//(b**i)
            digits+=str(dummy)
        n -= dummy*b**i

    print(digits)

"""
chr 65 -> A -> 10
chr 90 -> Z -> 35
"""
