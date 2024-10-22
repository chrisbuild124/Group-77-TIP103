class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

def list_to_tree(lst):
  if not lst or not lst[0]:
    return None
  root = TreeNode(lst[0])
  q = deque([root])
  i = 1
  while q and i < len(lst):
    current = q.popleft()
    if i < len(lst) and lst[i] is not None:
      current.left = TreeNode(lst[i])
      q.append(current.left)
    i += 1
    if i < len(lst) and lst[i] is not None:
      current.right = TreeNode(lst[i])
      q.append(current.right)
    i += 1
  return root
  
  
def tree_to_list(root):
    if not root: return
    # BFS using queue
    printable_list = []
    curr_lvl = [root]
    while curr_lvl:
        next_lvl = []
        for node in curr_lvl:
            printable_list.append(node.val)
        if node.left:
            next_lvl.append(node.left)
        if node.right:
            next_lvl.append(node.right)
        curr_lvl = next_lvl
    return printable_list

# '''
#     Plan:
#     1. Check if the root, exists, if so, add to queue, if not, return 0
#     2. Add the root into our queue, and then check each node's children
#     3. Increase depth by 1 after exploring all nodes and adding children
#     4. If node has no .left and .right, return the minimum depth
# '''


# def minDepth(root):
#     if not root:
#       return 0
    
#     queue = [root]
#     depth = 1

#     while queue:
#         for _ in range(len(queue)):
#             node = queue.pop(0)
#             if not node.left and not node.right:
#                 return depth
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         depth += 1

#     return depth


# root = list_to_tree([3,9,20,None,None,15,7])
# print(minDepth(root))  # 2
# root = list_to_tree([2,None,3,None,4,None,5,None,6])
# print(minDepth(root)) #5

'''
    Plan:
    1. DFS 
    2. Base case: if not root: return
    3. Check each node's descendants if the node is 0 we prune it root.lef/right = None
    4. Recusive check through each subtree-> left/right 
'''


# def pruneTree(root):
#     if not root:
#         return 
    
#     root.left = pruneTree(root.left)
#     root.right = pruneTree(root.right)

#     if not root.right and not root.left:
#        if root.val == 0:
#           root = None 
    
#     return root


# root = list_to_tree([1,None,0,0,1])
# print(tree_to_list(pruneTree(root)))



# def sortedArrayToBST(nums):
#     mid = len(nums) // 2
    
#     if mid < 0 or mid > len(nums) - 1:
#        return 
#     root = TreeNode(nums[mid])
#     root.left = sortedArrayToBST(nums[:mid])
#     root.right = sortedArrayToBST(nums[mid+1:])

#     return root


# nums = [-10,-3,0,5,9]
# print(tree_to_list(sortedArrayToBST(nums))) # [0,-3,9,-10,null,5]

# nums = [1,3]
# print(tree_to_list(sortedArrayToBST(nums))) # [3,1]

'''
    Plan:
    1. Initialize a dictionary to track sum frequencies key: subtree sum value: times values occurs
    2. Visit each node post-order and then recurse down each node's subtree to find the sum at that node
    3. Sum of the subtree would be node.val + node.left + node.right
    4. Check if it exists in our dictionary, if it does, then we just increment += 1
    5. Add a new key/value with the key being the sum and the value being the frequency
'''
from collections import Counter

def findFrequentTreeSum(root):
    freq = Counter()
    res = []

    def helper(node):
       if not node:
          return 0
       
       left = helper(node.left)
       right = helper(node.right)

       total = node.val + left + right 
       freq[total] += 1
       return total

    helper(root)
    max_value = max(freq.values())

    for sums in freq.keys():  # dang
        if freq[sums] == max_value:
            res.append(sums)
            
    return res


root = list_to_tree([5,2,-3])
print(findFrequentTreeSum(root))  [2,-3,4]
        
root = list_to_tree([5,2,-5])
print(findFrequentTreeSum(root)) # [2]
 