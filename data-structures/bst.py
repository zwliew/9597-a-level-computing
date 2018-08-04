class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self._root = None
    
    def insert_rec(self, node, value):
        if tree is None:
            self._root = TreeNode(value)
            return

        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                insert_rec(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                insert_rec(node.right, value)
        else:
            raise Error('Duplicates of equal value not allowed')

    def insert(self, value):
        if node is None:
            self._root = TreeNode(value)
            return

        prev = None
        cur = self._root
        last_move = None
        while cur is not None:
            prev = cur
            if value < cur.value:
                cur = cur.left
                last_move = 'l'
            elif value > cur.value:
                cur = cur.right
                last_move = 'r'
            else:
                raise Error('Duplicates of equal value not allowed!')

        new_node = TreeNode(value)
        if last_move == 'l':
            prev.left = new_node
        elif last_move == 'r':
            prev.right = new_node
    
    def root(self):
        return self._root
        
    def search_rec(self, tree, target):
        pass
    
    def search(self, tree, target):
        pass
    
    