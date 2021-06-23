def longestPalin(s):
    len_of_str = len(s)
    if len_of_str <= 1: 
        return s
    min_start, max_len, i = 0, 1, 0
    while i < len_of_str:
        if len_of_str - i <= max_len / 2: 
            break
        
        j, k = i, i
        while k < len_of_str - 1 and s[k] == s[k + 1]: 
            k += 1
        
        i = k + 1
        while k < len_of_str - 1 and j and s[k + 1] == s[j - 1]:  
            k, j = k + 1, j - 1
        
        if k - j + 1 > max_len: 
            min_start, max_len = j, k - j + 1
    return s[min_start: min_start + max_len]


