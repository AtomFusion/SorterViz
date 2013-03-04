from interfaces.ISorter import ISorter
from yapsy.IPlugin import IPlugin


class InsertionSorter(ISorter, IPlugin):

    def activate(self):
        print("Insertion sorter activated")
        self.state = []

    def deactivate(self):
        print("Insertion sorter deactivated")

    def prepare(self, list_obj, plotter):
        self.state = list_obj
        self.plotter = plotter
        print self.state

    def sort(self):
        # insertion sort algorithm
        for i in range(1, len(self.state)):
            val = self.state[i]
            j = i - 1
            while (j >= 0) and (self.state[j] > val):
                self.state[j+1] = self.state[j]
                j -= 1
            self.state[j+1] = val
            self.plotter(self.state, self.counter)
            self.counter += 1
