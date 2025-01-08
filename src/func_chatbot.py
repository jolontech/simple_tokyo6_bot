##########################################
# Project: Methods for Rikka Bot
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


# ファイル読み込み
def load_response(path):
  response = []
  with open(path) as f:
    for line in f:
       response.append(line.rstrip('\n'))
  return response


# 終了メッセージの生成
def say_byebye():
  # メッセージと顔文字の読み込み
  message_for_byebye = load_response('response/messages/for_byebye.txt')
  kaomoji_for_byebye = load_response('response/kaomoji/for_byebye.txt')

  text = random.choice(message_for_byebye)
  kaomoji = random.choice(kaomoji_for_byebye)
  return {"text": text, "kaomoji": kaomoji}


# 感情推定&応答の生成
def comfort_bot(input_text, sent_analysis_model):
  tokens = tokenizer.tokenize(input_text)

  # メッセージと顔文字の読み込み
  message_for_broccoli = load_response('response/messages/for_broccoli.txt')
  kaomoji_for_broccoli = load_response('response/kaomoji/for_broccoli.txt')
  message_for_yogurt = load_response('response/messages/for_yogurt.txt')
  kaomoji_for_yogurt = load_response('response/kaomoji/for_yogurt.txt')
  message_for_positive = load_response('response/messages/for_positive.txt')
  kaomoji_for_positive = load_response('response/kaomoji/for_positive.txt')
  message_for_negative = load_response('response/messages/for_negative.txt')
  kaomoji_for_negative = load_response('response/kaomoji/for_negative.txt')
  
  # トークンごとにルールをチェック
  for token in tokens:
    if token.surface in "ブロッコリー":
      text = random.choice(message_for_broccoli)
      kaomoji = random.choice(kaomoji_for_broccoli)
      return {"text": text, "kaomoji": kaomoji}
    elif token.surface in "ヨーグルト":
      text = random.choice(message_for_yogurt)
      kaomoji = random.choice(kaomoji_for_yogurt)
      return {"text": text, "kaomoji": kaomoji}
  
  sentiment, score = detect_negative_sentiment(input_text, sent_analysis_model)
  if sentiment == "negative":
    text = random.choice(message_for_negative)
    kaomoji = random.choice(kaomoji_for_negative)
    return {"text": text, "kaomoji": kaomoji}
  elif sentiment == "positive":
    text = random.choice(message_for_positive)
    kaomoji = random.choice(kaomoji_for_positive)
    return {"text": text, "kaomoji": kaomoji}
  else:
    return {"text": "ん、なんて？", "kaomoji": "(?_?)"}

