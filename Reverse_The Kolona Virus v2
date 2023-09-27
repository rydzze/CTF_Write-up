*Unzip The_Kolona_Virus_2.zip file and convert the python compile file into the source code.* <br>
*Under the same directory as the file, use command `uncompyle6 spread_kolona.pyc > spread_kolona.py` to convert the file into a Python source code.
After that, we will get this source code as a result*

```python
kolona_genome = open('MT568643', 'r').read()
kolona_rna = [
 9728, 9150, 9459, 25263, 1634, 27368, 11779, 19149, 9629, 2721]
kolona_rna2 = [5676, 10615, 13415, 16286, 17093, 13804, 26647, 26800, 4547, 13208]
original_virus = open('original_virus', 'r').read()
evolve_virus = ''

for i in range(len(original_virus)):
    evolve_virus += chr((ord(original_virus[i]) - ord(kolona_genome[kolona_rna[i % 10]]) - ord(kolona_genome[kolona_rna2[i % 10]])) % 256)

exec evolve_virus
```
