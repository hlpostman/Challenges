import unittest
import permutations

class TestPermute(unittest.TestCase):
     def test_general(self):
         input1 = [1,2,3]
         correct_output1 = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
         input2 = [1,2,3,4]
         correct_output2 = [[1,2,3,4], [1,2,4,3], [1,3,2,4], [1,3,4,2], [1,4,2,3], [1,4,3,2], [2,1,3,4], [2,1,4,3], [2,3,1,4], [2,3,4,1], [2,4,1,3], [2,4,3,1], [3,1,2,4], [3,1,4,2], [3,2,1,4], [3,2,4,1], [3,4,1,2], [3,4,2,1], [4,1,2,3], [4,1,3,2], [4,2,1,3], [4,2,3,1], [4,3,1,2], [4,3,2,1]]

         self.assertEqual(permutations.get_permutations(input1), correct_output1)
         self.assertEqual(permutations.get_permutations(input2), correct_output2)

     def test_non_unique(self):
         input1 = [1,1,1]
         correct_output1 = [[1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1]]
         self.assertEqual(permutations.get_permutations(input1), correct_output1)
     
     def test_corner(self):
         input1 = []
         correct_output1 = []
         input2 = [1]
         correct_output2 = [[1]]
         self.assertEqual(permutations.get_permutations(input1), correct_output1)
         self.assertEqual(permutations.get_permutations(input2), correct_output2)

     def test_bad_input(self):
         pass # raising correct errors (type, value, etc) for bad type of input, for wrong number of arguments, bad type in input array, etc.
if __name__ == "__main__":
    unittest.main()