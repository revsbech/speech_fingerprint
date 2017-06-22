import soundfile as sf
import sounddevice as sd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import pickle
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import (generate_binary_structure,
                                      iterate_structure, binary_erosion)
from scipy import signal
from detect_peak import detect_peaks

#The sice of the window usedn then doing the FFT
wsize = 4092
wratio = 0.0
samplerate = 16000
#The sample index
index = 1

filename = 'test.raw'
outputFilename = 'dataoutput.b'

signalData, samplerate = sf.read(filename, channels=1, samplerate=samplerate,  format='RAW', subtype='PCM_16')
print "Data length: ", len(signalData)
print "Slitting timeseries into ", len(signalData) / wsize, " windows"
numberOfWindows = len(signalData) / wsize
#The timespan of the clip
Time=np.linspace(0, len(signalData)/samplerate, num=len(signalData))



ax1 = plt.subplot(311)
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
plt.plot(Time,signalData)

plt.subplot(312)
#plt.subplot(312, sharex=ax1)


spectrum, freqs, t, im = plt.specgram(
        signalData,
        NFFT=wsize,
        Fs=samplerate,
        window=mlab.window_hanning,
        noverlap=int(wsize * wratio))



outArr = []
for x in range(0, numberOfWindows):
	sampleData = spectrum[...,x]

	#Take the log
	#sampleData = 10 * np.log10(1000 * sampleData)

	ax3 = plt.subplot(313)

	#Find the peaks that are greater than twice the meanVAlue
	meanValue = np.mean(sampleData)
	max_peaks = detect_peaks(sampleData, mph=meanValue * 2)
	peak_values = sampleData[max_peaks]

	print "Snapshow taken after", t[x], " seconds"
	plt.plot(sampleData)
	plt.scatter(max_peaks, peak_values, s=30)

	outdata = {'Sourcefilename': filename, 'window_start_position': t[x], 'window_number': x, 'peak_frequency': freqs[max_peaks], 'peak_value': peak_values}
	outArr.append(outdata)


pickle.dump(outArr,  open( outputFilename, "wb" ))


#print outArr
#plt.show()


