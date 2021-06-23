def chooseandswap(A)
    list_of_unique_chars = list()
    for i in A:
        if i not in list_of_unique_chars:
            list_of_unique_chars.append(i)
    for i in range(0, len(list_of_unique_chars) - 1):
        if list_of_unique_chars[i] > list_of_unique_chars[i + 1]:
            return A.replace(list_of_unique_chars[i], "_").replace(list_of_unique_chars[i+1], list_of_unique_chars[i]).replace("_", list_of_unique_chars[i+1])
    return A

