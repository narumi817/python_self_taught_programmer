import math
import random
import statistics
import keyword

print(math.pow(2, 3))
print(random.randint(0, 100))

# 整数リストから平均値、中央値、最頻値を求める
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(nums))
print(statistics.median(nums))
print(statistics.mode(nums))

# Pythonのキーワードかどうかチェック
print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))

# challenge 1
print(statistics.median_low(nums))