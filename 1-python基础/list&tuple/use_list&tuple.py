# list可变，tuple不可变
# 定义一个空的list = []
# 定义一个空的tuple = ()
# 定义只有一个元素的tuple：
# tuple = (1,)

# 1. 创建列表
# 定义一个空列表
my_list = []

# 定义一个包含多种类型元素的列表
my_list = [1, "apple", True, 3.14, [5, 6, 7], {"name": "John", "age": 30}]

# 2. 添加元素
# 2.1 append(),在列表末尾添加单个元素
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # 输出: [1, 2, 3, 4]

# 2.2 extend()：合并另一个可迭代对象（如列表）到当前列表
my_list = [1, 2]
my_list.extend([3, 4])
print(my_list)  # 输出: [1, 2, 3, 4]

# 2.3 insert(index, value)：在指定位置插入元素
my_list = [1, 2, 4]
my_list.insert(2, 3)  # 在索引2的位置插入3
print(my_list)  # 输出: [1, 2, 3, 4]

# 3. 删除元素
# 3.1 remove(value)：删除第一个匹配的值
my_list = [1, 2, 3, 2]
my_list.remove(2)  # 删除第一个值为2的元素
print(my_list)  # 输出: [1, 3, 2]

# 3.2 pop([index])：删除并返回指定索引的元素（默认最后一个）
my_list = [1, 2, 3, 4]
removed = my_list.pop(2)  # 删除索引2的元素
print(removed)  # 输出: 3
print(my_list)  # 输出: [1, 2, 4]

# 3.3 del 语句：按索引或切片删除元素
my_list = [1, 2, 3, 4, 5]
del my_list[1]       # 删除索引1的元素
del my_list[1:3]     # 删除索引1到2的元素
print(my_list)  # 输出: [1, 5]

# 3.4 clear()：清空整个列表
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # 输出: []

# 4. 修改元素
# 4.1 直接通过索引修改元素
my_list = [10, 20, 30, 40]
my_list[2] = 99  # 修改索引2的元素
print(my_list)  # 输出: [10, 20, 99, 40]

# 4.2 列表推导式批量修改
my_list = [1, 2, 3, 4]
my_list = [x * 2 for x in my_list]
print(my_list)  # 输出: [2, 4, 6, 8]

# 5. 列表排序
# 5.1 sort()：原地排序（默认升序）
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # 输出: [1, 2, 3]

# 5.2 降序排序
my_list = [3, 1, 2]
my_list.sort(reverse=True)
print(my_list)  # 输出: [3, 2, 1]

# 5.3 sorted()：返回新排序列表（不修改原列表）
my_list = [3, 1, 2]
sorted_list = sorted(my_list)
print(sorted_list)  # 输出: [1, 2, 3]
print(my_list)      # 原列表不变: [3, 1, 2]

# 6. 列表反转
# 6.1 reverse()：原地反转列表
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # 输出: [3, 2, 1]

# 6.2 切片反转
my_list = [1, 2, 3]
reversed_list = my_list[::-1]
print(reversed_list)  # 输出: [3, 2, 1]

# 7. 列表切片
# 7.1 基本切片
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # 输出: [20, 30, 40]
print(my_list[:3])   # 输出: [10, 20, 30]
print(my_list[2:])   # 输出: [30, 40, 50]

# 7.2 使用负数索引切片
my_list = [10, 20, 30, 40, 50]
print(my_list[-3:])  # 输出: [30, 40, 50]
print(my_list[-3:-1])  # 输出: [30, 40]

# 7.3 步长切片
my_list = [1, 2, 3, 4, 5]
print(my_list[::2])  # 输出: [1, 3, 5]
print(my_list[1::2])  # 输出: [2, 4]

# 8. 列表统计与查询
# 8.1 len()：获取列表长度
my_list = [1, 2, 3]
print(len(my_list))  # 输出: 3

# 8.2 in：检查元素是否存在
my_list = [1, 2, 3]
print(2 in my_list)  # 输出: True
print(4 in my_list)  # 输出: False

# 8.3 index(value)：查找元素的索引
my_list = [1, 2, 3, 2]
print(my_list.index(2))  # 输出: 1（第一个匹配的索引）

# 8.4 count(value)：统计元素出现的次数
my_list = [1, 2, 2, 3]
print(my_list.count(2))  # 输出: 2

# 8.5 max() / min() / sum()：计算最大值、最小值、总和
my_list = [4, 2, 9, 1, 5, 6]
print(max(my_list))  # 输出: 9
print(min(my_list))  # 输出: 1
print(sum(my_list))  # 输出: 27

# 9. 高级操作
# 9.1 列表推导式
# 基础用法
my_list = [x * 2 for x in range(5)]
print(my_list)  # 输出: [0, 2, 4, 6, 8]

# 带条件判断
my_list = [x * x for x in range(1, 11) if x % 2 == 0]
print(my_list)  # 输出: [4, 16, 36, 64, 100]

# 嵌套列表推导式（展平二维列表）
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [element for row in matrix for element in row]
print(flat_list)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 9.2 复制列表
# 浅拷贝
my_list = [1, 2, 3]
copy_list = my_list.copy()  # 或 my_list[:]
print(copy_list)  # 输出: [1, 2, 3]

# 10. 常见错误与注意事项
# remove() 删除不存在的元素会抛出 ValueError
my_list = [1, 2, 3]
my_list.remove(4)  # 抛出 ValueError

# 切片操作的“左闭右开”特性
my_list = [1, 2, 3, 4]
print(my_list[1:3])  # 输出: [2, 3]（不包含索引3的元素）