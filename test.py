#from Misc.readFile import readFile
from Data.DataClass import Data
from Misc.plotSpec import plotSpec
import torch
import torchaudio
import torchaudio.functional as F
import torchaudio.transforms as T
data = Data()

waveform, sample_rate = torchaudio.load(data.filenames[3512])
print(waveform.size()[1]/512)
#slices = torch.reshape(waveform, (int(waveform.size()[1]/512), 512))

# sample_rate = 16000
# 256 slices / second gives 16 ms slices


n_fft = 256

# Number of mel bands
# (frequency discretization leveles)
n_mels = 64

mel_filters = T.MelSpectrogram(
    sample_rate=sample_rate,
    n_fft=n_fft,
    hop_length=512,
    n_mels=n_mels,
    f_min=200,
    f_max=7000
)

plotSpec(waveform, mel_filters)
