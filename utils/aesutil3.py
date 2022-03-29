# -*- encoding: utf-8 -*-
"""
python3/mac:
pip install pycryptodome

python3/window:
pip install crypto
pip install pycryptodome

CBC加密需要一个十六位的key(密钥)和一个十六位iv(偏移量)
ECB加密不需要iv

"""
import binascii
import os
import struct
from base64 import b64encode, b64decode

from Crypto.Cipher import AES

BLOCK_SIZE = AES.block_size


class AESCipher:
    def __init__(self, seckey):
        """

        :param seckey:
        """
        self.key = seckey  # 密钥16位
        self.iv = seckey[0:16]  # 偏移量16位

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
        return text + (pad * amount_to_pad).encode()

    def __unpad(self, text):
        # pad = ord(text[-1])
        pad = text[-1]
        return text[:-pad]

    def encrypt(self, plain_data):
        """
        aes  cbc 128
        CBC加密需要一个十六位的key(密钥)和一个十六位iv(偏移量)
        加密函数，如果data不是16的倍数【加密文本data必须为16的倍数！】，那就补足为16的倍数
        :param plain_data:明文数据 16位
        """
        cipher = AES.new(self.key.encode('utf-8'), AES.MODE_CBC, self.iv.encode('utf-8'))  # 设置AES加密模式 此处设置为CBC模式

        # 填充数据
        pad_data = self.__pad(text=plain_data)
        # aes加密
        encrypted_data = cipher.encrypt(pad_data)
        return encrypted_data

    def decrypt(self, enc_data):
        """aes解密
        :param key:
        :param data:
        """
        cipher = AES.new(self.key.encode(), AES.MODE_CBC, self.iv.encode())
        dec_data = cipher.decrypt(enc_data)
        unpad_data = self.__unpad(dec_data)
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
            enc_content = self.encrypt(plain_data=content)
        with open(enc_file_path, 'wb') as f:  # 以二进制写类型打开
            f.write(enc_content)  # 写入文件

    def dec_file(self, enc_file_path, dec_file_path):
        """
        解密文件
        :param enc_file_path: 加密文件路径
        :param dec_file_path: 解密文件路径
        :return:
        """
        with open(enc_file_path, 'rb') as fileobj:
            content = fileobj.read()
            dec_content = self.decrypt(enc_data=content[64:])
        with open(dec_file_path, 'wb') as f:  # 以二进制写类型打开
            f.write(dec_content)  # 写入文件


if __name__ == '__main__':
    # 密钥
    encryptKey = "6agrioBE1D9yoGOX4yyDMyMFs72jYvJ8"
    aesCipher = AESCipher(encryptKey)
    # 加密
    enc_data = aesCipher.encrypt("哈哈哈")
    print(enc_data)
    # 解密
    print(aesCipher.decrypt(enc_data))

    # base_path = "/Users/conanmu/code/github/python/studyPython/data/"
    # plain_file = base_path + '/obama.jpg'
    # enc_file = base_path + '/obama_encrypt.jpg'
    # dec_file = base_path + '/obama_decrypt.jpg'
    # aesCipher.enc_file(plain_file_path=plain_file, enc_file_path=enc_file)
    # aesCipher.dec_file(enc_file_path=enc_file, dec_file_path=dec_file)
