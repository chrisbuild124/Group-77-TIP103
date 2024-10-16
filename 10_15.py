# '''
#     Plan:
#     1. Init: deque
#     2. Ping: check if front of queue is < t - 3000
#     3. If so, dequeue from queue
#     4. Enqueue t
#     5. Return len(queue)
# '''
# from collections import deque

# class RecentCounter(object):

#     def __init__(self):
#         self.q = deque()
#         self.time = 3000

#     def ping(self, t):
#         self.q.append(t)
#         while self.q[0] < t - self.time:
#             self.q.popleft()

#         return len(self.q)

# recentCounter = RecentCounter();
# print(recentCounter.ping(1));     
# # Returns 1
# print(recentCounter.ping(100));   
# # Returns 2
# print(recentCounter.ping(3001));   
# # Returns 3
# print(recentCounter.ping(3002));  
# # Returns 3

# '''
#     Plan:
#     1. Initialize two stacks s1 and s2
#     2. Push: append x to s1
#     3. Pop: 
# '''

# class MyQueue(object):

#     def __init__(self):
#         self.s1 = []
#         self.s2 = []

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         self.s1.append(x)

#     def pop(self):
#         """
#         :rtype: int
#         """
#         if self.s2:
#             return self.s2.pop()
#         else:
#             while self.s1:
#                 self.s2.append(self.s1.pop())
#             return self.s2.pop()

#     def peek(self):
#         """
#         :rtype: int
#         """
#         if self.s2:
#             return self.s2[-1]
#         else:
#             while self.s1:
#                 self.s2.append(self.s1.pop())
#             return self.s2[-1]

#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return not self.s1 and not self.s2


# # Your MyQueue object will be instantiated and called as such:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()


# myQueue = MyQueue()
# myQueue.push(1) # queue is: [1]
# myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
# print(myQueue.peek()) # return 1
# print(myQueue.pop()) # return 1, queue is [2]
# print(myQueue.empty()) # return false

# def validateStackSequences(pushed, popped):
#         """
#         :type pushed: List[int]
#         :type popped: List[int]
#         :rtype: bool
#         """
#         stack = []
#         i = 0
#         for value in pushed:
#             stack.append(value)
#             while stack and stack[-1] == popped[i]:
#                 stack.pop()
#                 i += 1

#         return len(stack) == 0

# pushed, popped = [1,2,3,4,5], [4,5,3,2,1]
# print(validateStackSequences(pushed, popped))
# # Returns True

# pushed, popped = [1,2,3,4,5], [4,3,5,1,2]
# print(validateStackSequences(pushed, popped))
# # Returns False


def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    stack = []
    for a in asteroids:
        if not stack:
            stack.append(a)
        else:
            # check for collision
            while a < 0 and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                # Keep checking values until bigger asteroid can stop
                elif stack[-1] == abs(a):
                    stack.pop()
                # Break to stop loop if asteroid is bigger stack[-1]
                break
            else:
                stack.append(a)

    return stack

asteroids = [5,10,-5]
print(asteroidCollision(asteroids))

asteroids = [8,-8]
print(asteroidCollision(asteroids))

asteroids = [10,2,-5]
print(asteroidCollision(asteroids))