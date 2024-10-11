# Plan
"""
1.) Create a set to store all unique characters
2.) Two pointers to iterate through the entire string
3.) 
"""

# def lengthLongest(s):
#     start = 0
#     maxLen = 0
#     unique_char = set()
#     for end in range(len(s)):
#         if s[end] not in unique_char:
#             unique_char.add(s[end])
#         else: # duplicate
#             while s[end] in unique_char:
#                 unique_char.remove(s[start])
#                 start += 1
#             unique_char.add(s[end])
#         maxLen = max(maxLen, end - start + 1)
#     return maxLen


# s = "abcabcbb"
# print(lengthLongest(s)) # output: 3
# s = "bbbbb"
# print(lengthLongest(s)) # output: 1
# s = "pwwkew"
# print(lengthLongest(s)) # output: 3




'''
Plan:

1. Create a hashmap to store each sorted value in its own subarray
2. Iterating through each string, sort it alphabetically and checking 
if its sorted key is in hashmap
3. Return hashmaps values
'''
# from collections import defaultdict

# def groupAnagram(strs):
#     sorted_dict = defaultdict(list)
#     for word in strs:
#         sorted_string = ''.join(sorted(word))
#         sorted_dict[sorted_string].append(word)

#     return sorted_dict.values()
    

# strs = ["eat","tea","tan","ate","nat","bat"]
# print(groupAnagram(strs)) # [["bat"],["nat","tan"],["ate","eat","tea"]]
# strs = [""]
# print(groupAnagram(strs)) # [[""]]
# strs = ["a"]
# print(groupAnagram(strs)) # [["a"]]

'''
Plan:

1. 
2. 
3.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return repr(self.val) + '->' + repr(self.next)

def link_list(lst):
    tmp = ListNode()
    curr = tmp
    for el in lst:
        curr.next = ListNode(el)
        curr = curr.next
    return tmp.next
        

def partitionList(head, x):
    low = ListNode()
    high = ListNode()
    lowHead = low
    highHead = high 
    
    curr = head 
    while curr:
        if curr.val < x:
            low.next = curr
            low = low.next 
        else:
            high.next = curr
            high = high.next 

        curr = curr.next 

    high.next = None
    low.next = highHead.next
    return lowHead.next

    
head = link_list([1,4,3,2,5,2])
x = 3    
print(partitionList(head,x)) # output: [1,2,2,4,3,5]
head = link_list([2,1])
x = 2
print(partitionList(head,x)) # output: [1,2]
