class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def append(self, data):
        if self.data:
            if self.data >= data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.append(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.append(data)
        else:
            self.data = data

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()

    def height(self):
        # Find the height of a given tree. If there is no data, return 0. If the tree is only one node, return 1.
        if self.data is None:
            return 0
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return 1 + self.right.height()
        if self.right is None:
            return 1 + self.left.height()
        return 1 + max(self.left.height(), self.right.height())

    def find_val(self, val):
        # Determine if the given value can be found in the binary tree. If yes, return True, otherwise return False.
        if self.data == val:
            return True
        if self.left is not None:
            if self.left.find_val(val):
                return True
        if self.right is not None:
            if self.right.find_val(val):
                return True
        return False


    def find_layer(self, layer):
        # Write a function that returns a list of all of the values on a given layer. You may use a helper method.
        return self.find_layer_helper(layer, 1)
    
    def find_layer_helper(self, layer, current_layer):
        if self.data is None:
            return []
        if current_layer == layer:
            return [self.data]
        left = []
        right = []
        if self.left is not None:
            left = self.left.find_layer_helper(layer, current_layer + 1)
        if self.right is not None:
            right = self.right.find_layer_helper(layer, current_layer + 1)
        return left + right