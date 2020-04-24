#http://builds.libav.org/windows/release-gpl/
from pydub import AudioSegment

x = AudioSegment.from_wav("111.wav")
x.export("file.mp3", format="mp3")