# Author: Timur Guner
# Class: CS325
# Term: Fall 2021
# Assignment 4: PowerSet.py

import copy

def powerset_helper(pointer, choices_made,inputs, result):
    """
    The time complexity is O(2^N)

    PSUEDOCODE from module

    def powerset_helper(pointer, choices_made,input, result):
        if (pointer < 0)):
            append choices_made to results # make a deep copy since we are working with objects
            return

        append input[pointer] to choices_made
        powerset_helper(pointer-1, choices_made, input, result)
        #backtracking
        remove last element added to choices_made
        powerset_helper(pointer - 1, choices_made, input, result)


    def powerset(input):
        result = []
        powerset_helper(len(input)-1, [], input, result)
        return result
        """
    # we need to make sure the pointer is in range
    if (pointer < 0):

        # make a deep copy since we are working with object
        deep_copy = copy.deepcopy(choices_made)
        result.append(deep_copy)

        return

    # append input[pointer] to choices_made
    choices_made.append(inputs[pointer])

    # then recursively call the powerset_helper with what is currently stored in results and decrement pointer
    powerset_helper(pointer-1, choices_made, inputs, result)

    # backtracking
    # remove last element added to choices_made and decrement pointer until we arrive at a situation where the algorithm
    # can select a new path
    choices_made.pop()
    powerset_helper(pointer-1, choices_made, inputs, result)

def powerset(input):

    # this function is the main function that will hold the results from the helper function and return the the sets
    result = []
    input.sort(reverse=True)
    powerset_helper(len(input)-1, [], input, result)
    return result

if __name__ == '__main__':
    print(powerset([1,3,2,5,4]))