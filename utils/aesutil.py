"""
python3 加解密
mac:
pip install pycryptodome

window:
pip install crypto
pip install pycryptodome

CBC加密需要一个十六位的key(密钥)和一个十六位iv(偏移量)
ECB加密不需要iv

"""
import os
from base64 import b64encode, b64decode

from Crypto.Cipher import AES

BLOCK_SIZE = AES.block_size


class AESCipher:
    def __init__(self, secretkey: str):
        self.key = secretkey  # 密钥
        self.iv = secretkey[0:16]  # 偏移量

    def enc_file(self, plain_file_path, enc_file_path):
        """
        加密文件
        :param plain_file_path: 明文文件路径
        :param enc_file_path: 加密后文件路径
        :return:
        """
        with open(plain_file_path, 'rb') as fileobj:
            content = fileobj.read()
            # 加密文件
            enc_content = self.encrypt(content)

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
            dec_content = self.decrypt(content)
        with open(dec_file_path, 'wb') as f:  # 以二进制写类型打开
            f.write(dec_content)  # 写入文件

    def encrypt(self, text):
        """
        加密 ：先补位，再AES加密，后base64编码
        :param text: 需加密的明文
        :return:
        """
        # 包pycryptodome 的加密函数不接受str
        text = self.__pad(text).encode()
        cipher = AES.new(key=self.key.encode(), mode=AES.MODE_CBC, IV=self.iv.encode())
        encrypted_text = cipher.encrypt(text)
        # 进行64位的编码,返回得到加密后的bytes，decode成字符串
        return b64encode(encrypted_text).decode('utf-8')

    def decrypt(self, encrypted_text):
        """
        解密 ：偏移量为key[0:16]；先base64解，再AES解密，后取消补位
        :param encrypted_text : 已经加密的密文
        :return:
        """
        encrypted_text = b64decode(encrypted_text)
        cipher = AES.new(key=self.key.encode(), mode=AES.MODE_CBC, IV=self.iv.encode())
        decrypted_text = cipher.decrypt(encrypted_text)
        return self.__unpad(decrypted_text).decode('utf-8')

    def __pad(self, text):
        """
        填充方式，
        # 不足BLOCK_SIZE的补位(s可能是含中文，而中文字符utf-8编码占3个位置,gbk是2，所以需要以len(s.encode())，而不是len(s)计算补码)
        pad = lambda s: s + (BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE)
        """
        amount_to_pad = AES.block_size - (len(text.encode()) % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return text + (pad * amount_to_pad)

    def __unpad(self, text):
        """
        去除填充
        该方法等同于下面lambda表达式
        unpad = lambda s: s[:-ord(s[len(s) - 1:])]
        :param text:
        :return:
        """
        pad = text[-1]
        return text[:-pad]


if __name__ == '__main__':
    # 密钥
    encryptKey = "6agrioBE1D9yoGOX4yyDMyMFs72jYvJ8"
    aesCipher = AESCipher(encryptKey)
    # 加密
    enc_data = aesCipher.encrypt("哈哈哈")
    print(enc_data)
    # 解密
    print(aesCipher.decrypt(enc_data))

    # /Users/conanmu/code/github/python/studyPython/data/obama.jpg
    # base_path = os.path.dirname(os.path.abspath(__file__)) + '/data'
    base_path = "/Users/conanmu/code/github/python/studyPython/data/"
    plain_file = base_path + '/obama.jpg'
    enc_file = base_path + '/obama_encrypt.jpg'
    dec_file = base_path + '/obama_decrypt.jpg'
    aesCipher.enc_file(plain_file_path=plain_file, enc_file_path=enc_file)
    aesCipher.dec_file(enc_file_path=enc_file, dec_file_path=dec_file)
