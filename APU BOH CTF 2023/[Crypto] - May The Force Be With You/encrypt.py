from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

import textwrap

def encrypt_file(file_path, password):
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    iv = get_random_bytes(AES.block_size)

    passwd = textwrap.dedent(password)[:-1]

    salt = b'salt123'  
    key = PBKDF2(passwd.encode(), salt, dkLen=16)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as file:
        file.write(ciphertext + iv)

    print("Encryption successful. Encrypted file saved as:", encrypted_file_path)

password = "ni5h2h?Yrq8Do?n+|6a;pKbZkv%}O~tV" 
file_path = "./flag.txt"   
encrypt_file(file_path, password)
