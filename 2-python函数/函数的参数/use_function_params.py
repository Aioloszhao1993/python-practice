# 函数的参数：
# 位置参数
def power(x):
    return x * x

x = 10
res = power(x)
print(f"位置参数:{res}")


# 默认参数
def print_name(name="Aiolos"):
    print(f"默认参数:你的名字是:{name}")

print_name()


# 可变参数
from functools import reduce
def list_sum(*args):
    return reduce(lambda x, y: x + y, args)

list1 = [1, 2, 3, 4, 5]
res = list_sum(*list1)
print(f"可变参数:{res}")
# 可变参数
def use_sorted(*args):
    res = sorted(args, key=lambda x:x["age"])
    return res

list1 = [
    {
        "name": "Aiolos",
        "age": 32
    },
    {
        "name": "Caroline",
        "age": 31
    },
    {
        "name": "Barry",
        "age": 23
    }
]
res = use_sorted(*list1)
print(f"可变参数:{res}")


# 关键字参数
def calc_value(**kwargs):
    value_list = [item for item in kwargs.values()]
    return value_list

dict1 = {"name": "Aiolos", "age": 32, "city": "xi'an"}
res = calc_value(**dict1)
print(f"可变参数:{res}")


# 命名关键字参数
def person1(name, age, *, city, job):
    print(f"命名关键字参数:name:{name}, age:{age}, city:{city}, job:{job}")

# 正确的示例
# 命名关键字参数必须传入参数名，且不能传入未定义的参数
person1("Aiolos", 32, city="xi'an", job="engineer")

# 错误的示例1
person1("Aiolos", 32, "xi'an", "engineer")

# 错误的示例2
person1("Aiolos", 32, hobby="soccer")
