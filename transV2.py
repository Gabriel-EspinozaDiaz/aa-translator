"""
Created February 28th 2023
by Gabriel Espinoza Diaz
A revamp of the original translator with class organization and some ability to deal with incorrect parameters or abnormalities
"""
from re import sub

class Translator:
    """
    This class accepts either a coding strand or a 
    """

    def __init__(self,strand):
        """
        Constructor
        """
        self.strand = str(strand).upper() #puts all characters in uppercase
        self.strand = ''.join(self.strand.split()) #removes whitespace
        self.aa = ''

        self.DNA = {
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

        self.RNA = {
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "UGU": "C", "UGC": "C",
        "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "UUU": "F", "UUC": "F", 
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", 
        "CAU": "H", "CAC": "H", 
        "AUA": "I", "AUU": "I", "AUC": "I", 
        "AAA": "K", "AAG": "K", 
        "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", 
        "AUG": "M", 
        "AAU": "N", "AAC": "N", 
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", 
        "CAA": "Q", "CAG": "Q", 
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R", 
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S", 
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", 
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", 
        "UGG": "W", 
        "UAU": "Y", "UAC": "Y", 
        "UAA": "___", "UAG": "___", "UGA": "___", 
        }
    
    def check_input(self):
        """
        Ensures that the code being given is either RNA or DNA, and that it only uses nucleotide codes. Returns True if DNA and False if RNA. 
        """
        
        coding = True
        checker = sub('[A,C,T,G,U]','',self.strand)
        if checker != '':
            raise Exception('Strand must only contain the letters A, C, G, T and U')
        if 'U' in self.strand:
            coding = False
            if 'T' in self.strand:
                raise Exception('Strand cannot contain both uracil and thymine')
            return coding
        elif 'T' in self.strand:
            if 'U' in self.strand:
                raise Exception('Strand cannot contain both uracil and thymine')
            return coding

    def check_round(self):
        """
        Print any nucleotides that don't fit into the last codon
        """
        if len(self.strand)%3 != 0:
            return True
        else:
            return False
    
    def round(self):
        """
        Print any nucleotides that don't fit into the last codon
        """
        return self.strand[-(len(self.strand)%3):]
    
    def translate(self):
        """
        EDIT Runs code to return a list with either 1 or 2 strings:
        the first contains the amino acid sequence, 
        the second will contain any extra nucleotides that didn't fit into the last codon
        """
        aasequence = ""
        RoD = Translator.check_input(self)

        if RoD:
            for i in range(int((len(self.strand)/3))):
                aasequence += self.DNA.get(self.strand[3*i:3*i+3])
            Translator.round(self)
            self.aa = aasequence
            return self.aa

        else:
            for i in range(int((len(self.strand)/3))):
                aasequence += self.RNA.get(self.strand[3*i:3*i+3])
            Translator.round(self)
            self.aa = aasequence
            return self.aa
        
    def __str__(self):
        return self.aa
        
    





class main():
    s1 = Translator('ACC ATG ATT ACG GAT TCA CTG GCC GTC GTT TTA CAA CGT CGT GAC TGG GAA AAC CCT GGC')
    s2 = Translator('UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU')
    sER1 = Translator('ABCDEFGHIJKL')
    print(s1.translate())
    print(s2.translate())
    print(sER1.translate())
    #print(s1)
