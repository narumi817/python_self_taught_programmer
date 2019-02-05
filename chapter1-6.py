# 第6章 Challenge
# 1. 文字列「カミュ」に含まれている全ての文字列を1文字ずつ出力しよう
str = "カミュ"
print(str[0])
print(str[1])
print(str[2])

# 2. 2つの文字列を入力させるプログラムを書こう。
#    文字列を埋め込んで出力しよう
input1 = input("名前を入力してね：")
input2 = input("年齢を入力してね：")
push_string = "{}は{}歳です".format(input1, input2)
print(push_string)

# 3. 文法的には正しい文章を書いた文字列の先頭をメソッドを使って大文字にしよう
eng_str = "aldous Huxley was born in 1894."
print(eng_str.capitalize())

# 4. 文字列をメソッドで分割して、リストにしよう
jap_str = "どこで? だれが? いつ?"
jap_list = jap_str.split(" ")
print(jap_list)

# 5. リストの文字列を連結させる
eng_list = ["The", "fox", "jumped", "over", "the", "fence", "."]
join_string = " ".join(eng_list).replace(" .", ".")
print(join_string)

# 6. 文字列のsをドル記号に置き換える
eng_str2 = "A screaming comes across the sky"
print(eng_str2.replace("s", "$"))

# 7. 文字列の中で最初に「m」が出現するインデックスを調べる
print("Hemingway".index("m"))

# 8. クォーと文字列
print("can\'t get enough")

# 9. 文字列を「＋」で結合.「*」で同じ文字列
str2 = " three"
print(str2 + str2 + str2)
print(str2 * 3)

# 10. スライス
jap_str2 = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(jap_str2[:jap_str2.index("、")])