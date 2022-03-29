# -*- encoding: utf-8 -*-
"""
@File    : aesutil2.py
@Time    : 2022/3/29 3:53 下午
@Author  : xingnana
@Email   : 
@Software: PyCharm
@Description: 
"""
import binascii
import os
import struct

from Crypto.Cipher import AES


class AESCipherOld:

    def __init__(self, seckey):
        self.key = seckey  # 密钥
        self.iv = str.encode(seckey[0:16])  # 偏移量

    def __generate_iv(self):
        iv = b'884228eb5e53a57bd0511adb60fffa8d'
        return iv

    def __pad(self, text):
        """填充方式，加密内容必须为16字节的倍数，若不足则使用self.iv进行填充"""
        text_length = len(text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return text + pad * amount_to_pad

    def __unpad(self, text):
        pad = ord(text[-1])
        return text[:-pad]

    def aes_encrypt(self, plain_data):
        """
        aes  cbc 128
        CBC加密需要一个十六位的key(密钥)和一个十六位iv(偏移量)
        加密函数，如果data不是16的倍数【加密文本data必须为16的倍数！】，那就补足为16的倍数
        :param plain_data:明文数据 16位
        :param key:  16位
        :param iv:16位
        """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)  # 设置AES加密模式 此处设置为CBC模式

        # 填充数据
        pad_data = self.__pad(text=plain_data)

        encrypted_data = cipher.encrypt(pad_data)  # aes加密
        # encrypted= base64.b64encode(cipher.encrypt(pad_data))
        # 返回的二进制数据的十六进制表示。每一个字节的数据转换成相应的2位十六进制表示。
        result = binascii.b2a_hex(encrypted_data)  # b2a_hex encode  将二进制转换成16进制
        return encrypted_data

    def aes_decryppt(self, enc_data):
        """aes解密
        :param key:
        :param data:
        """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        dec_data = cipher.decrypt(enc_data)

        unpad_data = self.__unpad(dec_data)
        # 字符串转16进制
        result = binascii.hexlify(unpad_data)
        return unpad_data

    def enc_file(self, plain_file_path, enc_file_path):
        """
        加密文件
        :param plain_file_path: 明文文件路径
        :param enc_file_path: 加密后文件路径
        :param key: 秘钥
        :return:
        """

        with open(plain_file_path, 'rb') as fileobj:
            content = fileobj.read()
            # 加密文件
            enc_content = self.aes_encrypt(plain_data=content)
        file_name = os.path.basename(plain_file_path)
        # out_file_path = os.path.dirname(plain_file_path) + '/enc_obama.jpg'

        with open(enc_file_path, 'wb') as f:  # 以二进制写类型打开
            f.write(enc_content)  # 写入文件

    def dec_file(self, enc_file_path, dec_file_path):
        """
        解密文件
        :param enc_file_path: 加密文件路径
        :param dec_file_path: 解密文件路径
        :param key: 秘钥
        :return:
        """
        with open(enc_file_path, 'rb') as fileobj:
            content = fileobj.read()
            # 解密文件
            dec_content = self.aes_decryppt(enc_data=content)
        file_name = os.path.basename(enc_file_path)

        # (filename, extension) = os.path.splitext(file_name)
        # dec_file_path = os.path.dirname(enc_file_path) + '/dec_obama.jpg'
        with open(dec_file_path, 'wb') as f:  # 以二进制写类型打开
            f.write(dec_content)  # 写入文件

    def append_struct_info_to_encFile(self, key, plain_file_size, enc_file_path):
        """
        在加密文件头部加上解密信息
        头信息如下：
        UINT_T version;    无符号32位整形 4字节
        BYTE_T iv[AES_ENCRYPT_KEY_LEN];   BYTE_T是无符号8位CHAR型
        UINT_T size;         size是图片加密前的大小
        char reserve[40];  reserve是为后续备用的，可以不用填
        :param key:
        :param enc_file_path:本地加密文件 enc_obama.jpg
        :return:
        """
        key = key.encode('raw_unicode_escape')
        iv = key
        version = 1
        reserve = ' ' * 40

        with open(enc_file_path, "rb+") as fileobj:
            content = fileobj.read()
            fileobj.seek(0)
            # 小端，unsigned int 4字节无符号整数
            data = struct.pack('<I16sI40s', version, key, plain_file_size, reserve)
            # 写入头文件
            fileobj.write(data)

            # version = struct.pack('I', version)
            # size = struct.pack('I', plain_file_size)
            # iv = struct.pack('16s', key)
            # 写入加密文件
            fileobj.write(content)

        # 读取验证是否写入
        with open(enc_file_path, 'rb') as fileobj:
            new_content = fileobj.read()


if __name__ == '__main__':
    # 密钥
    encryptKey = "6agrioBE1D9yoGOX4yyDMyMFs72jYvJ8"

    aesCipher = AESCipherOld(encryptKey)
    enc_data = aesCipher.aes_encrypt("这是一个测试")
    print(enc_data)
    print(aesCipher.aes_decryppt(enc_data))
    # /Users/conanmu/code/github/python/studyPython/data/obama.jpg
    # base_path = os.path.dirname(os.path.abspath(__file__)) + '/data'
    # base_path = "/Users/conanmu/code/github/python/studyPython/data/"
    # plain_file = base_path + '/obama.jpg'
    # enc_file = base_path + '/obama_encrypt.jpg'
    # dec_file = base_path + '/obama_decrypt.jpg'
    # aesCipher.enc_file(plain_file_path=plain_file, enc_file_path=enc_file)
    # aesCipher.dec_file(enc_file_path=enc_file, dec_file_path=dec_file)
