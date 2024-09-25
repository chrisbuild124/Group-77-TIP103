class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return repr(self.val) + '->' + repr(self.next)


def link_list(lst):
    if not lst:
        return None
    curr = tmp = ListNode()
    for el in lst:
        curr.next = ListNode(el)
        curr = curr.next
    return tmp.next


def swap_node(head):
    # 1. create temp head -> head
    # 2. check curr and curr.next, if they exist we assign the pointers
    # 3. we previously pointer, curr, second, next_p
    # 4. 
    temp = ListNode(0, next=head)
    curr = head
    prev = temp 

    while curr and curr.next:
        second = curr.next
        nxt_p = curr.next.next

        second.next = curr
        curr.next = nxt_p

        prev.next = second
        prev = curr
        curr = nxt_p
        
    return temp.next

head = link_list([1,2,3,4])
print(swap_node(head))
# [2,1,4,3]

head = link_list([ ])
print(swap_node(head))
# []

head = link_list([1])
print(swap_node(head))
# [1]





def rotate_list(head, k):
    if k == 0 or not head:
        return head

    n = 1
    tail = head 

    # Get the length of our LL
    while tail and tail.next:
        tail = tail.next
        n += 1

    k = k % n
    if k == 0:
        return head
    
    curr = head 
    for _ in range(k):
        curr = curr.next

    new_head = curr.next 
    curr.next = None 
    tail.next = head 
    
    return new_head

head = link_list([1,2,3,4,5])
print(rotate_list(head, 2))
# [4,5,1,2,3]

head = link_list([0,1,2])
print(rotate_list(head, 4))
# [2,0,1]



def remove_nth(head, n): 
    # one pass to get length, use temp pointer
    # iterate over length - n nodes
    # pointer.next = pointer.next.next
    temp = head 
    length = 1
    while temp and temp.next:
        temp = temp.next
        length += 1

    if length == n:
        return head.next
    return new_head

head = link_list([1,2,3,4,5])
print(remove_nth(head, 2))
# [4,5,1,2,3]
