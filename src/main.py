#########################################
# Project: Let Rikka Bot talk and encourage
# Author: jolon
# Usage: python main.py
##########################################

from func_chatbot import *
from func_autovp import *
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from janome.tokenizer import Tokenizer

if __name__ == "__main__":
  with_voice = True
  
  # ナレーターをコンフィグファイルから取得
  cfg_file = arg_parser()
  narrator = get_narrator(cfg_file)
  
  # voicepeakコマンドのテンプレートを生成
  template = get_command_template(cfg_file)
  
  # sentiment analysis modelのロード
  sentiment_analysis_model_name = "jarvisx17/japanese-sentiment-analysis"
  sentiment_analysis_model = load_sentiment_analysis_model(sentiment_analysis_model_name)
  
  # 終了条件のロード
  byebye = load_response('response/byebye/judge_byebye.txt')
  
  # ナレーターの選択
  if narrator == 'rikka':
    message_dict, kaomoji_dict = get_message_dict(narrator="rikka")
    comfort_bot = comfort_bot_rikka
    narrator_name = "六花"
    text_color = ["\033[38;5;213m", "\033[0m"]
    
  elif narrator == 'karin':
    message_dict, kaomoji_dict = get_message_dict(narrator="karin")
    comfort_bot = comfort_bot_karin
    narrator_name = "花梨"
    text_color = ["\033[38;5;128m", "\033[0m"]
    
  elif narrator == 'chifuyu':
    message_dict, kaomoji_dict = get_message_dict(narrator="chifuyu")
    comfort_bot = comfort_bot_chifuyu
    narrator_name = "千冬"
    text_color = ["\033[38;5;28m", "\033[0m"]
    
  else:
    print("不明なナレーターのため、'Koharu Rikka'に変更されました。")
    message_dict, kaomoji_dict = get_message_dict(narrator="rikka")
    comfort_bot = comfort_bot_rikka
    narrator_name = "六花"
    text_color = ["\033[38;5;213m", "\033[0m"]

  print("\n " + text_color[0] + narrator_name + text_color[1] + "がログインしました。\n")
  
  # チャットボットの実行
  while True:
    user_input = input("ユーザー: ")
    
    # 終了メッセージ
    if user_input.lower() in byebye:
      # メッセージ生成
      response_text_kaomoji = say_byebye(narrator)
      response = response_text_kaomoji['text'] + response_text_kaomoji['kaomoji']
      
      # ボイス生成
      if with_voice:
        generate_voice(query=response_text_kaomoji['text'], template=template)
        
      # メッセージ&ボイス出力
      print(f"{text_color[0]}{narrator_name}: {response}{text_color[1]}\n")
      if with_voice:
        play_voice(input='wav/response.wav')
        break
      
    # 応答メッセージ生成
    response_text_kaomoji = comfort_bot(user_input, sentiment_analysis_model, message_dict, kaomoji_dict)
    response = response_text_kaomoji['text'] + response_text_kaomoji['kaomoji']
    
    # ボイス生成
    if with_voice:
      generate_voice(query=response_text_kaomoji['text'], template=template)
      
    # メッセージ&ボイス出力
    print(f"{text_color[0]}{narrator_name}: {response}{text_color[1]}\n")
    if with_voice:
      play_voice(input='wav/response.wav')
      
