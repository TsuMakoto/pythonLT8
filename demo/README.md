# Amazon pollyでテキストデータを音声データへ変換するスクリプト

# 開発環境
pipインストール、もしくはdockerでの環境を用いる

## Using pip

```
$ pip install poetry
$ poetry shell
$ poetry install
```

## Using docker

```
$ docker build . -t mimpaku_polly
$ docker run -it --rm --mount type=bind,src=`pwd`,dst=/app mimpaku_polly bash
```

# Usage
$HOME/.awsへconfigを設定しておくこと
https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-chap-configure.html

```
$ poetry shell
$ python src/main.py
# or 複数のファイルを指定する
$ pythoon src/main.py /path/to/data1.xml /path/to/data2.xml ....
```

を実行後tmpディレクトリ配下に音声データが入っている。
