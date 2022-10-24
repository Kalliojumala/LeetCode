#Given a string s, return the longest palindromic substring in s.
#A string is called a palindrome string if the reverse of that string is the same as the original string.

def solution_o2(s):
    sub_str = ""
    for i in range(len(s)+1):
        if len(sub_str) >= len(s) - i:
            break

        for j in range(len(s)+1, i, - 1):
            if len(s[i:j]) < len(sub_str):
                break
            if s[i:j] == s[i:j][::-1]:
                if len(s[i:j]) > len(sub_str):
                    sub_str = s[i:j]
                    break

    return sub_str





  
print(solution_o2("saippuakauppias" * 50))
s = "cbbd"
