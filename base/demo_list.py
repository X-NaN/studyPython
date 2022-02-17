"""
可以直接运行本文件
从上到下逐行解释执行
"""
list = []
list.append("test")
list.append("apple")
list.append("banana")
for item in list:
    print(item)


def fact(n):
    """
    阶乘方法
    :param n:
    :return:
    """
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


print("demo_list.py文件, __name__:%s" % __name__)
# print格式化，推荐使用如下
print(f"demo_list.py文件,阶乘: {fact(3)}")
