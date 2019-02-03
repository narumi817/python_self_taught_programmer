# 第4章 Challenge
# 1. 数字を入力値として受け取り、その数字を2乗した戻り値を返す関数を書いてみよう。
def power(x) :
    """
    Returns x ** 2.
    : param x : int.
    : return : int x power 2.
    """
    return x ** 2

# 2. 文字列を引数とし、その文字列を出力する関数を書いてみよう。
def print_str(x) :
    """
    Print string x.
    : input x : string 
    """
    print(x)

# 3. 3つの必須引数と2つのオプション引数がある関数を書いてみよう。
def calc(x, y, z, a = 2, b = 5) :
    """
    Print calc x + y + z and a ** b.
    : input x : int
    : input y : int
    : input z : int
    : input a : int
    : input b : int
    """
    print(x + y + z)
    print(a ** b)

# 4. 2つの関数からなるプログラムを書いてみよう。
#    1つ目の関数は整数を引数として受け取り、その整数を2で割ってもとめられる整数を出力として返そう。
#    2つ目の関数は整数を引数として受け取り、4でかけた整数を返そう
#    プログラム内で、1つ目の関数を呼び、戻り値を変数として保存し、2つ目の関数の引数として渡そう。
def div(x) :
    """
    Return calc x //2
    : input x : int
    """
    return int(x) // 2

def times(x) :
    """
    Return calc x * 4
    : input x : int
    """
    return int(x) * 4

print(times(div(3)))

# 5. 文字列をfloat型に変換して戻り値とする関数を書いてみよう。
#    起こりうる例外をキャッチする例外処理を書こう。
def change_num_for_float(x) :
    """
    Return float(x)
    : input x : string
    """
    try :
        float_x = float(x)
        return float_x
    except ValueError :
        print("Invalid Input Value.")

print(change_num_for_float(10))
print(change_num_for_float(0))
print(change_num_for_float('aaa'))

