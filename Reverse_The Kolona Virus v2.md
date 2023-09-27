##### First Step

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
`kolona_rna` and `kolona_rna2` are arrays that store integers (index for `MT568643` file).
`original_virus` variable will open `original_virus` file to read and save its content.
Lastly, `evolve_virus` is an empty string.
Next, the for() loop is used to loop every char from `original_virus` variable and SUB with the nested array of `kolona_genome` & `kolona_rna` and a nested array of `kolona_genome` & `kolona_rna2` ~~(sorry, idk how to explain it properly but you get the idea :D)~~.
So, this loop involves SUB operation and we can solve it by using [cyberchef](https://gchq.github.io/CyberChef/#recipe=SUB(%7B'option':'Hex','string':''%7D)SUB(%7B'option':'Hex','string':''%7D)).

##### Second Step

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

#### Third Step
