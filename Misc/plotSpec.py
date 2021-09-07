import numpy as np
from matplotlib import pyplot as plt
import torch


def plotSpec(waveform, filter):
    ms = filter(waveform)
    ms2 = torch.squeeze(ms).numpy()
    plt.imshow(ms2, cmap='hot')
    plt.show()
    return 0
