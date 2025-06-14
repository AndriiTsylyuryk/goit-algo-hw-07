class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        else:
            node.right = self._insert_rec(node.right, key)
        return node





def find_max(node):
    current = node
    while current and current.right:
        current = current.right
    return current.key if current else None


def find_min(node):
    current = node
    while current and current.left:
        current = current.left
    return current.key if current else None


def sum_of_tree(node):
    if node is None:
        return 0
    return node.key + sum_of_tree(node.left) + sum_of_tree(node.right)



bst = BinarySearchTree()
for value in [15, 10, 20, 8, 12, 17, 25]:
    bst.insert(value)

print("Максимум:", find_max(bst.root))  
print("Мінімум:", find_min(bst.root))   
print("Сума:", sum_of_tree(bst.root))   
