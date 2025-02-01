import random
import string

def str_xor(phrase='110313162c02475200'):
    secret = bytes.fromhex(phrase).decode('latin1')
    key = ''.join(random.choices(string.ascii_letters, k=5))
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)     
    data = "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
    return "".join([f"{ord(c):02x}" for c in data])
