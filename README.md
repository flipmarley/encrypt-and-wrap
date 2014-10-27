encrypt-and-wrap
================

Generate encrypted messages wrapped in a self-decrypting python script

usage: python enc.py _password_ > _out.py_<br>
where password is the encryption password and out.py is the message/script file<br>
the message to encrypt is read from stdin.

to decrypt use: python out.py _password_<br>
this will print the message to stdout.
