n = int(input())
numbers = []
for i in range(0,n):
    numbers.append(int(input()))

def quicksort(x):
    if len(x) <= 1:
        return x
    pivot = x[round(len(x)/2)]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)
    return quicksort(less) + equal + quicksort(more)

ans = quicksort(numbers)

for i in ans:
    print (i)
