from interfaces.ISorter import ISorter
from yapsy.IPlugin import IPlugin
from random import shuffle


class FooSorter(ISorter, IPlugin):

    def activate(self):
        print("Foo sorter activated")

    def deactivate(self):
        print("Foo sorter deactivated")

    def prepare(self, list_obj, plotter):
        self.state = list_obj
        self.plotter = plotter
        print("Prepared object")

    def sort(self):
        # foo sorting algorithm
        # Just keep messing with the data-set
        for i in range(1, 25):
            shuffle(self.state)
            self.plotter(self.state, self.counter)
            self.counter += 1
