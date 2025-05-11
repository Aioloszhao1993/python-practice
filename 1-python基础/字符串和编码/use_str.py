# ASCII编码是1个字节
# Unicode编码通常是2个字节（偏僻的字符就要用到4个字节）
# UTF-8编码方式为可变长度，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节
# ASCII、Unicode和UTF-8的关系
# ASCII编码实际上可以被看成是UTF-8编码的一部分，在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码

# bytes：字符串如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
# encode(编码，str到bytes)
str = "中文"
res = str.encode('utf-8')
print(f"str:{str}的编码结果为:{res}")

# decode(解码，bytes到str)
b_res = res.decode('utf-8')
print(f"bytes:{res}的解码结果为:{b_res}")

# 格式化
# %s,%d,%f
str1 = "Aiolos"
int1 = 32
float1 = 80.1123
print("I'am %s, age %d, weight %.2f" % (str1, int1, float1))

