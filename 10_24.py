"""
Plan

1.) Create a set to track visited nodes and res to track num of connected
components
2.) Iterate through the list of provinces, for each city
unvisited, recurse until we have visited cities for that
connected component
3.) For each province, add to set, check if the following
connection exists for its neighbors
4.) Increment result by 1
5.) Return number of connected components
"""


# def findCircleNum(isConnected):
#     res = 0
#     visited = set()

#     def dfs(start):
#         if start in visited:
#             return
#         visited.add(start)
#         for neighbor in range(len(isConnected[start])):
#             if isConnected[start][neighbor] == 1:
#                 dfs(neighbor)

#     for i in range(len(isConnected)):
#         if i not in visited:
#             dfs(i)
#             res += 1

#     return res 

# isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# print(findCircleNum(isConnected))  # 2
# isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# print(findCircleNum(isConnected))  # 3

# Definition for a Node.
"""
1.) Created a hashmap to store node values and create new copies
2.) Run DFS and recurse starting at the root node 
3.) 
"""
# def cloneGraph(node):
#     nodeStore = {}

#     def dfs(node):
#         if node in nodeStore:
#             return nodeStore[node]
        
#         copy = Node(node.val)
#         nodeStore[node] = copy 
#         for neighbor in node.neighbors:
#             copy.neighbors.append(dfs(neighbor))
#         return copy
    
#     return dfs(node) if node else None


# adjList = [[2,4],[1,3],[2,4],[1,3]]
# print(cloneGraph(adjList))  # [[2,4],[1,3],[2,4],[1,3]]

def keysRooms(rooms):
    visited = set()

    def dfs(room):
        if room in visited:
            return 
        
        visited.add(room)
        for key in rooms[room]:
            dfs(key)
    
    dfs(0)
    return len(visited) == len(rooms)
    

rooms = [[1],[2],[3],[]]
print(keysRooms(rooms)) # True
rooms = [[1,3],[3,0,1],[2],[0]]
print(keysRooms(rooms)) # False
