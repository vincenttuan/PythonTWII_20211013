from functools import reduce

# 1. lambda parameter_list: expression
max = lambda a, b: a if a > b else b
print(max(10, 20))

# 2. (lambda parameter_list: expression)(argument)
print((lambda a: a*a)(5))

# 3. filter(lambda parameter: expression, iterable)
# iterable = 數組
nums = [50, 2, 10, 40]
print(type(nums), nums)
# 想要過濾出大於 20 的資料
result = filter(lambda x: x > 20, nums)
print(result, list(result)) # 轉 list

# 4. map(lambda parameter: expression, iterable)
# map 轉換
scores = [50, 80, 90, 30]  # [False, True, True, False]
result = map(lambda x: x >= 60, scores)
print(list(result))
result = map(lambda x: 1 if x >= 60 else 0, scores)
print(list(result))

# 4. reduce(lambda param1, param2: expression, iterable)
# reduce 歸納
scores = [50, 80, 90, 30]
result = reduce(lambda x, y: x + y, scores)
# [50, 80, 90, 30]
# x=50, y=80: 130
# x=130, y=90: 220
# x=220, y=30: 250
print(result)

# 5. sorted(iterable, key=lambda parameter: expression)
scores = [50, 80, 90, 30]
print(sorted(scores))
print(sorted(scores, reverse=True))
prices = [('2330.TW', 599), ('2317.TW', 108), ('3008.TW', 2080)]
print(sorted(prices, key=lambda p: p[1], reverse=True))
