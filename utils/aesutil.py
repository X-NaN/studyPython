"""
python3 加解密
mac:
pip install pycryptodome

window:
pip install crypto
pip install pycryptodome

"""
import binascii
import os
import struct

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESUtil:
    def __init__(self, secKey: str):
        """
        初始化密钥和偏移量
        :param secKey: 密钥,密钥应由16位，24位，32位字母或数字组成
        """
        self.key = secKey  # 密钥
        self.iv = secKey[0:16]  # 偏移量, 截取密钥前16位

    def enc_file(self, plain_file_path, enc_file_path):
        """
        加密文件
        :param plain_file_path: 明文文件路径
        :param enc_file_path: 加密后文件路径
        :return:
        """
        with open(plain_file_path, 'rb') as fileObj:
            content = fileObj.read()
            # 加密文件
            enc_content = self.aes_encrypt(plain_data=content, key=self.key, iv=self.iv)
        with open(enc_file_path, 'wb') as f:  # 以二进制写类型打开
            f.write(enc_content)  # 写入文件

    def dec_file(self, enc_file_path, dec_file_path):
        """
        解密文件
        :param enc_file_path: 加密文件路径
        :param dec_file_path: 解密文件路径
        :return:
        """
        with open(enc_file_path, 'rb') as fileObj:
            content = fileObj.read()
            # 解密头
            version, key1, enc_content_length, reserve = struct.unpack('<I16sI40s', content[0:64])
            dec_content = self.aes_decrypt(enc_data=content[64:], key=self.key, iv=self.iv)
        with open(dec_file_path, 'wb') as f:  # 以二进制写类型打开
            f.write(dec_content)  # 写入文件

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

    def aes_encrypt(self, plain_data, key, iv):
        """
        aes  cbc 128
        CBC加密需要一个十六位的key(密钥)和一个十六位iv(偏移量)
        加密函数，如果data不是16的倍数【加密文本data必须为16的倍数！】，那就补足为16的倍数
        :param plain_data:明文数据 16位
        :param key:  16位
        :param iv:16位
        """
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))  # 设置AES加密模式 此处设置为CBC模式

        # 填充数据
        pad_data = self.__pad(text=plain_data)
        encrypted_data = cipher.encrypt(pad_data)  # aes加密
        # encrypted= base64.b64encode(Cipher.encrypt(pad_data))
        # 返回的二进制数据的十六进制表示。每一个字节的数据转换成相应的2位十六进制表示。
        result = binascii.b2a_hex(encrypted_data)  # b2a_hex encode  将二进制转换成16进制
        return encrypted_data

    def aes_decrypt(self, enc_data, key, iv):
        """aes解密
        :param key:
        :param data:
        """
        cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
        dec_data = cipher.decrypt(enc_data)

        unpad_data = self.__unpad(dec_data)

        # 字符串转16进制
        result = binascii.hexlify(unpad_data)
        return unpad_data

    def _encryptFile(self, srcFilePath, dstFilePath, encryptKey):
        fileSize = os.path.getsize(srcFilePath)
        self.enc_file(plain_file_path=srcFilePath, enc_file_path=dstFilePath, key=encryptKey)
        return self.append_struct_info_to_encFile(key=encryptKey, plain_file_size=fileSize, enc_file_path=dstFilePath)

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
        enc_content_length = os.path.getsize(enc_file_path)
        headLength = 0

        with open(enc_file_path, "rb+") as fileobj:
            content = fileobj.read()
            fileobj.seek(0)
            # 小端，unsigned int 4字节无符号整数
            data = struct.pack('<I16sI40s', version, key, enc_content_length, reserve.encode())
            # 写入头文件
            fileobj.write(data)
            headLength = len(data)
            # version = struct.pack('I', version)
            # size = struct.pack('I', plain_file_size)
            # iv = struct.pack('16s', key)
            # 写入加密文件
            fileobj.write(content)

        # 读取验证是否写入
        with open(enc_file_path, 'rb') as fileobj:
            new_content = fileobj.read()

        return headLength


if __name__ == '__main__':
    # /Users/conanmu/code/github/python/studyPython/data/obama.jpg
    # base_path = os.path.dirname(os.path.abspath(__file__)) + '/data'
    base_path = "/Users/conanmu/code/github/python/studyPython/data/"
    plain_file = base_path + '/obama.jpg'
    enc_file = base_path + '/obama_encrypt.jpg'
    dec_file = base_path + '/obama_decrypt.jpg'
    # 密钥
    encryptKey = "6agrioBE1D9yoGOX4yyDMyMFs72jYvJ8"
    aesUtil = AESUtil(encryptKey)
    # 加密
    aesUtil.enc_file(plain_file_path=plain_file, enc_file_path=enc_file)
    # 解密
    aesUtil.dec_file(enc_file_path=enc_file, dec_file_path=dec_file)
