import soundfile as sf
from fingerprint import audio_fingerprint

filename = 'test.raw'
samplerate = 16000

signalData, samplerate = sf.read(filename, channels=1, samplerate=samplerate,  format='RAW', subtype='PCM_16')
print "Number of points", len(signalData)
print "Which is ", len(signalData)/samplerate, "seconds of audio"
# Desided windowssize is 5 per seconds
windowsSize = int(0.2 * samplerate)
data = {'filename': filename, 'fingerprints': audio_fingerprint(signalData, windowSize = windowsSize, sampleRate = samplerate)}
print len(data["fingerprints"])
