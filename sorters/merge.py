from interfaces.ISorter import ISorter
from yapsy.IPlugin import IPlugin


class MergeSorter(ISorter, IPlugin):

    def activate(self):
        print("Merge sorter activated")
        self.state = []

    def deactivate(self):
        print("Merge sorter deactivated")

    def prepare(self, list_obj, plotter):
        self.state = list_obj
        self.plotter = plotter
        print self.state

    def sort(self):
        # Non-recursive (natural) merge-sort
        left = self.count_sorted(self.state)
        while left < len(self.state):
            right = self.count_sorted(self.state, left)
            self.merge_sublists(self.state, left, right)
            self.plotter(self.state, self.counter)
            self.counter += 1
            left += right

    def count_sorted(self, items, start=0):
        for x in range(start + 1, len(items)):
            if items[x - 1] > items[x]:
                return x - start
        return len(items) - start

    def reinsert(self, items, val, start, end):
        for x in range(start, end - 1):
            if items[x + 1] > val:
                items[x] = val
                return
            else:
                items[x] = items[x + 1]
        items[end - 1] = val


    def merge_sublists(self, items, left, right):
        for x in range(0, left):
            if items[x] > items[left]:
                val = items[x]
                items[x] = items[left]
                self.reinsert(items, val, left, left + right)


