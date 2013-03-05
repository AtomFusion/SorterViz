from interfaces.ISorter import ISorter
from yapsy.IPlugin import IPlugin


class SelectionSorter(ISorter, IPlugin):

    def activate(self):
        print("Selection sorter activated")
        self.state = []

    def deactivate(self):
        print("Selection sorter deactivated")

    def prepare(self, list_obj, plotter):
        self.state = list_obj
        self.plotter = plotter

    def sort(self):
        # selection sorter
        self.plotter(self.state)
        for i in range(len(self.state)):
            idx = i
            num = self.state[i]
            for j in range(i+1, len(self.state)):
                if num > self.state[j]:
                    idx = j
                    num = self.state[j]

            self.state[i], self.state[idx] = self.state[idx], self.state[i]

            self.plotter(self.state)
