#!/usr/bin/python
''' \
USAGE:  trainAndTest filename
    filename : The waw file to test against the training set

'''
from __future__ import division
import sys

import soundfile as sf
from fingerprint import audio_fingerprint
from time import time
import numpy as np

from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

in_arr = sys.argv

if len(sys.argv) != 2:

	print('Error: Please specify filename')
	print (__doc__)
	exit()

print " ** Loading %s to test " % in_arr[1]
filename = in_arr[1]

#####################  Get training data
from tools import preprocess
features_train, labels_train, features_test, labels_test = preprocess()

print "I have ", len(features_train), " training features"
print "I have ", len(labels_train), " training labels"

t0 = time()
clf = GaussianNB()
#clf = tree.DecisionTreeClassifier(min_samples_split=2)
clf = RandomForestClassifier(n_estimators=25, min_samples_split = 4)
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

##################### Predict #####################

signalData, samplerate = sf.read(filename)
windowsSize = int(0.02 * samplerate)

signalData, samplerate = sf.read(filename)
fingerprints = audio_fingerprint(signalData[...,0], windowSize = windowsSize, sampleRate = samplerate, no_samples=6)

print "I have ", len(fingerprints), " fingerprints to test"
features_test = []

for i in range(0, len(fingerprints)):
	no_values = len(fingerprints[i]['peak_frequency'])
	features_test.append(fingerprints[i]["peak_frequency"])

predictionArr = clf.predict(features_test)

counts = {'daniel': 0, 'martin': 0, 'juri': 0, 'mads': 0, 'janerik': 0, 'jon': 0, 'sidsel': 0,'kasper': 0}
total = 0
for i in range(0, len(predictionArr)):
	counts[predictionArr[i]] = counts[predictionArr[i]] + 1
	total = total + 1

mostProbable = "unknown"
max = 0
for name in counts:
	value = counts[name]
	percentage = value / total * 100

	print '%12s: %4.2f%s (%d)' % (name, percentage,'%', value)
	if max < value:
		max = value
		mostProbable = name

print counts
per = max / total * 100
print "********************************************"
print " "
print 'Most probably %s speaking. Confidence: %4.2f%s' % (mostProbable, per, '%')
print " "
print "********************************************"
