a = input()
b = input()
basket1 = a.split()
basket2 = b.split()

move1 = int(basket1[0]) + int(basket2[1])
move2 = int(basket1[1]) + int(basket2[0])

if move1 < move2:
    print (move1)
elif move1 > move2:
    print (move2)
else:
    print (move1)
