from interfaces.ISorter import ISorter
from yapsy.IPlugin import IPlugin


class HeapSorter(ISorter, IPlugin):

    def activate(self):
        print("Heap sorter activated")
        self.state = []

    def deactivate(self):
        print("Heap sorter deactivated")

    def prepare(self, list_obj, plotter):
        self.state = list_obj
        self.plotter = plotter

    def sort(self):
        # selection sorter
        self.plotter(self.state)
        self.HeapSort(self.state)

    ## {{{ http://code.activestate.com/recipes/577086/ (r1)
    def HeapSort(self, A):
        def heapify(A):
            start = (len(A) - 2) / 2
            while start >= 0:
                siftDown(A, start, len(A) - 1)
                start -= 1

        def siftDown(A, start, end):
            root = start
            while root * 2 + 1 <= end:
                child = root * 2 + 1
                if child + 1 <= end and A[child] < A[child + 1]:
                    child += 1
                if child <= end and A[root] < A[child]:
                    A[root], A[child] = A[child], A[root]
                    root = child
                else:
                    return

        heapify(A)
        end = len(A) - 1
        self.plotter(self.state)
        while end > 0:
            A[end], A[0] = A[0], A[end]
            siftDown(A, 0, end - 1)
            end -= 1
            self.plotter(self.state)
