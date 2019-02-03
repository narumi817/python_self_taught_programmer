# 第5章 Challenge
# 1. 好きなミュージシャンのリストを作ろう
musician_list = ["RADWIMPS", "ONE OK ROCK", "KAT-TUN"]
print(musician_list)

# 2. タプルのリストを作ろう。各タプルには行ったことのある場所の緯度と経度を持たせよう
place_list = list()
tokyo = (20.2531, 136.4011)
aichi = (35.1049, 136.5424)
kyoto = (35.0117, 135.4520)
place_list.append(tokyo)
place_list.append(aichi)
place_list.append(kyoto)
print(place_list)

# 3. 辞書を作ろう。特徴を表すキーバリューのペアを持たせよう
my_feature = {
    "height" : 157,
    "age" : 28,
    "favorite_color" : "pink",
}
print(my_feature)

# 4. 任意のキーを入力させる。入力されたキーを使って、1つ前の辞書からバリューを取得して表示
input_key = input("キーを入力してください：")
if input_key in my_feature :
    print(my_feature[input_key])
else :
    print("キーが存在しません")

# 5. 好きなミュージシャンを辞書のキーに入れ、そのバリューに曲をリストで持たせよう
favorite_musician = {
    "KAT-TUN" : [
        "Real Face",
        "LIPS",
        "Keep the face",
    ],
    "Sexy Zone" : [
        "Rock tha town",
        "ぎゅっと",
        "すっぴんKISS",
    ],
    "KinKi Kids" : [
        "硝子の少年",
        "ジェットコースターロマンス",
        "Bonnie Butterfly",
    ],
}
print(favorite_musician)

# 6. setについて調べよう
# set : 要素の重複がないコンテナ。順序もなし。set(list)で生成。
tmp_list = ["apple", "banana", "orange", "apple"]
print(tmp_list)
set_list = set(tmp_list)
print(set_list)