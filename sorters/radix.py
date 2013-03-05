from interfaces.ISorter import ISorter
from yapsy.IPlugin import IPlugin


class RadixSorter(ISorter, IPlugin):

    def activate(self):
        print("Radix sorter activated")
        self.state = []

    def deactivate(self):
        print("Radix sorter deactivated")

    def prepare(self, list_obj, plotter):
        self.state = list_obj
        self.plotter = plotter

    def sort(self):
        # radix sorter
        self.plotter(self.state)
        # for the number length
        length = len(str(len(self.state)))
        self.radixSort(10, length)

    def radixSort(self, n, maxLen):
        for x in range(maxLen):
            bins = [[] for i in range(n)]
            for y in self.state:
                bins[(y / 10 ** x) % n].append(y)
            self.state = []
            for section in bins:
                self.state.extend(section)
                self.plotter(self.state)