import hou
from houdiniCacheManager.cachemanage import findMoveCache
#Used in jumpToSop and MoveCacheFiles.

    # get the button's parm name and extract the digit at the end. This can be used as an index
    # to find its folder's label which is the path of the targeted sop.
def extractDigits(input_string):
    digits = [char for char in input_string if char.isdigit()]
    return ''.join(digits)
def findParmNum(parm):
    parmName = parm.name()
    parmNum = extractDigits(parmName)
    return parmNum
def findSopPathByNum(parmNum):
#Get the Dictionary
    fmc = findMoveCache.FindMoveCache()
    filePathDict,filecacheNames, pathList, sopLocations= fmc.filePathDict() 
    # find the folder's label 
    sopPath = sopLocations[int(parmNum)]
    print(f'the sop path is {sopPath}')
    return sopPath
def findFilePathBySopName(sopName):
    fmc = findMoveCache.FindMoveCache()
    filePathDict,filecacheNames, pathList, sopLocations= fmc.filePathDict() 
    # find the folder's label 
    filePath = filePathDict[sopName] 
    return filePath