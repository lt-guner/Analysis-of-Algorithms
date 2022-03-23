"""
EXPLANATION

NOTE: This is a lot like the current implementation of the combination problem. There are several differences.
1) The array needs to be sorted first with A.sort() in order to make sure we move up the list correctly and we don't
make entries that are essentially the same, such as [1,3,2] and [1,2,3].
2) Instead of passing continuously passing i in the recursively, i+1 must must be used in order to ensure we are
checking the index after the current index. We cannot use the same index twice.
3) Since the output list will be in order and there can be multiple [1,2,2] for example, we remove them using the map
and converting them to tuple sets to dedupe, then converting back to a list.

def amount_helper(nums, start, result, remainder, combination):

    #Base case
    if(remainder == 0):
        result.append(combination)
        return

    elif( remainder <0):
        return # sum exceeded the target

    for i := start to len(nums)-1:
        combination.append(nums[i])
        amount_helper(nums, i+1, result, remainder-nums[i], combination)
        #backtrack
        combination.pop()

def amount(A, S):

    A.sort()
    result = []
    amount_helper(A, 0, result, S,[])
    result = set(map(tuple,result))
    result = list(map(list,result))


TIME COMPLEXITY

This is polynomial time O(n^k)
"""

from copy import deepcopy

def amount_helper(nums, start, result, remainder, combination):

    # if we have the remainder of 0 then we have the correct combination and it needs to be added to results and return
    # for a pop
    if(remainder == 0):
        result.append(deepcopy(combination))
        return

    # if the remainder is less than 0 then we to return so the back tracking can be used for pop
    elif(remainder <0):
        return

    # iterate through start to length of numbers and append the nums current index value to combinations. Call
    # amount_helper recursively so the the it coins can be continuously iterated through until it the change is correct
    # or over negative. Then pop to check the next combination
    for i in range(start, len(nums)):
        combination.append(nums[i])
        amount_helper(nums, i+1, result, remainder-nums[i], combination)
        combination.pop()

def amount(A, S):

    # sort as A so we can go in order by smallest to largest. Create a blank list for results. Call the helper function
    # to start the cursive calls. Lastly dedupe the the list and return in revesre order.
    A.sort()
    result = []
    amount_helper(A, 0, result, S, [])
    result = set(map(tuple,result))
    result = list(map(list,result))
    result.sort(reverse=True)
    return result

if __name__ == '__main__':
    print(amount([1,2], 4))