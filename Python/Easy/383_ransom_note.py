#https://leetcode.com/problems/ransom-note/description/

def can_construct(ransom_note, magazine):

    h = {}

    for i in magazine:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1

    for i in ransom_note:
        if i not in h or h[i] > 0:
            return False
            
        h[i] -= 1

    return True




