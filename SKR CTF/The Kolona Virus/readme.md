## The Kolona Virus

### 📚 Overview

OMG! My picture is corrupted with the Kolona virus! I managed to get the virus source code and the corrupted picture,
please help me recover it. I will give you a flag for reward!

### 🤔 Hint 

> _"Have you tried to "print" the virus?"_

### ✨ Solution

```python
kolona_genome = open("MN908947",'r').read() # Read the Genome
kolona_rna = open("kolona_virus","r").read() # Read the RNA
kolona_virus = ""

for i,k in enumerate(kolona_rna): # Decode RNA
	kolona_virus += chr(ord(k) ^ ord(kolona_genome[i % len(kolona_genome)]))

exec(kolona_virus) # Spread the virus
```

Let's break down the source code first.
1. `kolona_genome` will open `MN908947` file to read and then save the content.
2. `kolona_rna` will open `kolona_virus` file to read and then save the content.
3. `kolona_virus` is an empty string.
4. `For loop` will loop every character in `kolona_rna` and then it will XOR with the `kolona_genome` array.

With the help of [CyberChef](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'UTF8','string':''%7D,'Standard',false)),
we can solve this by putting the `kolona_virus` file as input and then XOR it with the text from `MN908947` file. 

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/50683395-acf5-48a8-b808-cf286dd46136)

```python
flag = open("flag.jpg","r")
kolona = open("flag.kolona","w+")
key = "COVID-19"

for i,c in enumerate(flag.read()):
	kolona.write(chr(ord(c) ^ ord(key[i % len(key)])))
```

Based on the source code given from the output, the process looks quite similar to the previous one.
`For loop` will loop every character in `flag.jpg` and then XOR it with the `key` string, which is "**COVID-19**".
However, `flag.jpg` is corrupted and the file is still corrupted if we rename `flag.kolona` to `flag.jpg`.

So, what we can do is open [CyberChef](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'UTF8','string':''%7D,'Standard',false))
and then put the `flag.kolona` file as input and XOR it with "**COVID-19**".

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/2ce8f9b1-30bd-4842-b0bd-c9c0b54229c2)

Then, click on the magic pen that appears beside the Output panel and it will render the image.

### 🏳️ Flag

![image](https://github.com/rydzze/CTF_Write-up/assets/86187059/927d68ff-d378-4ae3-8e4c-fe50c261bf9a)
