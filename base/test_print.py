print("单纯打印一行字符")
name = "test"
print(f"通过f格式化打印, 变量name={name}")

print("以下通过end打印不换行")
list = []
list.append("test")
list.append("apple")
list.append("banana")
for item in list:
    print(item, end='')
print()
print("以下输出间隔符")
x, y, z = 1, 2, 3
print(x, y, z, sep=",")

print("以下打印内容不转义")
print(r"\n \r \t")
