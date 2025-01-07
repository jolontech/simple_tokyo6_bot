##########################################
# Project: Let chatbot say hello world!
# Author: jolon
##########################################

from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import random
from janome.tokenizer import Tokenizer

# Janomeのインスタンスを作成
tokenizer = Tokenizer()

# 事前学習済みモデルの読み込み
def load_sentiment_analysis_model(model_name):
  model = AutoModelForSequenceClassification.from_pretrained(model_name)
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  sentiment_analysis_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
  return sentiment_analysis_pipeline

# 感情分析
def detect_negative_sentiment(text, sentiment_analysis_pipeline):
  result = sentiment_analysis_pipeline(text)
  sentiment = result[0]["label"]
  score = result[0]["score"]
  return sentiment , score

# 応答ルール
def comfort_bot(input_text, sent_analysis_model):
  tokens = tokenizer.tokenize(input_text)
  
  # トークンごとにルールをチェック
  for token in tokens:
    if token.surface in "ブロッコリー": # 定義した挨拶用語が含まれる場合は同じ言葉を返すルール
      return "うわ、そんなもん持って来んなぁ！！！"
    elif token.surface in "ヨーグルト":
      return "え！ヨーグルトくれるの！？やった〜"
  
  sentiment, score = detect_negative_sentiment(input_text, sent_analysis_model)
  if sentiment == "negative":
    return random.choice(encouragement_messages1)
  elif sentiment == "positive":
    return random.choice(encouragement_messages2)
  else:
    return "ん、なんて？"

sentiment_analysis_model_name = "jarvisx17/japanese-sentiment-analysis"
sentiment_analysis_model = load_sentiment_analysis_model(sentiment_analysis_model_name)

encouragement_messages1 = [
    "どしたん？話、聞こか？",
    "どしたん？話、聞くよ？",
    "どしたん？トド岩、行っとく？",
    "どしたん？ヨーグルト、食べとく？"
]

encouragement_messages2 = [
    "いいね！",
    "GJ! ^^b",
    "頑張ってるね〜",
    "さっすが〜！知らなかった〜！すごーい！センスいい！そうなんだ〜！"
]

# チャットボットの利用
while True:
    user_input = input("ユーザー: ")
    if user_input.lower() == "終了":
        print("またね〜！ *˙︶˙*)ﾉ\n")
        break

    response = comfort_bot(user_input, sentiment_analysis_model)
    print(f"六花: {response}\n")

