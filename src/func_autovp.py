##########################################
# Project: Methods for generating and playing voice with VoicePeak
# Author: jolon
# Description: methods called from main
##########################################

# Import moudules
import argparse
import subprocess
from pydub import AudioSegment
from pydub.playback import play
import warnings
warnings.simplefilter('ignore')  # デバッグ時は表示させる

df_out_file = 'test.wav'
df_vp_path = '/Applications/voicepeak.app/Contents/MacOS/voicepeak'
df_narrator = 'Koharu Rikka'
df_emotion = 'hightension=100'

# VoicePeakでボイスのwavデータを生成
def generate_voice(query, out_file=df_out_file, narrator=df_narrator, vp_path=df_vp_path, emotion=df_emotion):
  # Generate voice
  # print('Processing: ' + command + ' -s ' + query + ' -n ' + narrator + ' -o ' + out_file)
  input = [vp_path, '-s', query, '-n', narrator, '-o', out_file]
  if emotion is not False:
    input = input + ['-e', emotion]
  subprocess.run(input)

# wavファイルを再生
def play_voice(input, format="wav"):
  # Play voice
  sound = AudioSegment.from_file(input, format=format)
  play(sound)
  
