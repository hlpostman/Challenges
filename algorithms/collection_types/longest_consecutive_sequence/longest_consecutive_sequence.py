# longest_consecutive_sequence.py
# 22 July 2018

def longest_consecutive_sequence(arr):
    """Takes an unsorted array of integers and returns an array of the elements that would make up the longest consecutive sequence of integers if the input array were sorted, without duplicates.  Does this in O(n) time.

        Args: array of integers

        Returns: array of integers

        Raises:
            TypeError: expected array of integers
    """
    longest_consecutive_sequence = []
    hash = set(arr)
    while hash:
        elt = hash.pop()
        print(elt)
        start = elt - 1
        while start in hash:
            hash.remove(start)
            start -= 1
        end = elt + 1
        while end in hash:
            hash.remove(end)
            end += 1
        if end - start - 1> len(longest_consecutive_sequence):
            longest_consecutive_sequence = [i for i in range(start+1,end)]
            print(longest_consecutive_sequence)
    return longest_consecutive_sequence
