"""
Plan

1.) Row, Col variable to track row and col and check bounds
2.) A variable to track what color number we want to change
3.) We start at the given position, and use DFS to recurse
4.) Check all 4 directions, if number matches start number, change it
5.) End recursion for that specific direction if number != match
6.) Return modified 2d array 

"""

# def flood_fill(image, sr, sc, color):
#     rows, cols = len(image), len(image[0])
#     originalColor = image[sr][sc]

#     def dfs(r, c):
#         if r < 0 or r >= rows:
#             return 
#         if c < 0 or c >= cols:
#             return 
#         if image[r][c] != originalColor or image[r][c] == color:
#             return
        
#         image[r][c] = color
#         dfs(r - 1, c)
#         dfs(r + 1, c)
#         dfs(r, c - 1)
#         dfs(r, c + 1)
    
#     dfs(sr, sc)
#     return image


# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# color = 2
# print(flood_fill(image, sr, sc, color))
# image = [[0,0,0],[0,0,0]]
# sr = 0
# sc = 0
# color = 0
# print(flood_fill(image, sr, sc, color))

"""
Plan

1.) Row, Col variable to track row and col and check bounds
2.) We start at the given position, and iterate until we find 
the first matching character
4.) Recurse through using DFS to check the 4 directions
5.) Check if the word string is empty, out of bounds, nonmatching
character or character we've already visited
6.) If the character is valid, mark it and recurse through ]
the 4 directions, reduce string by [1:] if valid chaarcter


"""

# def exist(board, word):
#     rows, cols = len(board), len(board[0])
#     def dfs(r, c, word, board):
#         if word == "":
#             return True 
#         elif r < 0 or r >= rows:
#             return False
#         elif c < 0 or c >= cols:
#             return False
#         elif board[r][c] == '#':
#             return False 
#         elif board[r][c] != word[0]:
#             return False
#         board[r][c] = '#'
#         if (dfs(r+1, c, word[1:], board) or dfs(r-1, c, word[1:], board) or \
#             dfs(r, c+1, word[1:], board) or dfs(r, c-1, word[1:], board)):
#             return True
#         board[r][c] = word[0]
        
#     for r in range(rows):
#         for c in range(cols):
#             if dfs(r, c, word, board):
#                 return True
            
#     return False
        

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
# print(exist(board, word))  # True

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"
# print(exist(board, word))  # True

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"
# print(exist(board, word))  # False
from collections import deque

def orangesRotting(grid):
    queue = deque()
    time = 0
    fresh_oranges = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                queue.append((row,col))
            elif grid[row][col] == 1:
                fresh_oranges += 1
    # pop queue and infect orange, add oranges to queue and 
    return -1 
        
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))