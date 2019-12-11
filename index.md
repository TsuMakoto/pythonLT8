---

title: 業務でboto3を導入し、Text2Speechを半自動化した話
theme: uncover
class: invert
image: https://marp.app/og-image.jpg
size: 16:9


# 業務でboto3を導入し、Text2Speechを半自動化した話

## 自己紹介
- 塚本真人
- 株式会社Fusic
- 大学院卒1年目
- 普段はRubyやJuliaを書いてます(あれ？)
- 趣味: ポケモン

![bg right:50% height:80%](img/49139020)

# なにがあったのか？
* 上司) AWSのAmazon Polly使って、音声案内作っといて〜
* ぼく) 了解でーす
* ....................................................
* やることを調べた
* テキスト入力
* ダウンロードボタンポチ
* ふう。一個完成

## おもんな！！
やりたくない！！
![bg right:50% height:80%](img/yaruki_nai_suit_man.png)

## 自動化できるらしい！
やる！！
![bg right:50% height:80%](img/yaruki_aru_suit_man.png)

# 業務を半自動化した話

# 業務を半自動化(効率化)した

## boto3で利用

```py

import boto3


session = boto3.session.Session(profile_name='{profine_name}')
polly = session.client('polly')
response = polly.synthesize_speech(
  Engine='standard',
  LanguageCode='ja-JP',
  TextType='text', # or ssml
  VoiceId='Mizuki',
  Text='こんにちは、ミズキです。読みたいテキストをここに入力してください。',
  OutputFormat='mp3'
)
```

## boto3で利用

```json
{
  "ResponseMetadata": {
    "RequestId": "0460c587-f386-4558-8f97-8ece81f05a48",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
    	"x-amzn-requestid": "0460c587-f386-4558-8f97-8ece81f05a48",
    	"x-amzn-requestcharacters": "33",
    	"content-type": "audio/mpeg",
   	  "transfer-encoding": "chunked",
      "date": "Sat, 23 Nov 2019 15:41:18 GMT"
    },
    "RetryAttempts": "0"
  },
  "ContentType": "audio/mpeg",
  "RequestCharacters": "33",
  "AudioStream": "<botocore.response.StreamingBody object at 0x7f4943354fa0>"
}
```

## レキシコン

発音を辞書として、保存することができます。

```
<?xml version="1.0" encoding="UTF-8"?>
<lexicon version="1.0"
 xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon
 http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd"
 alphabet="ipa"
 xml:lang="ja-JP">
  <lexeme>
    <grapheme>こんにちは</grapheme>
    <alias>tyaasu</alias>
  </lexeme>
</lexicon>

```

# ということで

# LT発表内容

## デモってみた

```
Pythonに関係することであればOKです！
LTをしたことない方でも大歓迎です！
練習に使っても大丈夫です。
ぜひ挑戦してみてください！
登壇していただける方は管理人にツイッターでDM
もしくは、ページ最後の問い合わせ先メールにて、発表タイトルをご連絡ください。

＊予告なしでテーマや発表者が変わる可能性があります。

発表時間：一人当たり5~10分程度でお願いいたします。（多少前後しても問題ありません）

```

## デモ

## Fusic 機械学習記事
https://fusic.co.jp/ml/5

![width:600px](img/polly.png)


# ありがとうございました！！！
