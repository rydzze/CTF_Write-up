# The Kolona Virus v2
_please let me know if there are any mistakes ;)_



### |-o- First Step -o-|

Unzip The_Kolona_Virus_2.zip file and convert the Python compile file into the source code. <br> Under the same directory as the file, use command `uncompyle6 spread_kolona.pyc > spread_kolona.py` to convert the file into source code.

```python
kolona_genome = open('MT568643', 'r').read()
kolona_rna = [9728, 9150, 9459, 25263, 1634, 27368, 11779, 19149, 9629, 2721]
kolona_rna2 = [5676, 10615, 13415, 16286, 17093, 13804, 26647, 26800, 4547, 13208]
original_virus = open('original_virus', 'r').read()
evolve_virus = ''

for i in range(len(original_virus)):
    evolve_virus += chr((ord(original_virus[i]) - ord(kolona_genome[kolona_rna[i % 10]]) - ord(kolona_genome[kolona_rna2[i % 10]])) % 256)

exec(evolve_virus)
```

The source code will open `MT568643` file to read and save the content in a variable, `kolona_genome`.
`kolona_rna` and `kolona_rna2` are arrays that store 10 integers (index for characters in `MT568643` file).
`original_virus` variable will open `original_virus` file to read and save its content.
Lastly, `evolve_virus` variable is an empty string.
Next, the for() loop is used to loop every char from `original_virus` variable and SUB with the nested array of `kolona_genome` & `kolona_rna` and a nested array of `kolona_genome` & `kolona_rna2` ~~(sorry, idk how to explain it properly but you get the idea :D)~~.
So, this loop involves SUB operation and we can solve it by using [CyberChef](https://gchq.github.io/CyberChef/#recipe=SUB(%7B'option':'Hex','string':''%7D)SUB(%7B'option':'Hex','string':''%7D)).



### |-o- Second Step -o-|

Upload the `original_virus` file in the input section.

![image](https://github.com/arffrdzln/SKR-CTF_Write-up/assets/86187059/6ffb1bf6-c468-4214-8b70-b556fdbc28cf)

Now, insert the key from `MT568643` file. However, we cannot copy all of it because the `MT568643` file is not the key itself. The key consists of 10 characters that can be obtained by retrieving the characters from the `MT568643` file based on the index given from `kolona_rna` and `kolona_rna2` arrays and hence, we need two keys. So, we can script a simple for() loop for it to output the keys.

```python
kolona_genome = open('MT568643', 'r').read()
kolona_rna = [9728, 9150, 9459, 25263, 1634, 27368, 11779, 19149, 9629, 2721]
kolona_rna2 = [5676, 10615, 13415, 16286, 17093, 13804, 26647, 26800, 4547, 13208]

for i in range(len(kolona_rna)):
        print(chr(ord(kolona_genome[kolona_rna[i]])), end='')
print('')
for i in range(len(kolona_rna2)):
        print(chr(ord(kolona_genome[kolona_rna2[i]])), end='')

#Output
#CTTTTTTAGT   <-- Key 1
#CCCCGCATAC   <-- Key 2
```

Then, we can insert the keys and change the output format to UTF8.

![image](https://github.com/arffrdzln/SKR-CTF_Write-up/assets/86187059/0e64c4d1-5b21-47b6-8392-731f639dff14)

We will see another output which is a Python source code.

```python
kolona_genome = open("MT568643",'r').read()
kolona_rna1 = [23345, 11951, 3108, 5530, 21395, 4536, 27288, 1593, 15001, 3441, 21401, 16319, 3268, 24970, 25483, 26318, 3451, 19165, 23997, 9356]
kolona_rna2 = [26841, 22129, 29143, 13838, 29641, 28796, 11242, 6388, 11659, 19381, 11479, 15576, 25715, 13948, 8014, 6941, 23751, 11716, 22374, 21328]
evolved_virus = open("evolved_virus",'r').read()
code = ""

for i in range(len(evolved_virus)):
	code += chr((ord(evolved_virus[i]) - ord(kolona_genome[kolona_rna1[i % 20]]) - ord(kolona_genome[kolona_rna2[i % 20]])) % 256)
	
exec(code)
```

The source code will open `MT568643` file to read and save the content in a variable, `kolona_genome`.
`kolona_rna1` and `kolona_rna2` are arrays that store 20 integers (index for characters in `MT568643` file).
`evolve_virus` variable will open `evolve_virus` file to read and save its content.
Lastly, `code` variable is an empty string.
Next, the for() loop is used to loop every char from `evolve_virus` variable and again, SUB with the nested array of `kolona_genome` & `kolona_rna1` and a nested array of `kolona_genome` & `kolona_rna2`. We can solve it by using [CyberChef](https://gchq.github.io/CyberChef/#recipe=SUB(%7B'option':'Hex','string':''%7D)SUB(%7B'option':'Hex','string':''%7D)) just like before.



### |-o- Third Step -o-|

Upload the `evolved_virus` file in the input section.

![image](https://github.com/arffrdzln/SKR-CTF_Write-up/assets/86187059/f893b06d-8a09-4ed5-8156-ab30ffac0e23)

Script a simple for() loop to output the keys.

```python
kolona_genome = open("MT568643",'r').read()
kolona_rna1 = [23345, 11951, 3108, 5530, 21395, 4536, 27288, 1593, 15001, 3441, 21401, 16319, 3268, 24970, 25483, 26318, 3451, 19165, 23997, 9356]
kolona_rna2 = [26841, 22129, 29143, 13838, 29641, 28796, 11242, 6388, 11659, 19381, 11479, 15576, 25715, 13948, 8014, 6941, 23751, 11716, 22374, 21328]

for i in range(len(kolona_rna1)):
        print(chr(ord(kolona_genome[kolona_rna1[i]])), end='')
print('')
for i in range(len(kolona_rna2)):
        print(chr(ord(kolona_genome[kolona_rna2[i]])), end='')

#Output
#ATGCCATAACTGAAGCGAAA   <-- Key 1
#CACTATCTTGAATCATGTTA   <-- Key 2
```

Insert the keys and change the output format to UTF8.

![image](https://github.com/arffrdzln/SKR-CTF_Write-up/assets/86187059/e6e47e9e-0bf9-4bfc-92bc-2495298dbb84)

Once again, we will see another output which is a Python source code.

```python
import random
flag = open("flag.png","r")
kolona = open("flag.kolona","w+")
key = "SARS-CoV-2"
# Prevent Reverse Engineering!
random_num = random.randint(1,6666)

for i,c in enumerate(flag.read()):
	kolona.write(chr((ord(c) + ord(key[i % len(key)]) + random_num) % 256))
```

Based on the source code, `flag` variable will open flag.png file, `kolona` variable will write the output into `flag.kolona` file and the key given is "SARS-CoV-2". Then, we have `random_num` variable act as a randomiser that will give a random integer in the range of 1 to 6666. 



### |-o- Fourth Step -o-|


We can try to change `flag.kolona` file into `flag.png`, nonetheless, it is still corrupted. So, we can use [CyberChef](https://gchq.github.io/CyberChef/#recipe=ADD(%7B'option':'UTF8','string':''%7D)ADD(%7B'option':'Decimal','string':''%7D)) to recover the file.

Upload the `flag.kolona` file in the input section.

![image](https://github.com/arffrdzln/SKR-CTF_Write-up/assets/86187059/6dacbe69-f31b-49f0-8d83-8fec05ae9641)

ADD the key given, "SARS-CoV-2" and change the output format to UTF8.

![image](https://github.com/arffrdzln/SKR-CTF_Write-up/assets/86187059/05744419-f50f-4d42-8fd4-b7ea0b603df8)

However, we are still missing the second key that can be obtained from the randomiser, `random_num` variable. The key can help us to recover and read the file. What we can do now is change the file signature into PNG file signature.

```python
flag_kolona = "EA8DADA8224BB371151F"
flag_png = "89504E470D0A1A0A0000"
seckey = hex(int(flag_kolona, 16) - int(flag_png, 16))
# kolona + seckey = png   -->   - seckey = kolona - png

print(str(seckey)[2:].upper())
# OUTPUT
# - seckey = 613D5F6115419967151F
```
The code above is a script to find the value of the second key. For the file signature, let us take up to 20 bytes. Since the value of the second key should be negative, we will SUB the value and make sure the output format is HEX. 

![image](https://github.com/arffrdzln/SKR-CTF_Write-up/assets/86187059/eb3fcfe4-8756-44cc-bd86-faf31141e2e3)

After that, we will see the `PNG` file signature in the output and then a magic pen appeared beside the "Output" text. Click on it, the output will be displayed as well as the flag.

![image](https://github.com/arffrdzln/SKR-CTF_Write-up/assets/86187059/3e59b993-2107-4885-bda6-e33e4ca42f96)
