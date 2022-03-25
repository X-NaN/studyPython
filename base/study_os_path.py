import os
def path():
    print("当前文件路径："+os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    path()