from interfaces.ISorter import ISorter
from yapsy.IPlugin import IPlugin
from random import randrange


class BinaryTreeSorter(ISorter, IPlugin):

    def activate(self):
        print("Bubble sorter activated")
        self.state = []

    def deactivate(self):
        print("Bubble sorter deactivated")

    def prepare(self, list_obj, plotter):
        self.state = list_obj
        self.plotter = plotter

    def sort(self):
        # bubble sort algorithm
        btree = BinTree()
        size = range(len(self.state))
        root = btree.add_node(self.state.pop(randrange(len(self.state))))

        for val in self.state:
            btree.insert(root, val)
            self.plotter(btree.as_list(root))


class BNode:
    left, right, data = None, None, 0

    def __init__(self, data):
        # init members
        self.left = None
        self.right = None
        self.data = data


class BinTree():

    def add_node(self, data):
        # create a new node
        return BNode(data)

    def insert(self, root, data):
        # insert data
        if root is None:
            # if there isn't data there,
            # add it and return it
            return self.add_node(data)

        else:
            # enter it into the tree
            if data <= root.data:
                # if the data is less than the root node
                # go into the left tree
                root.left = self.insert(root.left, data)
            else:
                # go into the right tree
                root.right = self.insert(root.right, data)
            return root

    def lookup(self, root, target):
        # look for the value
        if root is None:
            return 0
        else:
            # it was found
            if target == root.data:
                return True
            # if it wasn't found
            else:
                if target < root.data:
                    # left
                    return self.lookup(root.left, target)
                else:
                    # right
                    return self.lookup(root.right, target)

    def size(self, root):
        if root is None:
            return 0
        else:
            return self.size(root.left)

    def as_list(self, root):
        if root is None:
            return []
        else:
            result = self.as_list(root.left) + [root.data] + self.as_list(root.right)
            return result