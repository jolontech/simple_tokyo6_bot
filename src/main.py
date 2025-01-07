##########################################
# Project: Let chatbot talk and encourage
# Author: jolon
##########################################

from func import *

from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from janome.tokenizer import Tokenizer

if __name__ == "__main__":
  # Janomeのインスタンスを作成
  tokenizer = Tokenizer()

  sentiment_analysis_model_name = "jarvisx17/japanese-sentiment-analysis"
  sentiment_analysis_model = load_sentiment_analysis_model(sentiment_analysis_model_name)

  byebye = load_response('response/byebye/judge_byebye.txt')
  # チャットボットの利用
  while True:
    user_input = input("ユーザー: ")
    if user_input.lower() in byebye:
      print("六花: またね〜！ *˙︶˙*)ﾉ\n")
      break

    response = comfort_bot(user_input, sentiment_analysis_model)
    print(f"六花: {response}\n")

