##########################################
# Project: Methods for chatbot with TOKYO6 characters
# Author: jolon
# Description: methods called from main
##########################################

# Import moudules
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import random
import sys
from janome.tokenizer import Tokenizer

# Janomeのインスタンスを作成
tokenizer = Tokenizer()


# 事前学習済みモデルの読み込み
def load_sentiment_analysis_model(model_name):
  
  # モデルのロード
  model = AutoModelForSequenceClassification.from_pretrained(model_name)
  tokenizer = AutoTokenizer.from_pretrained(model_name)
  sentiment_analysis_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
  
  return sentiment_analysis_pipeline


# 感情分析
def detect_negative_sentiment(text, sentiment_analysis_pipeline):
  result = sentiment_analysis_pipeline(text)
  sentiment = result[0]["label"]
  score = result[0]["score"]
  
  return sentiment, score


# ファイル読み込み
def load_response(path):
  response = []
  with open(path) as f:
    for line in f:
       response.append(line.rstrip('\n'))
       
  return response


# 終了メッセージの生成
def say_byebye(narrator):
  # メッセージと顔文字の読み込み
  message_for_byebye = load_response('response/' + narrator + '/messages/for_byebye.txt')
  kaomoji_for_byebye = load_response('response/' + narrator + '/kaomoji/for_byebye.txt')

  # 応答メッセージ生成
  text = random.choice(message_for_byebye)
  kaomoji = random.choice(kaomoji_for_byebye)
  
  return {"text": text, "kaomoji": kaomoji}


# メッセージと顔文字の辞書作成
def get_message_dict(narrator="rikka"):
  if narrator == "rikka":
    message_for_hello = load_response('response/rikka/messages/for_hello.txt')
    kaomoji_for_hello = load_response('response/rikka/kaomoji/for_hello.txt')
    message_for_liked = load_response('response/rikka/messages/for_liked.txt')
    kaomoji_for_liked = load_response('response/rikka/kaomoji/for_liked.txt')
    message_for_disliked = load_response('response/rikka/messages/for_disliked.txt')
    kaomoji_for_disliked = load_response('response/rikka/kaomoji/for_disliked.txt')
    message_for_positive = load_response('response/rikka/messages/for_positive.txt')
    kaomoji_for_positive = load_response('response/rikka/kaomoji/for_positive.txt')
    message_for_negative = load_response('response/rikka/messages/for_negative.txt')
    kaomoji_for_negative = load_response('response/rikka/kaomoji/for_negative.txt')
    message_for_byebye = load_response('response/rikka/messages/for_byebye.txt')
    kaomoji_for_byebye = load_response('response/rikka/kaomoji/for_byebye.txt')
    message_dict = {'hello': message_for_hello, 'positive': message_for_positive,
                    'negative': message_for_negative, 'liked': message_for_liked,
                    'disliked': message_for_disliked, 'byebye': message_for_byebye}
    kaomoji_dict = {'hello': kaomoji_for_hello, 'positive': kaomoji_for_positive,
                    'negative': kaomoji_for_negative, 'liked': kaomoji_for_liked,
                    'disliked': kaomoji_for_disliked, 'byebye': message_for_byebye}

  elif narrator == "karin":
    message_for_hello = load_response('response/karin/messages/for_hello.txt')
    kaomoji_for_hello = load_response('response/karin/kaomoji/for_hello.txt')
    message_for_liked = load_response('response/karin/messages/for_liked.txt')
    kaomoji_for_liked = load_response('response/karin/kaomoji/for_liked.txt')
    message_for_disliked = load_response('response/karin/messages/for_disliked.txt')
    kaomoji_for_disliked = load_response('response/karin/kaomoji/for_disliked.txt')
    message_for_positive = load_response('response/karin/messages/for_positive.txt')
    kaomoji_for_positive = load_response('response/karin/kaomoji/for_positive.txt')
    message_for_negative = load_response('response/karin/messages/for_negative.txt')
    kaomoji_for_negative = load_response('response/karin/kaomoji/for_negative.txt')
    message_for_byebye = load_response('response/karin/messages/for_byebye.txt')
    kaomoji_for_byebye = load_response('response/karin/kaomoji/for_byebye.txt')
    message_dict = {'hello': message_for_hello, 'positive': message_for_positive,
                    'negative': message_for_negative, 'liked': message_for_liked,
                    'disliked': message_for_disliked, 'byebye': message_for_byebye}
    kaomoji_dict = {'hello': kaomoji_for_hello, 'positive': kaomoji_for_positive,
                    'negative': kaomoji_for_negative, 'liked': kaomoji_for_liked,
                    'disliked': kaomoji_for_disliked, 'byebye': message_for_byebye}

  elif narrator == "chifuyu":
    message_for_hello = load_response('response/chifuyu/messages/for_hello.txt')
    kaomoji_for_hello = load_response('response/chifuyu/kaomoji/for_hello.txt')
    message_for_liked = load_response('response/chifuyu/messages/for_liked.txt')
    kaomoji_for_liked = load_response('response/chifuyu/kaomoji/for_liked.txt')
    message_for_disliked = load_response('response/chifuyu/messages/for_disliked.txt')
    kaomoji_for_disliked = load_response('response/chifuyu/kaomoji/for_disliked.txt')
    message_for_positive = load_response('response/chifuyu/messages/for_positive.txt')
    kaomoji_for_positive = load_response('response/chifuyu/kaomoji/for_positive.txt')
    message_for_negative = load_response('response/chifuyu/messages/for_negative.txt')
    kaomoji_for_negative = load_response('response/chifuyu/kaomoji/for_negative.txt')
    message_for_byebye = load_response('response/chifuyu/messages/for_byebye.txt')
    kaomoji_for_byebye = load_response('response/chifuyu/kaomoji/for_byebye.txt')
    message_dict = {'hello': message_for_hello, 'positive': message_for_positive,
                    'negative': message_for_negative, 'liked': message_for_liked,
                    'disliked': message_for_disliked, 'byebye': message_for_byebye}
    kaomoji_dict = {'hello': kaomoji_for_hello, 'positive': kaomoji_for_positive,
                    'negative': kaomoji_for_negative, 'liked': kaomoji_for_liked,
                    'disliked': kaomoji_for_disliked, 'byebye': message_for_byebye}

  else:
    sys.exit("Error: Inproper args of narrator in get_message_dict function")
    
  return message_dict, kaomoji_dict
  

