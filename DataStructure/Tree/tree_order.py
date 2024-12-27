from binary_tree import Tree
"https://koosco.tistory.com/entry/Python-%ED%8A%B8%EB%A6%AC-%EA%B5%AC%ED%98%84-%EC%88%9C%ED%9A%8C%EC%A0%84%EC%9C%84-%EC%88%9C%ED%9A%8C-%EC%A4%91%EC%9C%84-%EC%88%9C%ED%9A%8C-%ED%9B%84%EC%9C%84-%EC%88%9C%ED%9A%8C-%EB%A0%88%EB%B2%A8-%EC%88%9C%ED%9A%8C"

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None
    def preorder(self):
        def _preorder(node):
            print(node.data, end = " ")
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)
    
    def inorder(self):
        def _inorder(node):
            if node.left:
                _inorder(node.left)
            print(node.data, end = " ")    
            if node.right:
                _inorder(node.right)
        _inorder(self.root)
                
    def postordder(self):
        def _postordder(node):
            if node.left:
                _postordder(node.left)

            if node.right:
                _postordder(node.right)
                
            print(node.data, end = " ")    
        _postordder(self.root)