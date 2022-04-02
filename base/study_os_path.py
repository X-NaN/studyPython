import os


def path():
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.basename(current_path)
    print("当前文件路径：" + current_path)
    (filename, extension) = os.path.splitext(file_name)
    print(filename + "," + extension)

    root_path = current_path[:current_path.index("studyPython")+len("studyPython")]
    print(root_path)


if __name__ == '__main__':
    path()
