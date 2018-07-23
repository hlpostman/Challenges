# kth_smallest.py

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        """Takes an array A of integers and an integer B and returns the Bth smallest integer in O(n) time with O(1) space.

            Args:
                A: array of integers
                B: integer

            Returns:
                integer, the Bth smallest element of A

            Raises:
                TypeError - expecting array of integers for first argument and integer for second argument.
        """
        start = min(A)
        end = max(A)
        found = False
        while not found:
            mid = (start + end) // 2
            num_elts_less_than_B = 0
            num_elts_less_than_or_equal_B = 0
            for elt in A:
                if elt < mid:
                    num_elts_less_than_B += 1
                if elt <= mid:
                    num_elts_less_than_or_equal_B += 1
            if num_elts_less_than_or_equal_B >= B and num_elts_less_than_B < B:
                return mid
            elif num_elts_less_than_B >= B:
                end = mid - 1
            else:
                start = mid + 1
