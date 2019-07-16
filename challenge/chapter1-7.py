# 1. 次のリストの要素をそれぞれ出力しよう
movie_list = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for movie in movie_list:
    print(movie)

# 2. 25から50までの数値をそれぞれ出力しよう
for i in range(25, 51):
    print(i)

# 3. チャレンジ１のリストの要素をそれぞれ、インデックス値と一緒に出力しよう
for (i, movie) in enumerate(movie_list):
    print(i, movie) 

# 4. 無限ループする数字当てプログラムを書こう
# ユーザに文字を入力してもらい、qが入力されたら終了、数字が入力されたら正解かどうか判定しよう
# 正解の数値はプログラム内にいくつかリストで持たせておいて、ユーザが入力した数字がそのどれかと一致したら「正解」、一致しなかったら「不正解」と表示しよう
# もし数字かq以外の文字が入力されたら、「数字を入力するか、qで終了します」と表示しよう
# while True:
#     num_list = ['444', '56', '78', '12']
#     input_val = input("数字を入力してね")
#     if input_val == 'q':
#         break

#     if input_val.isnumeric() == False and input_val != 'q': 
#         print("数字を入力するか、qで終了します")
#         continue

#     result = False
#     for num in num_list:
#         if num == input_val:
#             result = True
#             break
    
#     if result:
#         print("正解")
#     else:
#         print("不正解")

while True:
    num_list = [444, 12, 14, 55]
    input_val = input("数字を入力してね")

    if input_val == 'q':
        break

    try:
        input_val = int(input_val)
    except:
        print("数字を入力するか、qで終了します")
        continue
    
    if input_val in num_list:
        print("正解")
    else:
        print("不正解")

# 5. 2つのリストに含まれる全ての数字の組み合わせでかけ算しよう
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
mul_list = []
for i in list1:
    for j in list2:
        mul_list.append(i * j)
print(mul_list)