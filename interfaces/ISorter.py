"""
Role
====

Defines the basic interface for the sorter. These are inherited
by the *core* class of a sorter. This is the class that will be
notified when a sort-frame has been recorded.

API
===
"""


class ISorter(object):
    """
    The most simple interface inherited when dealing with a sorter

    Inherits from IPlugin
    """

    counter = 0

    def sort(self, plotter):
        pass

    def prepare(self, list_obj):
        """
        Allow the sorter to prepare by giving it the starting set.
        Must return the set to be analyzed.
        """
        pass

    # Flags to send to the caller
    # Always unique
    class CONTINUE(object):
        pass
    class COMPLETE(object):
        pass
