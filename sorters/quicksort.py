from interfaces.ISorter import ISorter
from yapsy.IPlugin import IPlugin
from random import randrange


class QuicksortSorter(ISorter, IPlugin):

    def activate(self):
        print("Quicksort sorter activated")
        self.state = []

    def deactivate(self):
        print("Quicksort sorter deactivated")

    def prepare(self, list_obj, plotter):
        self.state = list_obj
        self.plotter = plotter

        self.stacks = []

    def sort(self):
        # quicksort sorting algorithm, non-recursive, stateful
        # uses nested lists to give a fully representative state
        # at all sort-ticks
        self.stacks.append(self.state)
        sorted = False
        while not sorted:
            sorts = []
            inner_stack = []
            for stack in self.stacks:
                # We want to see if this one is already "sorted", i.e. alone
                if len(stack) == 1:
                    sorts.append(True)
                    inner_stack.append(stack)
                    continue
                else:
                    sorts.append(False)
                self.plotter([item for sublist in self.stacks for item in sublist])
                pivot = stack.pop(randrange(len(stack)))
                lesser = [l for l in stack if l < pivot]
                greater = [l for l in stack if l > pivot]
                if len(lesser) > 0: inner_stack.append(lesser)
                inner_stack.append([pivot])
                if len(greater) > 0: inner_stack.append(greater)

            self.stacks = inner_stack
            if all(sorts): # If all the values are True
                sorted = True
