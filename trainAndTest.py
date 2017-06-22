import soundfile as sf
from fingerprint import audio_fingerprint
from time import time
import numpy as np
from sklearn.naive_bayes import GaussianNB

from tools import preprocess
features_train, labels_train, features_test, labels_test = preprocess()


t0 = time()
clf = GaussianNB()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

##################### Predict #####################

#filename = 'test_data/test2.raw'
filename = 'input_samples/martin/aa498cd4-9d92-4ebf-b1e5-b82421f5d655.raw'
samplerate = 16000
windowsSize = int(0.2 * samplerate)

signalData, samplerate = sf.read(filename, channels=1, samplerate=samplerate,  format='RAW', subtype='PCM_16')
fingerprints = audio_fingerprint(signalData, windowSize = windowsSize, sampleRate = samplerate)

print "I have ", len(fingerprints), " fingerprints to test"

features_test = []


for i in range(0, len(fingerprints)):
	no_values = len(fingerprints[i]['peak_value'])
	for n in range(0, no_values):
		freq = fingerprints[i]['peak_value'][n]
		value = fingerprints[i]['peak_frequency'][n]
		features_test.append([freq,value])

print "I have ", len(features_test), " samples to test"
predictionArr = clf.predict(features_test)
counts = {'daniel': 0, 'martin': 0}

for i in range(0, len(predictionArr)):

	if predictionArr[i] == "daniel":
		counts['daniel'] = counts['daniel'] + 1

	if predictionArr[i] == "martin":
		counts['daniel'] = counts['martin'] + 1

print counts