##########################################
# Project: Let chatbot say hello world!
# Author: jolon
##########################################

from janome.tokenizer import Tokenizer

# Janomeのインスタンスを作成
tokenizer = Tokenizer()

# ユーザー入力の処理
def get_response(user_input):
    greetings=["こんにちは", "おはよう", "こんばんは"]
    
    #メッセージをトークンに分割
    tokens = tokenizer.tokenize(user_input)
    
    # トークンごとにルールをチェック
    for token in tokens:
      if token.surface in greetings: # 定義した挨拶用語が含まれる場合は同じ言葉を返すルール
        return token.surface
      elif token.part_of_speech.split(",")[1] == "固有名詞":# 固有名詞が含まれる場合はその固有名詞を質問するルール
        return f"{token.surface}はどういう意味ですか？" 
                
    return "わかりませんでした。もう一度お願いします。"


# メインの対話ループ
while True:
    user_input = input("ユーザー: ")
    if user_input.lower() == "終了":
        print("チャットを終了します。")
        break

    response = get_response(user_input)
    print(f"ボット: {response}")


