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
