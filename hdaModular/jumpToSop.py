import hou  
from houdiniCacheManager.cachemanage import findMoveCache
def findSopName(kwargs):
    def extractDigits(input_string):
        digits = [char for char in input_string if char.isdigit()]
        return ''.join(digits)
    # get the button's parm name and extract the digit at the end. This can be used as an index
    # to find its folder's label which is the path of the targeted sop.
    parmName = kwargs['parm'].name()
    parmNum = extractDigits(parmName)

    #Get the Dictionary
    fmc = findMoveCache.FindMoveCache()
    filePathDict,filecacheNames, pathList, sopLocations= fmc.filePathDict() 
    # find the folder's label 
    sopPath = sopLocations[int(parmNum)]
    print(f'the sop path is {sopPath}')
    sop = hou.node(sopPath)
    sop.setSelected(True)
    hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor).setCurrentNode(sop)
