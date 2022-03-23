def kthelement(Arr1, Arr2, k):

    # initialize counters to 0
    i = 0
    j = 0
    x = 0

    # initialize empty array
    ktharray = [0] * (len(Arr1) + len(Arr2))

    # exist if k is out of range
    if k < 1 or k > len(Arr1) + len(Arr2):
        return False

    # while both counters are less than the length of both arrays
    while i < len(Arr1) and j < len(Arr2):

        # if the current index of Arr1 is less than Arr2 index, then add Arr1 index to ktharray at index x
        # then increment i and x
        if Arr1[i] < Arr2[j]:
            ktharray[x] = Arr1[i]
            i+=1
            x+=1

        # else do the same above except for Arr2
        else:
            ktharray[x] = Arr2[j]
            j+=1
            x+=1

    # if i is still less than len of Arr1 then continue iterating through and adding the elements to ktharray
    while i < len(Arr1):
        ktharray[x] = Arr1[i]
        i+=1
        x+=1

    # if j is still less than len of Arr2 then continue iterating through and adding the elements to ktharray
    while j < len(Arr2):
        ktharray[x] = Arr2[j]
        j+=1
        x+=1
    # return the value at kth term from the user
    return ktharray[k-1]

if __name__ == '__main__':
    Arr1 = [1, 2, 3, 5, 6, 8]
    Arr2 = [3, 4, 5, 6, 7]
    print(kthelement(Arr1,Arr2,0))