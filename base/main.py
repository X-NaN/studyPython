"""
__name__:模块（文件）名称
__main__python程序入口
"""
import demo_list

if __name__ == '__main__':
    print(f'main.py, 程序入口, 当前执行文件名: {__name__}')
    print(f"main.py, 阶乘: {demo_list.fact(3)}")
