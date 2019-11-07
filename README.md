# NanacoGiftHelpers

nanacoギフト関連のスクリプト集です。

## 説明

NanacoGiftHelpersは、nanacoギフトの自動登録を行うスクリプトです。

## 使い方

### Windows

1. 「Clone or download」からスクリプトをダウンロード・解凍
1. 外部サイトからChromeDriverをダウンロード
1. ギフトIDをクリップボードにコピー（改行区切りで複数入力可能）
1. start.batを実行

### Linux

```bash
git clone https://github.com/finphie/NanacoGiftHelpers.git

wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver NanacoGiftHelpers

cd NanacoGiftHelpers
python3 nanaco.py -d ${ChromeDriverのパス} ${card または mobile} ${nanaco番号} ${パスワード} ${ギフトID} ${ギフトID}...
```

## 使用言語

- Windows PowerShell 5.1(Desktop)
- Python 3.8

## 開発環境

- Visual Studio Code

## 作者

finphie

## ライセンス

CC0 1.0

## クレジット

このプロジェクトでは、下記のライブラリを使用しています。

### ライブラリ

- Selenium