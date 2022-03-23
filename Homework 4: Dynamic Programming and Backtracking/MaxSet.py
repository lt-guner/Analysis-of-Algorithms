# Author: Timur Guner
# Class: CS325
# Term: Fall 2021
# Assignment 4: MaxSet.py

import copy

def max_independent_set(nums):
    """
    The time complexity is O(N)
    """

    # handle use cases when list is empty or one slot.
    if len(nums) == 0:
        return ([],)

    if len(nums) == 1:
        return (nums, nums[0])

    # first things that need to be done
    # 1) we need a dynamic programming array that stores subarray
    # 2) the first subarray is equal to the first element of nums
    # 3) incl which is keeps track of the sum at a particle point of the nums including the current i-th, default is
    # nums[0]
    # 4) excl is the same except it doesnt't include the current i-th number in nums, default is 0
    dp = [[] for _ in nums]
    dp[0].append(nums[0])
    incl = nums[0]
    excl = 0

    # since nums can include negative numbers then we have to determine the sign of the starting value of nums
    # 1 for postive and 0 for negative
    sign = 1
    if nums[0] < 0:
        sign = 0

    # iterate through the nums stating at index 1 because nums[0] was added to already
    for i in range(1, len(nums)):

        # temp is used to update the incl later
        tmp = excl + nums[i]

        # if sign is 1 then this code will execute and not
        if sign == 1:
            # This is ran only when i = is 1 to prevent out of bounds issues
            # if the current nums is greater than what is stored in the current dp, then append nums[i] to dp[i]
            if i == 1 and nums[i] > dp[0][0]:
                dp[1].append(nums[1])
            # else copy append nums[0] to tp dp[1]
            elif i == 1:
                dp[1].append(nums[0])
            # if nums[i] is a negative, the copy over what is in dp[i-1] to dp[i]
            elif nums[i] < 0:
                deep_copy_incl = copy.deepcopy(dp[i - 1])
                dp[i] = deep_copy_incl
            # if everything above does not trigger than the following happens
            else:
                # if the incl is bigger than the excl then we are proceeding with creating a new sublist based on values
                # in the dp[i-1]
                if incl > excl:
                    # if all the conditions are met then only nums[i] needs to be added
                    if len(dp[i - 1]) == 1 and nums[i] > dp[i - 1][0] and dp[i - 1][0] < 0:
                        dp[i].append(nums[i])
                    # else copy over what is in dp[i-1] to dp[i] and append nums[i] if the last digit in the subarray
                    # doesnt the previous value in nums
                    else:
                        deep_copy_incl = copy.deepcopy(dp[i-1])
                        dp[i] = deep_copy_incl
                        if dp[i][-1] != nums[i-1]:
                            dp[i].append(nums[i])
                # else excl > incl so proceed just like above but with dp[i-2]
                else:
                    if len(dp[i - 2]) == 1 and nums[i] > dp[i - 2][0] and dp[i - 2][0] < 0:
                        dp[i].append(nums[i])
                    else:
                        deep_copy_excl = copy.deepcopy(dp[i - 2])
                        dp[i] = deep_copy_excl
                        dp[i].append(nums[i])

        # if the sign starts at 0 then the following code runs until a positive integer is found and will not run again
        else:
            # if nums[i] is positive then nums[i] is appended to dp[i] and sign is set to 1
            if nums[i] >= 0:
                dp[i].append(nums[i])
                sign = 1
            # the following code is run with n
            else:
                # if the current num[i] is greater than the previous dp then append nums[i] to dp[i]
                if nums[i] > dp[i - 1][0]:
                    dp[i].append(nums[i])
                # else the previous dp[i-1] is still the greatest so it gets copied into dp[i]
                else:
                    deep_copy_neg = copy.deepcopy(dp[i - 1])
                    dp[i] = deep_copy_neg

        excl = max(incl, excl)
        incl = tmp

    list_sub = dp[i]
    list_sum = sum(list_sub)

    return (dp[i], list_sum)


if __name__ == '__main__':
    print(max_independent_set([]))
    print(max_independent_set([7, 2, 5, 8, 6]))
    print(max_independent_set([-1, -1, 0]))
    print(max_independent_set([-3, -2, -4, -34, -50, -3, -12]))
    print(max_independent_set([2, 1, 18]))
    print(max_independent_set([5, 5, 4, 4, 5]))