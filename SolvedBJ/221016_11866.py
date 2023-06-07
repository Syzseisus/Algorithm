class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        
        if self is other or self.item == other.item:
            return True
        
        return False
    
    def __str__(self):
        return f"{self.item}"

    
class CircularSinglyLinkedList:
    def __init__(self, N):
        self.head = Node("1")
        curr = self.head
        for i in range(2, N + 1):
            curr.next = Node(str(i))
            curr = curr.next
        self.tail = curr
        self.tail.next = self.head
        self.count = N

    def shift_head(self, k):
        for _ in range(k):
            self.head = self.head.next
            self.tail = self.tail.next

    def delete_head(self):
        item = self.head.item
        if self.head == self.head.next:
            self.head = None

        else:
            new_head = self.head.next
            self.head = new_head
            self.tail.next = self.head
        self.count -= 1
        return item

    def __len__(self):
        return self.count
    
    def __str__(self):
        if self.head is None:
            return '[]'
        
        else:
            items = []
            
            curr = self.head
            
            while curr.next != self.head:
                items.append(curr.item)
                curr = curr.next
            items.append(curr.item)

            return f"{items}"

'''(7, 3)
1 2 3 4 5 6 7
4 5 6 7 1 2     -> 3
7 1 2 4 5       -> 6
4 5 7 1         -> 2
1 4 5           -> 7
1 4             -> 5
'''

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

Q = deque(range(1, N + 1))

answer = []
while Q:
    for _ in range(K - 1):
        Q.append(Q.popleft())
    answer.append(str(Q.popleft()))

# print("<", end='')
# for i in range(N - 1):
#     print(f"{answer[i]}, ", end='')
# print(f"{answer[-1]}>")

print("<" + ", ".join(answer) + ">")

# Q = CircularSinglyLinkedList(N)

# # print("<", end='')
# # while len(Q) > 1:
# #     Q.shift_head(K - 1)
# #     print(Q.delete_head(), end=', ')
# # print(Q.delete_head(), ">", sep='')

# arr = []
# for _ in range(N):
#     Q.shift_head(K - 1)
#     arr.append(Q.delete_head())
# print("<" + ", ".join(arr) + ">")