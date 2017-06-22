import numpy as np
import pickle
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from detect_peak import detect_peaks


def audio_fingerprint(signalData, windowSize, sampleRate, overlapRatio = 0):
	#Varibles
	numberOfWindows = len(signalData) / windowSize
	overlap = int(windowSize
	 * overlapRatio)

	print "Data length: ", len(signalData)
	print "Slitting timeseries into ", numberOfWindows

	#The timespan of the clip
	Time=np.linspace(0, len(signalData)/sampleRate, num=len(signalData))

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

		#Find the peaks that are greater than twice the meanVAlue
		meanValue = np.mean(sampleData)
		max_peaks = detect_peaks(sampleData, mph=meanValue * 2)
		peak_values = sampleData[max_peaks]

		print "Snapshow taken after", t[x], " seconds"
		plt.plot(sampleData)
		plt.scatter(max_peaks, peak_values, s=30)

		outdata = {'window_start_position': t[x], 'window_number': x, 'peak_frequency': freqs[max_peaks], 'peak_value': peak_values}
		outArr.append(outdata)

	return outArr



