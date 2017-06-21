import soundfile as sf
import sounddevice as sd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import wave
wsize = 4096
wratio = 0.5
samplerate = 16000

signal, samplerate = sf.read('test.raw', channels=1, samplerate=16000,  format='RAW', subtype='PCM_16')


Time=np.linspace(0, len(signal)/samplerate, num=len(signal))


#plt.show()
#sd.play(signal, samplerate)



#Y = np.fft.fft(signal)
#plt.plot(Time, Y)
#plt.show()



ax1 = plt.subplot(311)
plt.plot(Time,signal)
#plt.subplot(312, sharex=ax1)
plt.subplot(312)

spectrum, freqs, t, im = plt.specgram(
        signal,
        NFFT=wsize,
        Fs=4,
        window=mlab.window_hanning,
        noverlap=int(wsize * wratio))


index = 17

print len(spectrum)

plt.subplot(313)


#plt.plot(spectrum[index])
#print spectrum[index]
#print len(spectrum[index])
#print len(t)
#print len(freqs)
#print len(spectrum[...,index])
print "Snapshow taken after", t[index], " seconds"
plt.plot(freqs,spectrum[...,index])
plt.show()



