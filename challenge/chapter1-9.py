# challenge:1 コンピュータにあるファイルを開いて、コンテンツを出力する
file_list = []
with open("file.txt", "r", encoding="utf-8") as f:
    file_list.append(f.read())
    for fi in file_list:
        print(fi)

# challenge:2 なんか質問するプログラムを書こう。入力された回答をファイルに書き出そう
ask = input("好きな食べ物は？")
with open("ask.txt", "w", encoding="utf-8") as f:
    f.write(ask)

# challenge:3 リストのリストに含まれている要素をCSVに書き出す
import csv
list1 = [["Top Gun", "Risly Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movie.csv", "w", newline='') as f:
    writer = csv.writer(f)
    for movie in list1:
        writer.writerow(movie)

# challenge:4 リストのリストに含まれている要素をCSVに書き出す(日本語でやってみる)
list1 = [["トップガン", "リズリービジネス", "マイノリティレポート"], ["タイタニック", "リベナント", "インセプション"], ["トレーニングデイ", "マンオブファイア", "フライト"]]
with open("movie2.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    for movie in list1:
        writer.writerow(movie)