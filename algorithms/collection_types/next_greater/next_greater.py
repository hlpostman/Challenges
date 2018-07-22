# next_greater.py
# 22 July 2018

def next_greater(arr):
    """ Takes an array of integers and returns an array where for every element arr[i] in the input array, return_array[i] is the elment arr[j] where arr[j] > arr[i] and j is the smallest j such that j > i.  If no such element arr[j] exists for a given i, return_array[i] is -1.  Space and time complexity are both linear.

        Args: array of integers

        Returns: array of integers

        Raises:
            TypeError: expected array of integers
    """
    dict = {(arr[i], i):-1 for i in range(len(arr))} # Initialize dict to keep order.  Key is 2-tuple of array element and index.  Value initialized to -1, but algorithm will update this to next greater when next greater exists
    stack = [(arr[0],0)] # Initialize to the first element of the input array
    for i in range(1,len(arr)):
        while stack and arr[i] > stack[-1][0]:
            dict[stack.pop()] = arr[i]
        stack.append((arr[i],i))
    return_array = [dict.get(key) for key in [(arr[i], i) for i in range(len(arr))] ]
    return return_array
