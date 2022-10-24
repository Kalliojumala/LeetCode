"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows.

Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
"""

def solution(s: str, num_of_rows: int = 1) -> str:
    pointer = 0
    direction = - 1
    checked_indices = 0
    hash_table = {}

    while checked_indices < len(s):
        
        if pointer == 0:                  #pointer increments until last row, then decrement until at first row again
            direction = +1
        elif pointer == num_of_rows - 1:
            direction = -1
        
        #hash table additions, each row is repped by one entry on table starting at 0. eg 0 = row1, 1= row2 of final str.
        #loop back and forth until every index of s is checked.
        if pointer not in hash_table:
            hash_table[pointer] = s[checked_indices]
        else:
            hash_table[pointer] = hash_table[pointer] +  s[checked_indices]

        checked_indices += 1
        pointer += direction 

    result_str = ""
    for i in range(len(hash_table)):                 #combine hash_table rows for final result
        result_str = result_str + hash_table[i]

    return result_str

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    num_rows = 3
    print(solution(s, num_rows))
    s = "A"
    num_rows = 3
    print(solution(s, num_rows))