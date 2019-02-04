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