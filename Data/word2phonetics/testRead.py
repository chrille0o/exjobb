import pickle


def readFile(filename):
    infile = open(filename, 'rb')
    variable = pickle.load(infile)
    infile.close()
    return variable


test = readFile('tags')
print(test.keys())
