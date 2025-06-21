# Simple chatbot with TOKYO6 chatacters

## Requirement

- python >=3.10.9
- zsh
- Python modules in requirements/requirements.txt

```sh
% python -m venv ~/tokyo6_bot && source ~/tokyo6_bot/bin/activate
% cd ./requirements/
% pip install -r requirements.txt
```


## How to run

### コンフィグファイルを指定せずに実行

```sh
% cd src
% python main.py  # 六花、花梨、千冬のうちいずれかのチャットボットがランダムで起動
Device set to use cpu

 六花がログインしました。

ユーザー: [文章を入力]  # 文章を入力するとbotが返答
...

ユーザー: おやすみ  # 終了する際は"おやすみ"や"バイバイ"、"またね"と入力
\033[38;5;213m六花\033[0m: またね〜！ *˙︶˙*)ﾉ

```


### テンプレートのコンフィグファイルを指定して実行

```sh
% cd src
% python main.py --cfg ../confs/karin_template.cfg  # [rikka/karin/chifuyu]_template.cfgのうちいずれかを指定
Device set to use cpu

 花梨がログインしました。

ユーザー: [文章を入力]  # 文章を入力するとbotが返答
...

ユーザー: おやすみ  # 終了する際は"おやすみ"や"バイバイ"、"またね"と入力
花梨: またね！ *˙︶˙*)ﾉ

```


### 任意のコンフィグファイルを指定して実行

```sh
% cd src
% python main.py --cfg ../confs/[your_config_file]  # テンプレートを編集して自由にカスタマイズ
Device set to use cpu

 千冬がログインしました。

ユーザー: [文章を入力]  # 文章を入力するとbotが返答
...

ユーザー: おやすみ  # 終了する際は"おやすみ"や"バイバイ"、"またね"と入力
千冬: また来てくださいね！ *˙︶˙*)ﾉ

```


## Specification

1. 「おはよう」と挨拶すると挨拶し返してくれます。
2. ポジティブな文章を入れるとイイネしてくれます。
3. ネガティブな文章を入れると話を聞いてくれます。
4. 好きな食べ物 (六花ならヨーグルト)、嫌いな食べ物 (六花ならブロッコリー)に触れると強く反応してくれます。
5. 「おやすみ」や「またね」というとバイバイしてチャットボットを閉じてくれます。


