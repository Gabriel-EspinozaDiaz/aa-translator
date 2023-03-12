import unittest
from transV2 import Translator

class main(unittest.TestCase):

    def setUp(self):
        self.s1 = Translator('ACC ATG ATT ACG GAT TCA CTG GCC GTC GTT TTA CAA CGT CGT GAC TGG GAA AAC CCT GGC')
        self.s2 = Translator('UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU')
        self.sER1 = Translator('ABCDEFGHIJKL')
    
    def test_run(self):
        """
        Tests to ensure that the sequences are being translated to the correct string.
        """
        self.assertEqual(self.s1.translate(), 'TMITDSLAVVLQRRDWENPG')
        self.assertEqual(self.s2.translate(), 'FFFFFFFFFFFFF')



if __name__ == "__main__":
    unittest.main()


"""
s1 is the first 20 amino acids in the lacZ gene
s2 is the test that was used to determine that a codon comprised only of thymines codes for phenylalanine
"""
