import pickle
import cPickle
import numpy as np


def loadData():
	filename = 'traindata.pkl'
	traindata_file_handler = open(filename, "r")
	data = pickle.load(traindata_file_handler)
	traindata_file_handler.close()
	return data

def preprocess():
	data = loadData()
	print "Loaded traindata from ", len(data), " datafile"

	trainFeatures = []
	trainLabels = []

	for index in range(0, len(data)):
		no_fingerprints = len(data[index]["fingerprints"])
		for fingerprint_index in range(0, no_fingerprints):

			testData = data[index]["fingerprints"][fingerprint_index]
			trainFeatures.append(testData["peak_frequency"])
			trainLabels.append(data[index]['person'])
			#no_points = len(testData['peak_value'])
			#for i in range(0,no_points):
			#	value = testData["peak_value"][i]
			#	freq = testData["peak_frequency"][i]
			#	trainFeatures.append([freq,value])
			#	trainLabels.append(data[index]['person'])


	cutoff = 1
	total_no_features = len(trainFeatures);

	return np.array(trainFeatures[cutoff:total_no_features]), np.array(trainLabels[cutoff:total_no_features]),trainFeatures[0:cutoff],trainLabels[0:cutoff]

