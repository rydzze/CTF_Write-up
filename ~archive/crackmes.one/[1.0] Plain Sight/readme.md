## Plain Sight

### 📚 Overview

A beginner friendly crackme that hides the answer in plain sight ;)

### ✨ Solution

When we run the programme, it will ask for a password.

```bash
┌──(kali@kali)-[~/Downloads]
└─$ ./plain_sight      
Enter the password: pass
Wrong password!
```

Decompile the .ELF file using Ghidra/IDA, go to the `Login` function and you will find the password.

```c
__int64 Login(void)
{
  __int64 v0; // rax
  char v2[40]; // [rsp+0h] [rbp-30h] BYREF

  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v2);
  std::operator<<<std::char_traits<char>>(&std::cout, "Enter the password: ");
  std::operator>><char,std::char_traits<char>,std::allocator<char>>(&std::cin, v2);
  if ( (unsigned __int8)std::operator==<char,std::char_traits<char>,std::allocator<char>>(v2, "do_not_hardcode") )
    v0 = std::operator<<<std::char_traits<char>>(&std::cout, "Welcome!");
  else
    v0 = std::operator<<<std::char_traits<char>>(&std::cout, "Wrong password!");
  std::ostream::operator<<(v0, &std::endl<char,std::char_traits<char>>);
  return std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v2);
}
```

```bash
┌──(kali@kali)-[~/Downloads]
└─$ ./plain_sight      
Enter the password: do_not_hardcode
Welcome!
```

### 🏳️ Password

Hence, the password is `do_not_hardcode`



                       