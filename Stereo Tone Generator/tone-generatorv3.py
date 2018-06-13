
import pyaudio
import numpy as np

p = pyaudio.PyAudio()

print "Witaj w generatorze tonow! By wywolac ton wpisz: \n generate(czestotliwosc, czas trwania)\ngdzie zamiast slow wpisz wartosci w Herzach i sekundach."

def generate(f, duration):

    volume = 0.5
    fs = 44100

    # generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*(duration*2))*(f/2)/fs)).astype(np.float32) # f/2 because of 2 channels - stereo and duration*2

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                channels=2,
                rate=fs,
                output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume*samples)

    stream.stop_stream()
    stream.close()

    p.terminate()

generate(100, 5)
