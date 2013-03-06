from interfaces.ISorter import ISorter
from yapsy.IPlugin import IPlugin
from random import shuffle


class FooSorter(ISorter, IPlugin):

    def activate(self):
        print("Foo sorter activated")

    def deactivate(self):
        print("Foo sorter deactivated")

    # The list to be sorted and the plotting function
    # are given when prepare is called.
    def prepare(self, list_obj, plotter):
        self.state = list_obj
        self.plotter = plotter
        print("Prepared object")

    # This is the sort function. It isn't necessarily
    # required to return a value, but it would be wise
    # to call the plotter function provided when
    # prepare() was called. This plots the state
    # of the sort at a given frame.
    def sort(self):
        # foo sorting algorithm
        # Just keep messing with the data-set
        for i in range(1, 25):
            shuffle(self.state)
            # This is calling the plotting function at
            # a time when data has been changed.
            # (A good time to do so)
            self.plotter(self.state)
