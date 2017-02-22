
def aloop (testcase):
    recorded = input()
    foxsounds = recorded.split()
    animalSounds = []
    while(1):
        soundInput = input()
        if soundInput == "what does the fox say?":
            break
        else:
            animalSounds.append(soundInput)
    sounds = []
    for element in animalSounds:
        sounds.append(element.split()[2])
    for sound in sounds:
        for foxsound in foxsounds:
            if foxsound == sound:
                num = foxsounds.count(foxsound)
                for i in range(0,num):
                    foxsounds.remove(foxsound)
    print (foxsounds)

numOfCases = input()
aloop(numOfCases)
