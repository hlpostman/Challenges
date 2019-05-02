# test_knuth_morris_pratt.py
# May 2019

import unittest
from knuth_morris_pratt import knuth_morris_pratt_algorithm, longest_repeated_prefix

class TestKnuthMorrisPratt(unittest.TestCase):

    def test_general(self):
        input1_str, input1_substr = "aefaefaefaedaefaedaefaefa", "aefaedaefaefa"
        correct_output1 = True
        actual_output1 = knuth_morris_pratt_algorithm(input1_str, input1_substr)
        self.assertEqual(correct_output1, actual_output1)
    
    def test_corner(self):
        pass
    
    def test_longest_repeated_prefix(self):
        input1 = "aa"
        correct_output1 = "a"
        input2 = "aab"
        correct_output2 = "a"
        input3 = "aba"
        correct_output3 = "a"
        input4 = "a"
        correct_output4 = ""
        input5 = ""
        correct_output5 = ""
        input6 = "aefaedaefaefa"
        correct_output6 = "aefae"
        self.assertEqual(longest_repeated_prefix(input1), correct_output1)

if __name__ == "__main__":
    unittest.main()