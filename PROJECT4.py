class LinkedBST:
    
    def successor(self, item):
        return self._successor_helper(self.root, item)

    def _successor_helper(self, node, item):
        if node is None:
            return None

        if node.item == item:
            if node.right is not None:
                return self._leftmost(node.right)
            else:
                return None

        if item < node.item:
            left = self._successor_helper(node.left, item)
            if left is not None:
                return left
            else:
                return node
        else:
            return self._successor_helper(node.right, item)

    def predecessor(self, item):
        return self._predecessor_helper(self.root, item)

    def _predecessor_helper(self, node, item):
        if node is None:
            return None

        if node.item == item:
            if node.left is not None:
                return self._rightmost(node.left)
            else:
                return None

        if item < node.item:
            return self._predecessor_helper(node.left, item)
        else:
            right = self._predecessor_helper(node.right, item)
            if right is not None:
                return right
            else:
                return node

    def _leftmost(self, node):
        if node.left is None:
            return node
        else:
            return self._leftmost(node.left)

    def _rightmost(self, node):
        if node.right is None:
            return node
        else:
            return self._rightmost(node.right)