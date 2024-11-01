import heapq 
from collections import defaultdict

# def networkDelayTime(n, times, k):
#     adj = defaultdict(list)
#     for source, dest, time in times:
#         adj[source].append((dest,time))
    
#     visited = set()
#     total_time = 0
#     min_heap = [(0,k)]
#     while min_heap:
#         time, node = heapq.heappop(min_heap)
#         if node in visited:
#             continue 
#         visited.add(node)
#         total_time = max(total_time, time)
#         for neighbor, t in adj[node]:
#             if neighbor not in visited:
#                 heapq.heappush(min_heap,(t+time,neighbor))

#     return total_time if len(visited) == n else -1




# print(networkDelayTime(4, [[2,1,1],[2,3,1],[3,4,1]], 2)) # 2
# print(networkDelayTime(2, [[1,2,1]], 1)) # 1
# print(networkDelayTime(2, [[1,2,1]], 2)) # -1

def findRedundant(edges):
    pass
    