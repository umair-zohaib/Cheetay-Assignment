from itertools import permutations
def printLargest(arr):
    res_list = []
    for p in permutations(arr, len(arr)):
        val = "".join(map(str, p))
        res_list.append(val)
    return max(res_list)

