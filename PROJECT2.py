class LinkedBST:
    def __init__(self):
        self.root = None
        self.size = 0

    def height(self):
        return self.get_height(self.root)

    def get_height(self, node):
        if node is None:
            return -1
        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def isBalanced(self):
        return self.check_balance(self.root)

    def check_balance(self, node):
        if node is None:
            return True
        else:
            left_height = self.get_height(node.left)
            right_height = self.get_height(node.right)
            if abs(left_height - right_height) > 1:
                return False
            else:
                return self.check_balance(node.left) and self.check_balance(node.right) and (self.height() <= 2 * math.log2(self.size + 1))
