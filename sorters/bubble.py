from interfaces.ISorter import ISorter
from yapsy.IPlugin import IPlugin


class BubbleSorter(ISorter, IPlugin):

    def activate(self):
        print("Bubble sorter activated")
        self.state = []

    def deactivate(self):
        print("Bubble sorter deactivated")

    def prepare(self, list_obj, plotter):
        self.state = list_obj
        self.plotter = plotter
        print self.state

    def sort(self):
        # bubble sort algorithm
        swapped = True
        while swapped:  # until there's no swapping
            swapped = False
            for i in range(len(self.state)-1):
                if self.state[i] > self.state[i+1]:
                    self.plotter(self.state)
                    self.state[i+1], self.state[i] = self.state[i], self.state[i+1] # swap
                    swapped = True