from yapsy.PluginManager import PluginManager
from random import shuffle
from functools import partial
import pylab
import os
import sys
import shutil


def main():
    # Get a manager
    plugin_manager = PluginManager()

    # Give it a folder to look in, sorters
    plugin_manager.setPluginPlaces(['sorters'])

    # Load 'em
    plugin_manager.collectPlugins()

    # TODO: Add flag for how many numbers it should sort

    # Activate 'em and run 'em
    for plugin in plugin_manager.getAllPlugins():
        if 'all' not in sys.argv:
            if plugin.name not in sys.argv:
                continue
        plugin_manager.activatePluginByName(plugin.name)
        folder_name = plugin.name
        temp, _ = os.path.split(os.path.abspath(__file__))
        folder_path = os.path.join(temp, folder_name)
        try:
            os.makedirs(folder_path)
        except:
            shutil.rmtree(folder_name)  # Remove the folder, we're going to remake it
            os.makedirs(folder_path)
        a = range(1000)
        shuffle(a)
        plot = Plotter()
        plugin.plugin_object.prepare(a, partial(plot.plot, folder_path))
        plugin.plugin_object.sort()
        create_movie(folder_name, plugin.plugin_object.counter)


class Plotter(object):

    counter = 0

    def plot(self, folder_path, state):

        x = range(len(state))
        pylab.plot(x, state, 'k.', markersize=6)

        pylab.savefig(folder_path + "/img" + '%04d' % self.counter + ".png")
        self.counter += 1
        pylab.clf()  # figure clear

# TODO: Add flag to change fps
def create_movie(m_name, count, fps=30):
    import os, re

    if (count / fps / 60) > 0.5:
        fps = count / 30

    safe_m_name = re.escape(m_name)
    os.system('rm ' + safe_m_name + '.mp4')

    os.system('ffmpeg -r ' + str(fps) + ' -b 1800 -i ' + safe_m_name + '/img%04d.png ' + safe_m_name + '.mp4')
    os.system('rm -r ' + safe_m_name)

if __name__ == '__main__':
    main()