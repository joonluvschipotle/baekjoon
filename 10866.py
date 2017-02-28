trial = int(input())
DEQUE = []

def push_front(x):
    DEQUE.insert(0,x)

def push_back(x):
    DEQUE.append(x)

def pop_front():
    if len(DEQUE) == 0:
        print (-1)
    else:
        print (DEQUE.pop(0))

def pop_back():
    if len(DEQUE) == 0:
        print (-1)
    else:
        print (DEQUE.pop())

def size():
    print (len(DEQUE))

def empty():
    if len(DEQUE) == 0:
        print (1)
    else:
        print (0)

def front():
    if len(DEQUE) == 0:
        print (-1)
    else:
        print (DEQUE[0])

def back():
    if len(DEQUE) == 0:
        print (-1)
    else:
        print (DEQUE[-1])


for i in range(0,trial):
    inputs = input().split()
    if inputs[0] == "push_front":
        push_front(int(inputs[1]))
    elif inputs[0] == "push_back":
        push_back(int(inputs[1]))
    elif inputs[0] == "pop_front":
        pop_front()
    elif inputs[0] == "pop_back":
        pop_back()
    elif inputs[0] == "size":
        size()
    elif inputs[0] == "empty":
        empty()
    elif inputs[0] == "front":
        front()
    elif inputs[0] == "back":
        back()
