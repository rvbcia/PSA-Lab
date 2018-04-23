import wave, struct, math

samplingRate = 44100.0  # Hertz
lenght = 10.0           # seconds
freq = 440.0            # Hertz

wavef = wave.open('sinus_440.wav','w')
wavef.setnchannels(1) # mono
wavef.setsampwidth(2) 
wavef.setframerate(samplingRate)

for i in range(int(lenght * samplingRate)):
    value = int(32767.0*math.sin(freq*2.0*math.pi*float(i)/float(samplingRate)))
    data = struct.pack('<h', value)
    wavef.writeframesraw( data )

wavef.writeframes('')
wavef.close()


