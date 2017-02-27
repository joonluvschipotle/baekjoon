info = input().split()
inputs = []
lists = [[] for row in range(100)]
scores = [0 for row in range(100)]
durations = [0 for row in range(100)]

for i in range(0,int(info[2])):
    dummy = input().split()
    lists[int(dummy[1])-1].append(dummy)

for stats in lists:
    for stat in stats:
        if stat[3] == "AC":
            dummy = int(stat[2])
            dumindex = lists.index(stats)
            scores[dumindex] += 1
            for i in stats:
                if int(i[2])==dummy:
                    durations[dumindex] += int(i[0])
                    if i[3] == "AC":
                        break

for i in range(0,int(info[0])):
    print (str(i+1) + " " + str(scores[i]) + " " + str(durations[i]))
