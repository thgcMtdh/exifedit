# 写真のEXIF情報を書き換えるスクリプト
# photoフォルダ内の写真すべてについて処理を実行する
# 参考 https://otameshitech.com/tech/python/pyexiv2-modify

import os
import pyexiv2

dirname = "photo"

# photoフォルダ内のファイルを取得
files = os.listdir(dirname)

for filename in files:
    # img 取得
    img = pyexiv2.Image(dirname + "/" + filename)

    # メタデータ read
    metadata = img.read_exif()

    # 撮影日時を書き換え
    print(f"File {filename}:")
    newdate = input(" Input date in YYYY:MM:DD HH:MM:SS format: ")  # ユーザが入力
    metadata["Exif.Photo.DateTimeOriginal"] = newdate

    # メタデータ を img に書き戻し
    img.modify_exif(metadata)

    # ファイルクローズ
    img.close()
