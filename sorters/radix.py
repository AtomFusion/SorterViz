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
        nat_len = len(self.state)
        for x in range(maxLen):
            bins = [[] for i in range(n)]
            for y in self.state:
                bins[(y / 10 ** x) % n].append(y)

                sz = nat_len - len(list(self.flatten(bins)))
                if sz > 0:
                    self.plotter(list(self.flatten(bins)) + ([0] * sz))
                else:
                    self.plotter(list(self.flatten(bins)))
            self.state = []
            for idx, section in enumerate(bins):
                self.state.extend(section)
                if self.state == list(self.flatten(bins[idx:])):
                    sz = nat_len - len(self.state)
                    if sz > 0:
                        self.plotter(self.state + [0] * sz)
                    else:
                        self.plotter(self.state)
                else:
                    self.plotter(self.state + list(self.flatten(bins[idx:])))

    def flatten(self, *args):
        for x in args:
            if hasattr(x, '__iter__'):
                for y in self.flatten(*x):
                    yield y
            else:
                yield x