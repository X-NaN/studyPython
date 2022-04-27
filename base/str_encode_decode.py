# -*- encoding: utf-8 -*-
"""
@File    : str_encode_decode.py
@Time    : 2022/4/27 3:10 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 
"""

txt = '你好'
# str->bytes encode
txt = txt.encode('utf-8')
print(type(txt))
# bytes->str decode
txt = txt.decode('utf-8')
print(type(txt))

if __name__ == '__main__':
    pass
