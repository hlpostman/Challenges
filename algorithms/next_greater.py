class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        """Takes a list A of integers and returns a list where the ith element in the return list is the value of A[j] for the smallest j such that j > i and A[j] > A[i], or -1 if no such j exists.

            Args: list of integers

            Returns: list of integers

            Raises: TypeError - expecting list of intgers
        """
        dict = {(A[i], i):-1 for i in range(len(A))} # Initialize dict to keep order.  Key is 2-tuple of array element and index.  Value initialized to -1, but algorithm will update this to next greater when next greater exists
        stack = [(A[0],0)] # Initialize to the first element of the input array
        for i in range(1,len(A)):
            while stack and A[i] > stack[-1][0]:
                dict[stack.pop()] = A[i]
            stack.append((A[i],i))
        return_array = [dict.get(key) for key in [(A[i], i) for i in range(len(A))] ]
        return return_array
