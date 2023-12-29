class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


tree = BinaryTreeNode(10)
tree.insert_right(20)
tree.insert_left(30)


if __name__ == "__main__":
    print("Hello world")
