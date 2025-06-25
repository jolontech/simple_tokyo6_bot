##########################################
# Project: Methods for generating and playing voice with VOICEPEAK
# Author: jolon
# Description: methods called from main
##########################################

# Import moudules
import argparse
import configparser
import os
import sys
import subprocess
import random
from pydub import AudioSegment
from pydub.playback import play


# 引数のパース
def arg_parser():
  args = sys.argv
  if len(args) == 1:  # 引数指定しなければ3人からrandomに選ばれる
    cfg_dict = ['../confs/rikka_template.cfg', '../confs/karin_template.cfg', '../confs/chifuyu_template.cfg']
    cfg = cfg_dict[random.randint(0, 2)]
    
  else:
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', help='Config file for voicepeak', default='../confs/rikka_template.cfg')
    cfg = parser.parse_args().cfg

  return cfg


def get_narrator(cfg_file):
  config_ini = configparser.ConfigParser()
  config_ini.read(cfg_file, encoding='utf-8')
  cfg_narrator = config_ini['indivisual']['NARRATOR']
  nar_dict = {'Koharu Rikka' : 'rikka', '夏色花梨' : 'karin', '花隈千冬' : 'chifuyu'}
  narrator = nar_dict[cfg_narrator]
  
  return narrator
  

# ボイス生成コマンドのテンプレート生成
def get_command_template(cfg_file):
  # Load configs
  config_ini = configparser.ConfigParser()
  config_ini.read(cfg_file, encoding='utf-8')
  vp_path = config_ini['common']['VOICEPEAK_PATH']
  speed = config_ini['common']['SPEED']
  pitch = config_ini['common']['PITCH']
  narrator = config_ini['indivisual']['NARRATOR']
  emot1 = config_ini['indivisual']['EMOT1']
  emot2 = config_ini['indivisual']['EMOT2']
  emot3 = config_ini['indivisual']['EMOT3']
  emot4 = config_ini['indivisual']['EMOT4']
  emot5 = config_ini['indivisual']['EMOT5']
  emotion = ','.join([emot1, emot2, emot3, emot4, emot5])
  os.makedirs('./wav', exist_ok=True)
  out_file = './wav/response.wav'
  
  # Command template
  template = [vp_path, '-s', '-n', narrator, '-o', out_file, '-e', emotion, '--speed', speed, '--pitch', pitch]
  
  return template

  
# VoicePeakでボイスのwavデータを生成
def generate_voice(query, template):  
  # Generate voice
  input = template[:2] + [query] + template[2:]
  '''
  print('Processing: ' + command + ' -s ' + query + ' -n ' + narrator + ' -o ' + out_file + ' -e ' + emotion
        + ' --speed ' + speed + ' --pitch ' pitch)
  '''
  subprocess.run(input, stderr=subprocess.DEVNULL)


# wavファイルを再生
def play_voice(input, format="wav"):
  # Play voice
  sound = AudioSegment.from_file(input, format=format)
  play(sound)
  
