from yapsy.PluginManager import PluginManager
from random import shuffle
from functools import partial
import pylab
import os
import shutil


def main():
    # Get a manager
    plugin_manager = PluginManager()

    # Give it a folder to look in, sorters
    plugin_manager.setPluginPlaces(['sorters'])

    # Load 'em
    plugin_manager.collectPlugins()

    # Activate 'em and run 'em
    for plugin in plugin_manager.getAllPlugins():
        if plugin.name != "Insertion Sort":
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
        a = range(100)
        shuffle(a)
        plugin.plugin_object.prepare(a)
        plugin.plugin_object.sort(partial(plot, folder_path))
        create_movie(folder_name, plugin.plugin_object.counter)


def plot(folder_path, state, imgidx):
    x = range(len(state))
    pylab.plot(x, state, 'k.', markersize=6)
    pylab.savefig(folder_path + "/img" + '%04d' % imgidx + ".png")
    pylab.clf()  # figure clear


def create_movie(m_name, count, fps=120):
    import os, re

    if (count / fps / 60) > 1:
        fps = count / 60

    safe_m_name = re.escape(m_name)
    os.system('rm ' + safe_m_name + '.mp4')

    os.system('ffmpeg -r ' + str(fps) + ' -b 1800 -i ' + safe_m_name + '/img%04d.png ' + safe_m_name + '.mp4')
    os.system('rm -r ' + safe_m_name)

if __name__ == '__main__':
    main()