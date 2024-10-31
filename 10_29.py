'''
    *Node can be VISITED (append to result), NOT VISITED, or VISITING (where we check for cycle)
    0. create a set for visited
    1. build adjacency list
    2. dfs on each node using that list
    3. base case: if cycle/node already in visited -- return
    4. recursive case: dfs on every prerequisite
    5. add node to visited set and result output
'''

# def findOrder(numCourses, prerequisites):
#     adj = { i: [] for i in range(numCourses) }
#     for course, prereq in prerequisites:
#         adj[course].append(prereq)
#     # print(adj)
#     res = []
#     visited = set()
#     cycle = set()
#     def dfs(course):
#         if course in cycle:
#             return False 
#         if course in visited:
#             return True 
#         for pre in adj[course]:
#             if dfs(pre) == False:
#                 return 
#         visited.add(course)
#         res.append(course)
#         return True
        
#     for course in range(numCourses):
#         if dfs(course) == False:
#             return []
#     return res

# print(findOrder(2, [[1,0]]))
# # Output [0, 1]
# print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
# # Output [0,2,1,3]
# print(findOrder(1, []))
# # Output [0]

def checkIfPrerequisite(numCourses, prerequisites, queries):
    res = [None]*len(queries)

    adj = { i: [] for i in range(numCourses) }
    for course, prereq in prerequisites:
        adj[course].append(prereq)

    prereq_map = {}

    def dfs(course):
        if course is not in prereq_map:
            prereq_map[course] = set()
            # x, y
            # x = x.union(y)
        for prereq in adj[course]:
           return_set= dfs(prereq)
           prereq_map[course].    
            
    for course in range(numCourses):
        dfs(course)
    
    # traverse through each query 

    
    return res

numCourses = 2
prerequisites = [[1,0]]
queries = [[0,1],[1,0]]
print(checkIfPrerequisite(numCourses, prerequisites, queries))  # [false,true]

numCourses = 2
prerequisites = []
queries = [[1,0],[0,1]]
print(checkIfPrerequisite(numCourses, prerequisites, queries))  # [false,false]

numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]
print(checkIfPrerequisite(numCourses, prerequisites, queries))  # [true,true]