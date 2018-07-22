# longest_consecutive_sequence.py
# 22 July 2018

def longest_consecutive_sequence(arr):
    """Takes an unsorted array of integers and returns an integer that represents the length of the longest consecutive sequence that could be made out of the elements of the input array without duplicates.  Does this in O(n) time.

        Args: array of integers

        Returns: integer

        Raises:
            TypeError: expected array of integers
    """
    length_of_longest_consecutive_sequence = 1
    hash = set(arr)
    while hash:
        elt = hash.pop()
        start = elt - 1
        while start in hash:
            hash.remove(start)
            start -= 1
        end = elt + 1
        while end in hash:
            hash.remove(end)
            end += 1
        if end - start - 1> length_of_longest_consecutive_sequence:
            length_of_longest_consecutive_sequence = end - start - 1
    return length_of_longest_consecutive_sequence
