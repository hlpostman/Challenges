# dutch_national_flag_problem.py
# 25 July 2018

def dutch_national_flag_problem(pivot_index, A):
    """Orders the elements of the array A passed into three groups: those that are less than the v, where v is the value of A[pivot_index] before function execution, at the front, those that are equal to v after those less than v, and those that are greater than v after those equal to v.  Does this in O(n) time with O(1) space.

        Args:
            pivot_index: integer, must be a valid index of A, i.e. must be in range(0, len(A))
            A: array of integers

        Returns: None

        Raises:
            TypeError: Expecting first argument an integer and second argument an array of integers
            ValueError: pivot_index is not a valid index of A, i.e. is not in the range(0, len(A))
    """
    pivot = A[pivot_index]
    small, equal, large = 0, 0, len(A) - 1

    while equal < large:
        if A[equal] < pivot:
            A[equal], A[small] = A[small], A[equal]
            equal += 1
            small += 1
        elif A[equal] == pivot:
            equal += # Leave the element undisturbed
        else: # A[equal] > pivot
            A[equal], A[large] = A[large], A[equal]
            large -= 1
