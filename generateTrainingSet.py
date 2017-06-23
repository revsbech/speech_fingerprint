import os
import soundfile as sf
import pickle
from fingerprint import audio_fingerprint

names = ['daniel', 'jon', 'juri', 'mads', 'janerik', 'sidsel']
outputFilename = 'traindata.pkl'

def getTrainDataForPerson( personName, fileName):
	samplerate = 44100
	windowsSize = int(0.02 * samplerate)
	file = 'input_samples/' + fileName
	print "-- Parsing filename: " + file
	signalData, samplerate = sf.read(file)
	data = {'person': personName, 'filename': file, 'fingerprints': audio_fingerprint(signalData[...,0], windowSize = windowsSize, sampleRate = samplerate, no_samples=6)}
	return data

outArr = []
for personName in names:
	print personName
	outArr.append(getTrainDataForPerson(personName, personName + '.wav'))
	#files = [ x for x in os.listdir('input_samples/' + personName)]
	#for fileName in files:
	#	trainData = getTrainDataForPerson( personName, fileName )
	#	outArr.append(trainData)

print "Generated traindata from", len(outArr), " inputs"
pickle.dump(outArr,  open( outputFilename, "wb" ))


