
import pickle

with open("beep-1.0") as f:
    lines = f.readlines()

data = []

for line in lines:
    data.append(line.split("\t"))


for line in data:
    line[:] = [x for x in line if x]

for line in data:
    line[-1] = line[-1].split()
    line[-1].pop()


words = []
sounds = []
tags = {}

for line in data:
    words.append(line[0])
    sounds.append(line[-1])

    for sound in line[-1]:
        if sound not in tags:  # and len(sound) <= 3:
            tags[sound] = len(tags)


for i, line in enumerate(sounds):
    for j, sound in enumerate(line):
        sounds[i][j] = tags[sounds[i][j]]


def saveData(filename, data):
    outfile = open(filename, 'wb')
    pickle.dump(data, outfile)
    outfile.close()
    return 0


saveData('data', data)
saveData('words', words)
saveData('sounds', sounds)
saveData('tags', tags)


# There are 44 sounds in the english language so this is good including sil (silent).
