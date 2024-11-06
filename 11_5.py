from collections import defaultdict

def accountsMerge(accounts):
    graph = defaultdict(set)
    emails = set()
    data = []
    for account in accounts:
        name = account[0]
        currentEmail = account[1]
        for email in account[2:]:
            graph[currentEmail].add(email)
            graph[email].add(currentEmail)
            # johnsmith@mail.com {john_newyork@gmail.com}
    
    
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(accountsMerge(accounts))


"""
Understand

Run DFS down until we reach the target sum
Use backtracking to track current sum 

"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def pathSum(root, targetSum):
#     res = []

#     def dfs(node, arr, curSum):
#         if not node:
#             return 
#         curSum += node.val
#         if not node.left and not node.right:
#            if curSum == targetSum:
#                 arr.append(node.val)
#                 res.append(arr)
#         return (dfs(node.left, arr + [node.val], curSum) or dfs(node.right, array + [node.val], curSum))
    
#     dfs(root, [], 0)
#     return res 

root = [5,4,8,11,null,13,4,7,2,null,null,5,1]
targetSum = 22
print(pathSum(root, targetSum)) # [[5,4,11,2],[5,8,4,5]]
