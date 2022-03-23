"""
EXPLANATION:

Take in two lists for hunger level per dog and how many treats of any size that are present. The two lists are sorted in
reverse so we we feed the hungriest dog the best biscuit size if the biscuit size satisfies the hunger level, meaning it
must be bigger than or equal to dogs hunger. The algorithm must return the number of dogs feed. Another variable is used
to increment the position of biscuit_size so it is not used again, I call it bisuits_uded. A single loop is used to
iterate through each dog. If a biscuit can feed that dog, then that increments biscuits_used (also used as index for
biscuit_size), number of dogs feed, and index of hunger_level. The loop will end if all dogs are iterated through or
break if all biscuits are used.


TIME COMPLEXITY:

The function uses the python sort function which of O(nlogn) and a single for loop of O(n). This means we have O(nlogn)
+ O(mlogm) (which is O(nlogn) but for biscuits) + O(n). This means we have a complexity of O(nlogn)
"""

def feedDog(hunger_level, biscuit_size):

    # dogs_feed and biscuits_used are used to keep track of how many dogs are feed and what point of the biscuit_size
    # list we need to start at.
    dogs_feed = 0
    biscuit_used = 0

    # reverse sort the dog hunger_level and biscuit_size and so the hungriest dog will get fed first if possible
    hunger_level.sort(reverse=True)
    biscuit_size.sort(reverse=True)

    # go through each dog to see if we can feed them a biscuit
    for x in range(0, len(hunger_level)):

        # if all biscuits have need used then break out of for loop to prevent out of bounds
        if biscuit_used == len(biscuit_size):
            break

        # the dog can be fed a biscuit then increment the dogs that were feed and the biscuits used
        if biscuit_size[biscuit_used] >= hunger_level[x]:
            dogs_feed += 1
            biscuit_used += 1

    # return the dogs_feed count
    return dogs_feed

