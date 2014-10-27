#!/usr/bin/python
"""
Generate encrypted messages wrapped in a self-decrypting python script
usage: python enc.py password > out.py
where password is the encryption password and out.py is the message/script file
to decrypt use: python out.py password
this will print the message to stdout.
"""

import sys, random

def encrypt(key, msg):
    encrypted = []
    for i, c in enumerate(msg):
	key_c = ord(key[i % len(key)])-32
	msg_c = ord(c)-32
	encrypted.append(chr(((msg_c + key_c) % 95)+32))
    return ''.join(encrypted)

def decrypt(key, enc):
    msg=[]
    for i, c in enumerate(enc):
        key_c = ord(key[i % len(key)])-32
        enc_c = ord(c)-32
	msg.append(chr(((enc_c - key_c) % 95)+32))
    return ''.join(msg)

def make_randstr(msg_len):
    sl = []
    r = random.SystemRandom()
    for i in range(msg_len):
        sl.append(chr(r.randint(32,126)))
    return ''.join(sl)

if __name__ == '__main__':
    msg = sys.stdin.read().replace("\n","\\n").replace("\t","\\t")
    randstr = make_randstr(len(msg))
    key = encrypt(sys.argv[1], randstr)
    encrypted = encrypt(key, msg)
    decrypted = decrypt(key, encrypted)
    if not msg == decrypted:
        raise Exception("Encryption Fail")

    print """
#!/usr/bin/python

import sys
    
def encrypt(key, msg):
    encrypted = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])-32
        msg_c = ord(c)-32
        encrypted.append(chr(((msg_c + key_c) % 95)+32))
    return ''.join(encrypted)

def decrypt(key, enc):
    msg=[]
    for i, c in enumerate(enc):
        key_c = ord(key[i % len(key)])-32
        enc_c = ord(c)-32
        msg.append(chr(((enc_c - key_c) % 95)+32))
    return ''.join(msg)

if __name__ == '__main__':"""
    print "\trandstr = ", repr(randstr)
    print "\tenc = ", repr(encrypted)
    print "\tkey = encrypt(sys.argv[1], randstr)"
    print "\tdecrypted = decrypt(key, enc).replace(\"\\\\n\",\"\\n\").replace(\"\\\\t\",\"\\t\")"
    print "\tprint decrypted"

