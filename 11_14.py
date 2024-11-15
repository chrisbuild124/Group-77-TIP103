def subsets(nums):
    res = []

    def backtracking(nums, subset, start):
        res.append(list(subset))
        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtracking(nums, subset, i + 1)
            subset.pop()

    backtracking(nums, [], 0)
    return res 


nums = [1,2,3]
print(subsets(nums))

nums = [0]
print(subsets(nums))



def generateParenthesis(n):
    res = []
    par_combo = []

    # def backtracking(open_par, closed_par):


    # backtracking(0, 0)
    return res 

n = 3
print(generateParenthesis(n))  # ["((()))","(()())","(())()","()(())","()()()"]

n = 1
print(generateParenthesis(n))  # ["()"]


