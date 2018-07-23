class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        """Takes a non-negative integer A and returns a (2A - 1) X (2A - 1) two-dimensional array with the property that when printed with each row on a new line right below the previous row, a series of nested rectangles is printed, with the integer A making the outer-most rectangle, A-1 as the next largest rectangle, and so on, down to 1 at the center.

            Args: non-negative integer

            Returns: 2-dimensional array of integers e.g. [[int]]

            Raises:
                TypeError: expecting integer
                ValueError: expecting nonengative integer
        """
        if A < 0:
            raise ValueError("Expecting nonengative integer.  Received %d.", A)
        # Initialize return array with first row
        return_array = [[A for _ in range(2*A - 1)]]

        # Top to center rows. Strategically subtract
        for i in range(1, A):
            return_array.append(return_array[i-1][:])
            for j in range(i, (2*A - 1) - i):
                return_array[i][j] -= 1

        # Center to bottom rows. Append symmetric rows
        for row in range(A-2, -1, -1):
            return_array.append(return_array[row])

        return return_array

# linear Solution
# recursive solution
