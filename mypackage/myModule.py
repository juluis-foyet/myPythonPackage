def top_n(items, n):
    """ This function returns top n items in a array in descending order.

    Args:
        items (array): List or array-like object
        n (int): number of top items to be returned

    Return:
        array: top n items, in descending order
    
    Egs:
        >>> top_n([15, 48, 36, 95, 78], 3)
        [48, 78, 95]
    """

    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items) - 1 - i):

             if items[j] > items[j + 1]: # if this item is bigger than next item...
                 items[j], items[j + 1] = items[j + 1], items[j] # swap the two
    
    # get last two items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]