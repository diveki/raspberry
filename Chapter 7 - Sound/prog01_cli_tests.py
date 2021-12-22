import pyaudio
import struct
import wave
import numpy as np
import matplotlib.pyplot as plt

#Calling pyadio module and starting recording 
p = pyaudio.PyAudio()

p.get_default_input_device_info()
p.get_default_output_device_info()
p.get_device_count()
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))

#defining audio variables
chunk = 2**11
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
device_index = 1
outputFile = 'outputFile1.wav'

stream = p.open(format=FORMAT,
            channels=CHANNELS, 
            input_device_index=device_index,
            rate=RATE, 
            input=True,
            frames_per_buffer=chunk)

stream.start_stream()
print("Starting!")
 
#Recording data until under threshold
    
#Converting chunk data into integers
data = stream.read(chunk)
f = np.frombuffer(data, dtype=np.int16)

#Stopping recording   
stream.stop_stream()
stream.close()
p.terminate()
print("Ending recording!")
    
     
#Saving file with wave module    
wf = wave.open(outputFile, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(data))
wf.close()


######### Recording for a given time
# ha RATE > chunk => 1 s alatt RATE/chunk db rogzites tortenik, igy X masodperc alatt X*RATE/chunk rogzites kell

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
device_index = 1
record_time = 5  # in seconds

stream = p.open(format=FORMAT,
            channels=CHANNELS, 
            input_device_index=device_index,
            rate=RATE, 
            input=True,
            frames_per_buffer=chunk)

stream.start_stream()

frames = np.array([])
for i in range(0, round(RATE*record_time / chunk)):
    data = stream.read(chunk)
    frames = np.append(frames, np.frombuffer(data, dtype=np.int16))

# teszt, len(frames) / RATE = vetelezesi ido

#Stopping recording   
stream.stop_stream()
stream.close()
p.terminate()


# folyamatos rogzites
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
device_index = 1
record_time = 5  # in seconds

stream = p.open(format=FORMAT,
            channels=CHANNELS, 
            input_device_index=device_index,
            rate=RATE, 
            input=True,
            frames_per_buffer=chunk)

stream.start_stream()

while True:
    data = stream.read(chunk)
    frames = np.append(frames, np.frombuffer(data, dtype=np.int16))
    print(np.mean(frames))