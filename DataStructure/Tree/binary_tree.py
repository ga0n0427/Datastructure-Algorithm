class Node:
    def __init__(self, data):
        self.data = data 
        self.parent = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        
    def search_tree(self, data):
        node = self.root
        while node:
            if data == node.data:
                return True
            elif data > node.data:
                node = node.left
            else:
                node = node.right
                
    def insert_Tree(self, data):
        new_node = Node(data)
        node = self.root
        if node == None:
            self.root = new_node
            return
        prev = None
        while node:
            prev = node
            if data == node.data:
                return False
            elif data > node.data:
                node = node.left
            else:
                node = node.right
        if data > prev.data:
            prev.left = new_node
        else:
            prev.right = new_node
        
        new_node.parent = prev
        return True
    
    def delete_Tree(self, data):
        """
        트리에서 특정 데이터를 삭제하는 함수.
        Args:
            data: 삭제할 데이터.
        Returns:
            True: 데이터가 성공적으로 삭제됨.
            False: 데이터가 트리에 존재하지 않음.
        """
        node = self.root
        t_node = None

        # 트리에서 삭제할 노드 탐색
        while node:
            if data == node.data:
                t_node = node
                break
            elif data > node.data:
                node = node.right
            else:
                node = node.left

        # 삭제할 노드가 없는 경우
        if t_node is None:
            return False

        # 삭제 케이스 1: 자식이 없는 경우 (Leaf 노드)
        if t_node.left is None and t_node.right is None:
            if t_node == self.root:
                self.root = None
            elif t_node.parent.left == t_node:
                t_node.parent.left = None
            else:
                t_node.parent.right = None

        # 삭제 케이스 2: 자식이 하나인 경우
        elif t_node.left is None or t_node.right is None:
            child = t_node.left if t_node.left else t_node.right
            if t_node == self.root:
                self.root = child
                child.parent = None
            elif t_node.parent.left == t_node:
                t_node.parent.left = child
            else:
                t_node.parent.right = child
            child.parent = t_node.parent

        # 삭제 케이스 3: 자식이 둘인 경우
        else:
            # 오른쪽 서브트리에서 가장 작은 값을 찾음 (후계자)
            successor = t_node.right
            while successor.left:
                successor = successor.left
            # 후계자 값을 현재 노드에 복사
            t_node.data = successor.data
            # 후계자를 삭제 (후계자는 자식이 없거나 하나)
            if successor.parent.left == successor:
                successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right
            if successor.right:
                successor.right.parent = successor.parent

        return True
if __name__ == "__main__":
    tree = Tree()
    