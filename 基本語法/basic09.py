# Python 基本資料結構
# list   列表[]    (元素內容可以重複, 元素內容可以修改)
# tuple  列表()    (唯讀, Fast)
# set    列表{}    (元素內容不可重複, 元素內容可以修改)
# dict   字典列表{} (元素內容可以重複, 元素內容可以修改)

# list 列表
scores1 = [100, 90]
scores2 = [80, 70]
scores1[1] = 95
scores1.append(70)
scores3 = scores1 + scores2
print(scores3)

# tuple 列表
scores1 = (100, 90)
# scores1[1] = 95  # 不可修改
# scores1.append(70)  # 不可增加
print(scores1)

# list 與 tuple 互轉
scores = (100, 90)
scores = list(scores)
print(type(scores), scores)
scores = tuple(scores)
print(type(scores), scores)

# set 列表
empIds = [1, 3, 5, 2, 3, 1]
empIds = set(empIds)
print(type(empIds), empIds)
print(len(empIds))
