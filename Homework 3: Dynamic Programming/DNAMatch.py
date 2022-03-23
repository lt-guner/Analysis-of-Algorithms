# author: Timur Guner
# assignment 3: LCS
# class: CS325

#---------- TOP-DOWN APPROACH ------------

def dna_match_topdown(DNA1, DNA2):

    # create a point for the to dna strings and a blank 2 by 2 array
    i = 0
    j = 0
    dnamatch = [['' for x in range(len(DNA2) + 1)] for x in range(len(DNA1) + 1)]

    # call the recursive helper function to pass the dna strings the pointers and the 2d array for memoization
    return dna_match_topdown_helper(DNA1, DNA2, i, j, dnamatch)

def dna_match_topdown_helper(DNA1, DNA2, i, j, dnamatch):

    # if the either pointer is out of bounds then store 0 in the corresponding matrix as 0
    if i == len(DNA1) or j == len(DNA2):
        dnamatch[i][j] = 0
        return dnamatch[i][j]

    # if the letter in DNA1 is the same in DNA2 then do either of the following
    # if [i+1][j+1] already has a variable stored in then pull that variable and 1 and store it in [i][j]
    # else recursive call this function with i+1 and j+1 pointers and add 1 when call is complete
    elif DNA1[i] == DNA2[j]:
        if dnamatch[i+1][j+1] != '':
            dnamatch[i][j] = 1 + dnamatch[i+1][j+1]
            return dnamatch[i][j]
        else:
            dnamatch[i][j] = 1 + dna_match_topdown_helper(DNA1, DNA2, i+1, j+1, dnamatch)
            return dnamatch[i][j]

    # else we make a recursive call call of max (i+1, j) and (i, j+1) and they are for options to choose
    # if both pointers have values stored in the dnamatch matrix then find the max between the two
    # two cases if one of the indexes is filled and the other isnt in dnamatch, then pull the index that has the value and recursive call the other in this functions
    # else find the max between two recursive calls for the two indexes
    else:
        if dnamatch[i+1][j] != '' and dnamatch[i][j+1] != '':
            dnamatch[i][j] = max(dnamatch[i+1][j], dnamatch[i][j+1])
            return dnamatch[i][j]
        elif dnamatch[i+1][j] != '':
            dnamatch[i][j] = max(dnamatch[i+1][j],dna_match_topdown_helper(DNA1, DNA2, i, j+1, dnamatch))
            return dnamatch[i][j]
        elif dnamatch[i][j+1] != '':
            dnamatch[i][j] = max(dna_match_topdown_helper(DNA1, DNA2, i+1, j, dnamatch),dnamatch[i][j+1])
            return dnamatch[i][j]
        else:
            dnamatch[i][j] = max(dna_match_topdown_helper(DNA1, DNA2, i+1, j, dnamatch),dna_match_topdown_helper(DNA1, DNA2, i, j+1, dnamatch))
            return dnamatch[i][j]

#----------- Bottom Up Approach -----------

def dna_match_bottomup(DNA1, DNA2):

    # save the length of DNA1 and DNA2 and create a 2d table for saving data
    n = len(DNA1)
    m = len(DNA2)
    dnamatch = [[0 for x in range(m+1)] for x in range(n+1)]

    # we have a double for loop here that iterates through the length of each string by starting at index 1 to keep
    # the first row and first column 0
    for x in range(1,n+1):
        for y in range(1,m+1):

            # if the letters match at index x-1 and y-1 then we take the value that is in dnamatch[x-1[y-1] which is
            # diaginally up left and add 1 when placing it in dnamatch[x][y]
            if DNA1[x-1] == DNA2[y-1]:
                dnamatch[x][y] = dnamatch[x-1][y-1] + 1

            # else store the max between the left cell or up cell in dnamatch[x][y]
            else:
                dnamatch[x][y]= max(dnamatch[x-1][y] , dnamatch[x][y-1])

    # return dnamatch[x][y] which contains the longest sequence
    return dnamatch[x][y]


if __name__ == "__main__":

    DNA1 = 'ATAG'
    DNA2 = 'GT'
    print(dna_match_bottomup(DNA1,DNA2))
    print(dna_match_topdown(DNA1, DNA2))