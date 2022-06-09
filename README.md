# exifedit
写真の撮影日を書き換えるために作ったちょっとしたスクリプト
photoフォルダ内の写真すべてについて処理を実行する
参考 https://otameshitech.com/tech/python/pyexiv2-modify

## Quick Start
### Requirement
```
pip3 install pyexiv2
```
### Usage
- 撮影日時を書き替えたい写真をすべて「photo」フォルダに移動する（どのフォルダ内の写真に対して処理を行うかはmain.py内で指定できる）
- コマンドラインで `python3 main.py`
- 撮影日を入力するよう促されるので、コマンドラインで指示に従って入力する
- すべての写真について繰り返される
