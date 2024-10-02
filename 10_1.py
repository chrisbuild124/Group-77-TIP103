"""
Plan

1.) Initialize two pointers, one at the beginning and end
of our string
2.) Check if each character is alphanumeric, skip over 
alphanumeric characters
3.) If it is alphanumeric, convert to lower and check if equal
4.) Return false if not equal



"""

def is_palindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1

        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    
    return True

s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))
# True


s = "race a car"
print(is_palindrome(s))
# False


s = " "
print(is_palindrome(s))
# True




"""
Plan



"""

def three_sum(nums):
    return



nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
# [[-1,-1,2],[-1,0,1]]



nums = [0,1,1]
print(three_sum(nums))
# [ ]


nums = [0,0,0]
print(three_sum(nums))
# [[0,0,0]]
