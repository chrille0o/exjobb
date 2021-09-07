import glob
import os
from Misc.readWrite import saveData


def convertPath(path):
    separator = os.path.sep
    if separator != '/':
        path = path.replace(os.path.sep, '/')
    return path


filenames = []
for filename in glob.iglob('Data/LibriSpeech/train-clean-100/**', recursive=True):
    if os.path.isfile(filename):  # filter dirs
        filenames.append(convertPath(filename))

saveData('paths', filenames)
