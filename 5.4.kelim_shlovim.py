# The function takes in an arbitrary number of lists as positional arguments and yields the elements of these lists
# in an interleaved order
def interleave(*lists):
    index = 0
    max_len = max(len(lst) for lst in lists)
    while index < max_len:
        for lst in lists:
            if index < len(lst):
                yield lst[index]
        index += 1


print(list(interleave('abc', [1, 2, 3], ('!', '@', '#'))))
