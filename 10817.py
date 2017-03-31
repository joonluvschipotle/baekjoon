inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])

list1 = [a,b,c]
list1.remove(max(list1))

print (max(list1))
