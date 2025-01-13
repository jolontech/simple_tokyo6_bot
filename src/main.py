##########################################
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
  
  # Janomeのインスタンスを作成
  tokenizer = Tokenizer()
  
  # sentiment analysis modelのロード
  sentiment_analysis_model_name = "jarvisx17/japanese-sentiment-analysis"
  sentiment_analysis_model = load_sentiment_analysis_model(sentiment_analysis_model_name)
  
  # チャットボットの利用
  byebye = load_response('response/byebye/judge_byebye.txt')
  while True:
    user_input = input("ユーザー: ")
    
    # 終了メッセージ
    if user_input.lower() in byebye:
      # メッセージ生成
      response_text_kaomoji = say_byebye()
      response = response_text_kaomoji['text'] + response_text_kaomoji['kaomoji']
      
      # ボイス生成
      if with_voice:
        generate_voice(query=response_text_kaomoji['text'], out_file='wav/response.wav')

      # メッセージ&ボイス出力
      print(f"六花: {response}\n")
      if with_voice:
        play_voice(input='wav/response.wav')
        break
    
    # 応答メッセージ
    # メッセージ生成
    response_text_kaomoji = comfort_bot(user_input, sentiment_analysis_model)
    response = response_text_kaomoji['text'] + response_text_kaomoji['kaomoji']

     # ボイス生成
    if with_voice:
      generate_voice(query=response_text_kaomoji['text'], out_file='wav/response.wav')

    # メッセージ&ボイス出力
    print(f"六花: {response}\n")    
    if with_voice:
      play_voice(input='wav/response.wav')
      
