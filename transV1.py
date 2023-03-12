"""
Created April 22nd 2022
by Gabriel Espinoza Diaz
My first python project - a simple translator that has to be modified manually through the 'sequence' string to make changes
"""

sequence = "ATGCCCAGAGGATTATTCAGATAAATGTGGTGTTTCCAATATCAT"

DNA = {
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F", 
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G", 
    "CAT": "H", "CAC": "H", 
    "ATA": "I", "ATT": "I", "ATC": "I", 
    "AAA": "K", "AAG": "K", 
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L", 
    "ATG": "M", 
    "AAT": "N", "AAC": "N", 
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P", 
    "CAA": "Q", "CAG": "Q", 
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R", 
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S", 
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T", 
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V", 
    "TGG": "W", 
    "TAT": "Y", "TAC": "Y", 
    "TAA": "___", "TAG": "___", "TGA": "___", 
}

aasequence = ""

for i in range(int((len(sequence)/3))):
    aasequence += DNA.get(sequence[3*i:3*i+3])

print(aasequence)

