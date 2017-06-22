from time import time
import numpy as np
from sklearn.naive_bayes import GaussianNB

from tools import preprocess
features_train, labels_train, features_test, labels_test = preprocess()

t0 = time()

#clf = GaussianNB()
#clf.fit(features_train, labels_train)
#print "training time:", round(time()-t0, 3), "s"
t0 = time()
#print "Predict: ", clf.predict(features_test)