import operator
ops = { "+": operator.add, "-": operator.sub }

a = input()
if a[0] != "F":
    ans = (69-ord(a[0]))
else: ans = "0"
if (len(a) == 1) or a[1] =="0":
    print (str(ans)+".0")
else: print (ops[a[1]](ans,0.3))
