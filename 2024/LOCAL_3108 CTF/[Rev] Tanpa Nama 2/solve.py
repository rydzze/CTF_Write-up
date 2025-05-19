hex_values = ['44h', '46h', '47h', '4Fh', '0Ch', '14h', '18h', '13h', '12h', '28h', '14h', '16h', '1h', '12h', '28h', '1Ah', '16h', '19h', '1Eh', '16h', '14h', '0Ah']
enc_flag = [int(value[:-1], 16) for value in hex_values]

flag = ''.join(chr(enc_flag[i] ^ 0x31 ^ 0x8 ^ 0x19 ^ 0x57) for i in range(len(enc_flag)))
print(flag)