# 感情推定 & 応答の生成 六花
def comfort_bot_rikka(input_text, sent_analysis_model, message_dict, kaomoji_dict):
  tokens = tokenizer.tokenize(input_text)

  # 特殊メッセージに該当するならば専用の応答を返す
  for token in tokens:
    # hello
    if token.surface in "おはよう":
      text = random.choice(message_dict['hello'])
      kaomoji = random.choice(kaomoji_dict['hello'])
      return {"text": text, "kaomoji": kaomoji}

    # liked
    elif token.surface in "ヨーグルト":
      text = random.choice(message_dict['liked'])
      kaomoji = random.choice(kaomoji_dict['liked'])
      return {"text": text, "kaomoji": kaomoji}

    # disliked
    elif token.surface in "ブロッコリー":
      text = random.choice(message_dict['disliked'])
      kaomoji = random.choice(kaomoji_dict['disliked'])
      return {"text": text, "kaomoji": kaomoji}

  # それ以外なら感情推定に基づいて応答を返す
  sentiment, score = detect_negative_sentiment(input_text, sent_analysis_model)
  if sentiment == "negative":
    text = random.choice(message_dict['negative'])
    kaomoji = random.choice(kaomoji_dict['negative'])
    return {"text": text, "kaomoji": kaomoji}
  
  elif sentiment == "positive":
    text = random.choice(message_dict['positive'])
    kaomoji = random.choice(kaomoji_dict['positive'])
    return {"text": text, "kaomoji": kaomoji}
  
  else:
    return {"text": "ん、なんて？", "kaomoji": "(?_?)"}


# 感情推定 & 応答の生成 花梨
def comfort_bot_karin(input_text, sent_analysis_model, message_dict, kaomoji_dict):
  tokens = tokenizer.tokenize(input_text)
  
  # 特殊メッセージに該当するならば専用の応答を返す
  for token in tokens:
    # hello
    if token.surface in "おはよう":
      text = random.choice(message_dict['hello'])
      kaomoji = random.choice(kaomoji_dict['hello'])
      return {"text": text, "kaomoji": kaomoji}

    # liked
    elif token.surface in "フロマージュ" or token.surface in "ドゥーブル・フロマージュ":
      text = random.choice(message_dict['liked'])
      kaomoji = random.choice(kaomoji_dict['liked'])
      return {"text": text, "kaomoji": kaomoji}

    # disliked
    elif token.surface in "抹茶":
      text = random.choice(message_dict['disliked'])
      kaomoji = random.choice(kaomoji_dict['disliked'])
      return {"text": text, "kaomoji": kaomoji}

  # それ以外なら感情推定に基づいて応答を返す
  sentiment, score = detect_negative_sentiment(input_text, sent_analysis_model)
  if sentiment == "negative":
    text = random.choice(message_dict['negative'])
    kaomoji = random.choice(kaomoji_dict['negative'])
    return {"text": text, "kaomoji": kaomoji}
  
  elif sentiment == "positive":
    text = random.choice(message_dict['positive'])
    kaomoji = random.choice(kaomoji_dict['positive'])
    return {"text": text, "kaomoji": kaomoji}
  
  else:
    return {"text": "え、なんて？", "kaomoji": "(?_?)"}

  
# 感情推定 & 応答の生成 千冬
def comfort_bot_chifuyu(input_text, sent_analysis_model, message_dict, kaomoji_dict):
  tokens = tokenizer.tokenize(input_text)
  
  # 特殊メッセージに該当するならば専用の応答を返す
  for token in tokens:
    # hello
    if token.surface in "おはよう":
      text = random.choice(message_dict['hello'])
      kaomoji = random.choice(kaomoji_dict['hello'])
      return {"text": text, "kaomoji": kaomoji}

    # liked
    elif token.surface in "抹茶":
      text = random.choice(message_dict['liked'])
      kaomoji = random.choice(kaomoji_dict['liked'])
      return {"text": text, "kaomoji": kaomoji}
    
    # disliked
    elif token.surface in "スイーツ":
      text = random.choice(message_dict['disliked'])
      kaomoji = random.choice(kaomoji_dict['disliked'])
      return {"text": text, "kaomoji": kaomoji}
    
  # それ以外なら感情推定に基づいて応答を返す
  sentiment, score = detect_negative_sentiment(input_text, sent_analysis_model)
  if sentiment == "negative":
    text = random.choice(message_dict['negative'])
    kaomoji = random.choice(kaomoji_dict['negative'])
    return {"text": text, "kaomoji": kaomoji}
  
  elif sentiment == "positive":
    text = random.choice(message_dict['positive'])
    kaomoji = random.choice(kaomoji_dict['positive'])
    return {"text": text, "kaomoji": kaomoji}
  
  else:
    return {"text": "え、なんて言いました？", "kaomoji": "(?_?)"}

