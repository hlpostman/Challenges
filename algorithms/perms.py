class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        """Takes a list A of integers and returns a list of all unique permutations of the elements in A.  Note that this algorithm computes duplicate permutations when A has duplicate elements, however by using a set as the data structure to which each permutation is added, only unique permutations are retained.  The return list is then created from the holding set.

            Args: list of integers

            Returns: list of list of integers (e.g. if A is [1,2], returns [[1,2], [2,1]])

            Raises: TypeError - expecting list of integers
        """
        def helper(i):
            if i == len(A) - 1:
                holding_set.add(tuple(A))
                return
            for j in range(i, len(A)):
                A[i], A[j] = A[j], A[i]
                helper(i+1)
                A[i], A[j] = A[j], A[i]
        holding_set = set() # Using a set ensures uniqueness
        helper(0)
        return list(holding_set)
