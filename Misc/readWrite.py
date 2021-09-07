import pickle


def readFile(filename):
    infile = open(filename, 'rb')
    variable = pickle.load(infile)
    infile.close()
    return variable


def saveData(filename, data):
    outfile = open(filename, 'wb')
    pickle.dump(data, outfile)
    outfile.close()
    return 0
