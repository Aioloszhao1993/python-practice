# 1. 条件判断的基本结构
# Python 使用 if、elif、else 实现条件判断，根据不同的条件执行不同的代码块

# 1.1 单分支结构：if
# 基本语法
# if 条件:
#     # 条件为 True 时执行的代码块
age = 20
if age >= 18:
    print("你已成年")

# 1.2 双分支结构：if-else
# 基本语法
# if 条件:
#     # 条件为 True 时执行的代码块
# else:
#     # 条件为 False 时执行的代码块
age = 16
if age >= 18:
    print("可以投票")
else:
    print("未成年，不能投票")

# 1.3 多分支结构：if-elif-else
# 基本语法
# if 条件1:
#     # 条件1为 True 时执行
# elif 条件2:
#     # 条件1为 False，条件2为 True 时执行
# elif 条件3:
#     # 条件1和条件2为 False，条件3为 True 时执行
# else:
#     # 所有条件均为 False 时执行
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 2. 嵌套条件判断
# 在条件判断内部再嵌套另一个条件判断，用于处理更复杂的逻辑
age = 20
has_license = True
if age >= 18:
    if has_license:
        print("你可以开车")
    else:
        print("你没有驾驶证")
else:
    print("你未满18岁")

# 3. 布尔表达式与逻辑运算符
# 3.1 比较运算符
a = 10
b = 20
print(a < b)  # True
print(a == b) # False

# 3.2 逻辑运算符
# and	所有条件均满足时为 True
# or	任一条件满足时为 True
# not	对条件取反
age = 25
print(age > 18 and age < 60) # True（同时满足两个条件）
print(age < 18 or age > 60)  # False（不满足任意条件）
print(not (age > 18))        # False（取反后结果为 False）

# 4. 条件判断的高级用法
# 4.1 成员运算符
# 用于检查值是否存在于序列（如列表、字符串）中
# in：存在时返回 True
# not in：不存在时返回 True
vowels = 'aeiou'
letter = 'e'
if letter in vowels:
    print("是元音字母")

# 4.2 身份运算符
# 用于判断两个变量是否指向同一对象：
# is：是同一对象时返回 True
# is not：不是同一对象时返回 True
a = [1, 2, 3]
b = a
print(a is b)  # True（a 和 b 指向同一对象）

# 5.布尔值的隐式转换：
# Python 中以下值会被视为 False：0、空字符串 ""、空列表 []、空字典 {}、None
if []:  # 空列表视为 False
    print("不会执行")