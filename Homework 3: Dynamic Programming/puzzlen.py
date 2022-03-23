def puzzle(n):

    # this is the brute force approach in which we repeat each subproblem multiple times even when they occurred by the
    # iterative approach without memoization
    if n < 1:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2

    return puzzle(n-1) + puzzle(n-2)


def puzzle_bottom_up(n):

    # these are the first base cases that need to be established that can exit the code if these are what are passed
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    # create a puzzle_table the size of n and assign index 0 as 1 and index 1 as 2 because these are the base cases for
    # the first two inputs of n
    puzzle_table = [0] * (n)
    puzzle_table[0] = 1
    puzzle_table[1] = 2

    # the current index puzzle_table[i] is the sum of the previous two indexes
    for i in range(2, n):
        puzzle_table[i] = puzzle_table[i-1] + puzzle_table[i-2]

    # return puzzle_table
    return puzzle_table[i]

if __name__ == "__main__":
    print(puzzle(1))
    print(puzzle_bottom_up(100))