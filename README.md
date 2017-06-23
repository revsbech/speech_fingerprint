Python based machine learning framework for detecting human voices
==================================================================

This project is a testlab for seing if its possible with rather simple Machine Learning (ML) algotihms
to detect the author of a given audio clip.

It workds by taking a set on wav input files, and spoits it into small parts of typically 0.2 seconds. 
A fingerprint is then taken for each segment, and stores in the training data.


Fingerprinting
--------------
Currently the fingerprinting consists of making a Fourier transform, then detect the N-highest peaks and
saving the frequencies these peak appear at (the aboslute value is also stored, but not used).

These six numbers then corresponds to the fingerprint og the given small soundclip. This is very crude, 
and should be optimzed.

Createing docker container
==========================

```docker build -f docker/Dockerfile -t pcodk/human-detection .```

Generating learning set
-----------------------

The script generateTrainingSet will parse a bunch of waw files, and generate fingerprints for each bit of the soundfiles
and then save the output ti traindata.pkl file which can then later be used to train ML algorithms.

```docker run pcodk/human-detection python generateTrainingSet.py```

Testing data
------------

After the traingin data is genereated, a single wav soundfile can be tested agains the training data

```docker run pcodk/human-detection python trainAndTest.py test_je.wav```


Recording sound on the MAC
=======

Record

```sox -d test_je.wav```

play

```afplay test_je.wav```