import hou  
# from houdiniCacheManager.cachemanage import findMoveCache
def findSopName(kwargs):
    def extractDigits(input_string):
        digits = [char for char in input_string if char.isdigit()]
        return ''.join(digits)
    parm = kwargs['parm']
    parmName = parm.name()
    node = kwargs['node']
    parmNum = extractDigits(parmName)
    allParms = node.parms()
    folderNames = []
    for p in allParms:
        if 'folderSet' in p.parmTemplate().type():
            pNum = extractDigits(p.name())
            if pNum == parmNum:
                folderNames.append(p.name()) 
    print(f'parm name is {parmName}, parm number is {parmNum}, node is {node}')
    # print(f'parm name is {parm.name()}, folder is {folderName}')
    # fmc = findMoveCache.FindMoveCache()
    #Get the Dictionary
    # filePathDict,filecacheNames, pathList, sopLocations= fmc.filePathDict() 
    # find the folder's name (parm name is always 'folder#')

    # for filecache in filecacheNames:
    #     if parmNum in filecache
    # sop = hou.node(folderLabel)
    # sop.setSelected(True)
    # hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor).setCurrentNode(sop)