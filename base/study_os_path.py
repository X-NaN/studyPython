import os


def path():
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.basename(current_path)
    print("当前文件路径：" + current_path)
    (filename, extension) = os.path.splitext(file_name)
    print(filename + "," + extension)


if __name__ == '__main__':
    path()
