import sys
sys.setrecursionlimit(5000)

class Node:
    def __init__(self, val, x):
        self.val = val # 노드 번호
        self.x = x
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, nodeinfo):
        if self.root is None: self.root = Node(nodeinfo[0], nodeinfo[1])
        else:
            parent = None
            cur = self.root
            
            while cur is not None: # 노드 삽입 위치 탐색
                parent = cur
                if nodeinfo[1] < cur.x: cur = cur.left
                else: cur = cur.right
                
            if nodeinfo[1] < parent.x: parent.left = Node(nodeinfo[0], nodeinfo[1])
            else: parent.right = Node(nodeinfo[0], nodeinfo[1])

    def preorder(self):
        traversed = []
        
        def __preorder(node):
            if node is None: return
            traversed.append(node.val)
            __preorder(node.left)
            __preorder(node.right)
            
        __preorder(self.root)
        return traversed
    
    def postorder(self):
        traversed = []
        
        def __postorder(node):
            if node is None: return
            __postorder(node.left)
            __postorder(node.right)
            traversed.append(node.val)
            
        __postorder(self.root)
        return traversed

def solution(nodeinfo):
    binary_tree = BinaryTree()
    
    # (노드 번호, 노드 x축, 노드 y축)의 형식으로 구성된 리스트를 레벨 내림차순으로 정렬
    complete_nodeinfo = sorted([(val+1, node[0], node[1]) for val, node in enumerate(nodeinfo)], \
                               key=lambda tuple_node: -tuple_node[2])
    
    # print(complete_nodeinfo)
    for node in complete_nodeinfo:
        binary_tree.insert(node)
        
    return [binary_tree.preorder(), binary_tree.postorder()]