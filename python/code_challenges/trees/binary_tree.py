from code_challenges.trees.node import Node


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    def pre_order(self):
        tree = []

        def traverse(root):
            if root is None:
                return

            tree.append(root.value)
            traverse(root.left)
            traverse(root.right)
        traverse(self.root)
        return tree

    def in_order(self):
        tree_2 = []

        def traverse_2(root):
            if root is None:
                return
            traverse_2(root.left)
            tree_2.append(root.value)
            traverse_2(root.right)
        traverse_2(self.root)
        return tree_2

    def post_order(self):
        tree_3 = []

        def traverse_3(root):
            if root is None:
                return
            traverse_3(root.left)
            traverse_3(root.right)
            tree_3.append(root.value)
        traverse_3(self.root)
        return tree_3
    def find_max(self):


        def traverse_4(root, max):


            if root is None:
                return max
            elif max < root.value:
                max = root.value
            max = traverse_4(root.left, max)
            return traverse_4(root.right, max)

        if self.root is None:
            return
        else:
            return traverse_4(self.root, self.root.value)
# I got help from my mentor on this






class BinarySearchTree(BinaryTree):
    def add(self, value=None):
        if self.root is None:
            self.root = Node(value)
            return
        def traverse(root, value):
            if root.value > value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    traverse(root.left, value)
            elif root.value < value:
                if root.right is None:
                    root.right = Node(value)
                else:
                    traverse(root.right, value)
        traverse(self.root, value)

    def contains(self,value):
        if self.root is None:
            return False

        def traverse(root, value):
            if root.value == value:
                return True
            elif value < root.value:
                if root.left:
                    return traverse(root.left, value)
            elif value > root.value:
                if root.right:
                    return traverse(root.right, value)
            return False
        return traverse(self.root, value)


