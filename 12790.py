testcase = input()
answers = []

def calcCP():
    stats = input()
    statlist = stats.split()
    hp = int(statlist[0]) + int(statlist[4])
    mp = int(statlist[1]) + int(statlist[5])
    atk = int(statlist[2]) + int(statlist[6])
    df = int(statlist[3]) + int(statlist[7])
    if hp < 0: hp = 1
    if mp < 0: mp = 1
    if atk < 0: atk = 0
    answers.append((1*hp)+(5*mp)+(2*atk)+(2*df))

for n in range(0,int(testcase)):
    calcCP()

for i in answers:
    print (i)
