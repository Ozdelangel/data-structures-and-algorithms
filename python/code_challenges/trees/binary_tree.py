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


        def traverse_4(root):
            max = root.value

            if root is None:
                return max
            left = traverse_4(root.left)
            right = traverse_4(root.right)
            if left > right:
                return left
            if left < right:
                return right
            if  root is None:

                   return

            else:
                return traverse_4(self.root, max)






# class BinarySearchTree(BinaryTree):
#     pass


