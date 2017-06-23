import soundfile as sf
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from fingerprint import audio_fingerprint

filename = 'input_samples/old/martin/aa498cd4-9d92-4ebf-b1e5-b82421f5d655.raw'
samplerate = 16000

signalData, samplerate = sf.read(filename, channels=1, samplerate=samplerate,  format='RAW', subtype='PCM_16')

############## PLOT 1 ###############
plt.subplot(311)
plt.plot(signalData)

############## PLOT 2 ###############
plt.subplot(312)
spectrum, freqs, t, im = plt.specgram(
        signalData,
        NFFT=4092,
        Fs=samplerate,
        window=mlab.window_hanning,
        noverlap=0.0)


xxx = audio_fingerprint(signalData, windowSize = 4092, sampleRate = samplerate)
sampleIndex = 6
fingerprint = xxx[sampleIndex]
sampleData = spectrum[...,sampleIndex]


############## PLOT 3 #################
plt.subplot(313)
print "Snapshot taken after", fingerprint["window_start_position"], " seconds"
plt.plot(freqs,sampleData)
print fingerprint["peak_frequency"]
#"peak_value"
plt.scatter(fingerprint["peak_frequency"], fingerprint["peak_value"], s=30)


#plt.plot(sampleData)
#plt.scatter(max_peaks, peak_values, s=30)




plt.show();
#print data[sampleIndex]
