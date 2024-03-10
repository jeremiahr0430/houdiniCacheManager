import hou  
import houdiniCacheManager.hdaModular.cacheSopUtils as csu
def jumpToSop(kwargs):
    # get the button's parm name and extract the digit at the end. This can be used as an index
    # to find its folder's label which is the path of the targeted sop.

    parmNum = csu.findParmNum(kwargs)
    sopPath = csu.findSopPathByNum(parmNum)
    sop = hou.node(sopPath)
    # select the found sop node and switch network editor's view to that sop's location.
    sop.setSelected(True)
    hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor).setCurrentNode(sop)
