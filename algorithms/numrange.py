class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        """Takes an array A of non-negative integers and a range specified by the second and third arguments, and returns the number of different consecutive slices in A having a sum in the specified range.

            Args:
                A: array of non-negative integers
                B: integer, the inclusive start of the range
                C: integer, the inclusive end of the range

            Returns:
                integer, the number of different consecutive slices in A having a sum in the specified range, e.g. for A = [ 0, 1, 2, 25, 2, 3 ], B = 1, C = 5, returns 8.

            Raises:
                TypeError.  Expecting array of non-negative integers for first argument, and integers for second and third arguments.
        """
        if not A:
            return 0
        num_ranges = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                current_sum = sum(A[i:j])
                if self.is_in_range(current_sum, B, C):
                    num_ranges += 1
                if j == len(A)-1:
                    if self.is_in_range(sum(A[i:]), B, C):
                        num_ranges += 1
                elif current_sum > C:
                    break
            if i == len(A)-1:
                    if self.is_in_range(A[i], B, C):
                        num_ranges += 1
        return num_ranges

    def is_in_range(self, n, a, b):
        """Returns true if the first argument is in the range specified by the second and third arguments, inclusive, false otherwise.

            Args:
                n: an integer
                a, b: both integers, representing a range

            Returns: bool.  True if n is in the range [a,b] or [b,a] inclusive, false otherwise

            Raises: TypeError.  Expecting three integers.
        """
        start = a if a < b else b
        end = a if start != a else b
        return (n >= start and n <= end)
