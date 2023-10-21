## challName

### 📚 Overview

Get the flag by entering two keys

### ✨ Solution

Decompile the `twokeys` file by using [IDA Free](https://hex-rays.com/ida-free/) and press F5 to view the source code.

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+1Ch] [rbp-24h]
  char v5[11]; // [rsp+22h] [rbp-1Eh] BYREF
  char v6[11]; // [rsp+2Dh] [rbp-13h] BYREF
  unsigned __int64 v7; // [rsp+38h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  printf("Enter first key: ");
  __isoc99_scanf("%10s", v5);
  printf("Enter second key: ");
  __isoc99_scanf("%10s", v6);
  for ( i = 0; i <= 9; ++i )
  {
    if ( ((unsigned __int8)v6[i] ^ (unsigned __int8)v5[i]) != enc[i] )
    {
      printf("Wrong key pair =(");
      return 0;
    }
  }
  printf("Correct key pair!! The flag is %s%s", v5, v6);
  return 0;
}
```

In short, the code will XOR every character of the `first key` with every character of the `second key` with the same index to obtain `enc` (You got the idea ;)).
We are able to find the value of `enc[]` as it is already stored within the programme. Now, we have to find the `first key`.

Since the programme itself will display the flag and the loop will iterate 10 times, it is safe to say that the `first key` is "WSCTF2021{".
Then, I find the `second key` using a simple script that XOR `first key` with `enc`

```python
enc = [0x0f, 0x63, 0x11, 0x60, 0x0a, 0x03, 0x56, 0x01, 0x10, 0x06]
key1 = "WSCTF2021{"

key1_ascii = [ord(char) for char in key1]

key2 = []
for i in range(len(enc)):
    key2.append(enc[i] ^ key1_ascii[i % len(key1_ascii)])
key2 = ''.join([chr(byte) for byte in key2])

print("flag: ", key1+key2)
```

### 🏳️ Flag

Hence, the flag is `WSCTF2021{X0R4L1f3!}`
