from interfaces.ISorter import ISorter
from yapsy.IPlugin import IPlugin


class ShellSorter(ISorter, IPlugin):

    def activate(self):
        print("Shell sorter activated")
        self.state = []

    def deactivate(self):
        print("Shell sorter deactivated")

    def prepare(self, list_obj):
        self.state = list_obj
        print self.state

    def sort(self, plotter):
        # shell sort algorithm
        gap = len(self.state) // 2
        # loop over the gaps
        while gap > 0:
            # do the insertion sort
            for i in range(gap, len(self.state)):
                val = self.state[i]
                j = i
                while j >= gap and self.state[j - gap] > val:
                    self.state[j] = self.state[j - gap]
                    plotter(self.state, self.counter)
                    self.counter += 1
                    j -= gap
                    #plotter(self.state, self.counter)
                    #self.counter += 1
                self.state[j] = val
                plotter(self.state, self.counter)
                self.counter += 1
            gap //= 2

