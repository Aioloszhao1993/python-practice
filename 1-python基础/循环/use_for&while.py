# 1. for 循环
# for 循环用于遍历序列（如列表、元组、字符串）或其他可迭代对象，逐个处理元素。
#
# 1.1 基本语法
# for 变量 in 可迭代对象:
#     # 循环体

# 1.2 示例：遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 1.3 遍历字符串
for char in "Python":
    print(char)

# 1.4 使用 range() 生成数字序列
for i in range(5):  # 0 到 4
    print(i)

# 1.5 遍历字典
# 遍历键
student_scores = {"Alice": 85, "Bob": 90, "Charlie": 78}
for name in student_scores:
    print(name)
# 遍历值
for score in student_scores.values():
    print(score)
# 同时遍历键和值
for name, score in student_scores.items():
    print(f"{name}: {score}")

# 2. while 循环
# 2.1 基本语法
# while 条件:
#     # 循环体
# 2.2 示例：计数器
count = 0
while count < 5:
    print(count)
    count += 1
# 2.3 无限循环与 break
while True:
    user_input = input("请输入 'q' 退出：")
    if user_input == 'q':
        break

# 3. 循环控制语句
# 3.1 break：提前终止循环
for i in range(10):
    if i == 5:
        break
    print(i)
# 3.2 continue：跳过当前迭代
for i in range(5):
    if i == 2:
        continue
    print(i)
# 3.3 else：循环正常结束时执行
for i in range(3):
    print(i)
else:
    print("循环结束")
# while 循环中的 else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("条件不满足，退出循环")

# 4. 嵌套循环
# 在循环内部嵌套另一个循环，用于处理多维数据或复杂逻辑。
#
# 4.1 示例：打印乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} * {i} = {i*j}", end="\t")
    print()

# 4.2 示例：矩阵遍历
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()

# 5. 高级用法
# 5.1 列表推导式
# 用一行代码生成列表，替代简单的 for 循环：
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 5.2 生成器表达式
# 节省内存，适用于大数据处理：
squares_gen = (x**2 for x in range(10))
for square in squares_gen:
    print(square)

# 5.3 enumerate()：获取索引和值
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")

# 5.4 zip()：同时遍历多个序列
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

