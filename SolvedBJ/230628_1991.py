import sys

prt = lambda x: print(x, end="")

tree = {}


class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def preorder(node):
    if node.item:
        prt(node.item)
    if node.left:
        preorder(tree[node.left])
    if node.right:
        preorder(tree[node.right])


def inorder(node):
    if node.left:
        inorder(tree[node.left])
    if node.item:
        prt(node.item)
    if node.right:
        inorder(tree[node.right])


def postorder(node):
    if node.left:
        postorder(tree[node.left])
    if node.right:
        postorder(tree[node.right])
    if node.item:
        prt(node.item)


N = int(sys.stdin.readline())
for _ in range(N):
    P, L, R = sys.stdin.readline().strip().split()
    L = None if L == "." else L
    R = None if R == "." else R
    tree[P] = Node(P, L, R)

preorder(tree["A"])
prt("\n")
inorder(tree["A"])
prt("\n")
postorder(tree["A"])
