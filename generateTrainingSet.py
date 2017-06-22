import os
import soundfile as sf
import pickle
from fingerprint import audio_fingerprint

directories = ['daniel', 'martin']
outputFilename = 'traindata.pkl'


def getTrainDataForPerson( personName, fileName):
	samplerate = 16000
	windowsSize = int(0.2 * samplerate)
	file = 'input_samples/' + personName + '/' + fileName
	print "-- Parsing filename: " + file
	signalData, samplerate = sf.read(file, channels=1, samplerate=samplerate,  format='RAW', subtype='PCM_16')
	data = {'person': personName, 'filename': file, 'fingerprints': audio_fingerprint(signalData, windowSize = windowsSize, sampleRate = samplerate)}
	return data


outArr = []
for personName in directories:
	print personName
	files = [ x for x in os.listdir('input_samples/' + personName)]
	for fileName in files:
		trainData = getTrainDataForPerson( personName, fileName )
		outArr.append(trainData)

print "Generated traindata from", len(outArr), " inputs"
pickle.dump(outArr,  open( outputFilename, "wb" ))


