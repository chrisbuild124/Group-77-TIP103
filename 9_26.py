# Plan
"""

"""
def shift_letters(s, shifts):
    res = ""
    shift_length = len(shifts)
    total_shift = 0

    for i in range(shift_length - 1, -1,-1):
        total_shift += shifts[i] # 9
        char = s[i] #c
        asc = ord(char)
        new_char = asc + total_shift
        new_letter = chr(new_char)
        res += new_letter

    return res

s= "abc""
hifts = [3,5,9]]
print(shift_letters(s, shifts))


# Plan
"
"def smatrix_zeroessmatrix:

    R = len(matrix)
    C = len(matrix[0])
    set_col = set()
    set_row = set()
    for row in range(R):
        for col in range(C):
            if matrix[row][col] == 0:
                set_col.add(col)
                set_row.add(row)
    
    for row in range(R):
        for col in range(C):
            if col in set_col or row in set_row:
                matrix[row][col] = 0
    
    #return
 matrix
smatrix = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix_zeroes(matrix))O
#Plan
"""

"""
def longest_rep(s, k):
    start = 0
    output = 0
    freq_map = {}
    for end in range(len(s)):
        if s[end] not in freq_map:
            freq_map[s[end]] = 0
        freq_map[s[end]] += 1

        while (end - start + 1) - max(freq_map.values()) > k:
            freq_map[s[start]] -= 1
            if freq_map[s[start]] == 0:
                freq_map.pop(s[start])
            start += 1

        output = max(end - start + 1, output)
    return output 

s = "ABAB"
k = 2
# Output: 4
print(longest_rep(s, k))

s = "AABABBA"
k = 1
# Output: 4
print(longest_rep(s, k))

