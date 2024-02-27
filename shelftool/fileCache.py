# Using Generate Node  class to create file cache.
# There are method that is not needed anymore due to houdini update. 

import hou
from cachemanage import generateNode  # findMoveCache class is called

reload(generateNode)

import os


def run():
    #Define the node
    gNode = generateNode.GenerateNode('filecache')
    gNode.getUserInput()
    filecache = gNode.generateNode()




