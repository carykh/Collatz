import numpy as np
from scipy.io.wavfile import write
import subprocess
import audio2numpy as a2n
from scipy.signal import resample
import sys



def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

def speedUp(audio, factor):
    if factor == 1.0:
        return audio
    
    # Speed up by resampling to fewer points
    return resample(audio, int(len(audio) / factor))  # 1.33x speed

FR = 60
SR = 44100

files = ["drop", "whoosh", "error"]
audios = [None]*len(files)
for f in range(len(files)):
    audio, _ = a2n.audio_from_file(f"CollatzMulti/data/{files[f]}.wav")
    audios[f] = audio
    
    
tag = sys.argv[1] # for example, "python sounder.py corner0"
    
f = open(f"CollatzMulti/{tag}.txt","r+")
lines = f.read().split("\n")[:-1]
f.close()

leng = round(get_length(f"CollatzMulti/collatz_multiverse_{tag}.mp4")*SR)
arr = np.zeros((leng, 2))


for i in range(len(lines)):
    parts = lines[i].split(",")
    
    frames = int(int(parts[0])/FR*SR)
    type_ = int(parts[1])
    speed_up = float(parts[2])
    
    audio = speedUp(audios[type_], speed_up)
    if frames+len(audio) >= len(arr):
        break
        
        
    volumes = [1.0,0.4,1.0]
    volume = volumes[type_]/pow(speed_up,5.3) # higher-pitched audio is quieter
        
    arr[frames:frames+len(audio)] += audio*volume


scaled = np.int16(arr / np.max(np.abs(arr)) * 32767)
write(f"{tag}_audio_no_high.wav", SR, scaled)