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

# 応答ルール
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
      return random.choice(message_for_broccoli) + random.choice(kaomoji_for_broccoli)
    elif token.surface in "ヨーグルト":
      return random.choice(message_for_yogurt) + random.choice(kaomoji_for_yogurt)
  
  sentiment, score = detect_negative_sentiment(input_text, sent_analysis_model)
  if sentiment == "negative":
    return random.choice(message_for_negative) + random.choice(kaomoji_for_negative)
  elif sentiment == "positive":
    return random.choice(message_for_positive) + random.choice(kaomoji_for_positive)
  else:
    return "ん、なんて？"

