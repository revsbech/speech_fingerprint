import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from detect_peak import detect_peaks


def audio_fingerprint(signalData, windowSize, sampleRate, overlapRatio = 0, no_samples=6):

	#Varibles
	numberOfWindows = len(signalData) / windowSize
	overlap = int(windowSize
	 * overlapRatio)

	#print "Data length: ", len(signalData)
	#print "Slitting timeseries into ", numberOfWindows

	#The timespan of the clip
	Time=np.linspace(0, len(signalData)/sampleRate, num=len(signalData))

	#signal.spectrogram(signalData, fs=sampleRate,
	spectrum, freqs, t, im = plt.specgram(
		signalData,
		NFFT=windowSize,
		Fs=sampleRate,
		window=mlab.window_hanning,
		noverlap=overlap)
	outArr = []
	for x in range(0, numberOfWindows):
		sampleData = spectrum[...,x]

		#Take the log
		#sampleData = 10 * np.log10(1000 * sampleData)

		#Find the peaks that are greater than twice the meanValue
		meanValue = np.mean(sampleData)
		max_peaks = detect_peaks(sampleData, mph=meanValue * 2)
		peak_values = sampleData[max_peaks]

		#temp = []
		#for i in range(0, len(peak_values)):
		#	temp.append((fremax_peaks[i], peak_values[i]])
		#print temp
		#print peak_values

		#Sort by maximum peak values
		ind = np.lexsort((max_peaks,peak_values))

		#Take last elements
		ind = ind[len(ind) - no_samples:]

		#print "Peak values: ", peak_values[ind]
		#print "Max peaks: ", max_peaks[ind]
		#print "Indexes: ", ind
		#print "Frequencies", freqs[max_peaks[ind]]
		peak_freqs = freqs[max_peaks[ind]]
		if len(peak_freqs) < no_samples:
			peak_freqs.resize(no_samples)

		peak_values = peak_values[ind]
		if len(peak_values) < no_samples:
			peak_values.resize(no_samples)

		outdata = {'window_start_position': t[x], 'window_number': x, 'peak_frequency': peak_freqs, 'peak_value': peak_values}
		outArr.append(outdata)

	return outArr



