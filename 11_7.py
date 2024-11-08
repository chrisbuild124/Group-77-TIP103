# def largestNumber(nums):

#     def comparison(n1, n2):
#         return str(n1) + str(n2) > str(n2) + str(n1)

#     for i in range(len(nums), 0, -1):
#         for j in range(i - 1):
#             if not comparison(nums[j], nums[j+1]):
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]

#     res = ''
#     for num in nums:
#         str_num = str(num)
#         res += str_num

#     return res

# nums = [10,2]
# print(largestNumber(nums))
# #"210"
# nums = [3,30,34,5,9]
# print(largestNumber(nums))
# # '3' + '30' >< '30' + '3'
# # '30' + '34' <> '34' + '30'
# # 3, 34, 30, 5, 9
# #9,5,3,30,34
# # "9534330"


def adv_shuffle(nums1, nums2):
    pass

nums1 = [2,7,11,15]
nums2 = [1,10,4,11]
adv_shuffle(nums1, nums2) #[2,11,7,15]
nums1 = [12,24,8,32]
nums2 = [13,25,32,11]
adv_shuffle(nums1, nums2) #[24,32,8,12]

# 2 7 11 15
# 1 4 10 11

# [2,2,7,2,7,11]
# assigned
# 1 : [2]
# 4 : [7]
# 10 : [11]
# 11 : [15]

# 2 > 1
# 7 > 4
# 

def maxNumberOfFamilies(n, reservedSeats):
    pass 



n = 3
reservedSeats = [[1,2],[1,3],[1,8], [2,6],[3,1],[3,10]]