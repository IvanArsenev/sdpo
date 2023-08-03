from pydub import AudioSegment
from pydub.playback import play
import time
def play_m(name):
	sound = AudioSegment.from_wav(name) 
	play(sound)
	