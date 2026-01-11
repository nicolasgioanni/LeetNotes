# Linear Time + Space
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        adjList = {}

        def clone(node):
            if not node:
                return None
            elif node in adjList:
                return adjList[node]
            
            newNode = Node(node.val)
            adjList[node] = newNode
            newNode.next, newNode.random = clone(node.next), clone(node.random)
            
            return newNode

        return clone(head)
