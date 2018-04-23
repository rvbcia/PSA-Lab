import wave, struct, math

samplingRate = 44100.0 # Hertz
lenght = 5.0           # seconds

# Use different frequencies for the left and right channels
rightFreq = 220.00  # A
leftFreq =  440.00  # C
maxAmplitude = 32767.0
leftGain = 0.5
rightGain = 0.5

wavef = wave.open('different_freqs.wav','w')
wavef.setnchannels(2) # stereo
wavef.setsampwidth(2) 
wavef.setframerate(samplingRate)

for i in range(int(lenght * samplingRate)):
    l = int(leftGain*maxAmplitude*math.sin(leftFreq*2.0*math.pi*float(i)/float(samplingRate)))
    r = int(rightGain*maxAmplitude*math.sin(rightFreq*2.0*math.pi*float(i)/float(samplingRate)))
    wavef.writeframesraw( struct.pack('<hh', l, r ) )

wavef.writeframes('')
wavef.close()


