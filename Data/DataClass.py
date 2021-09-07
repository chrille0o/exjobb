from Misc.readWrite import readFile


class Data():
    def __init__(self):
        self.tags = readFile("Data/word2phonetics/tags")
        self.phones = self.tags.keys()
        self.words = readFile("Data/word2phonetics/words")
        self.sounds = readFile("Data/word2phonetics/phonemes")
        self.filenames = readFile("Data/word2phonetics/paths")
        self.soundPaths = list()
        self.textPaths = list()
        for x in self.filenames:
            if x.endswith('.flac'):
                self.soundPaths.append(x)
            elif x.endswith('.txt'):
                self.textPaths.append(x)
