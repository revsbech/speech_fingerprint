import soundfile as sf
from fingerprint import audio_fingerprint

filename = 'test.raw'
samplerate = 16000

signalData, samplerate = sf.read(filename, channels=1, samplerate=samplerate,  format='RAW', subtype='PCM_16')

data = {'filename': filename, 'fingerprints': audio_fingerprint(signalData, windowSize = 4092, sampleRate = samplerate)}
print data
