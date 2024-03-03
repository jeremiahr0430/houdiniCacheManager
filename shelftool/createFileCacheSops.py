# This is for quickly creating filecache and give options to cache all created filecaches. 
# This is not useful in practice. It's just for testing findCache.py
import string,hou
chrList = list(string.ascii_lowercase)
chrList = chrList[:10]
print(chrList)
obj = hou.node('/obj')

fileCacheNodes = []
for n,i in enumerate(chrList):
    i = obj.createNode("geo",f"geo_{i}") 
    fileCacheNodes.append(i)
    fileCacheNodes[n] = i.createNode('filecache',f"filecache_{i}") 
    fileCacheNodes[n].parm('basedir').set("$HIP/geo/$OS")
    fileCacheNodes[n].parm('loadfromdisk').set(1)
result = hou.ui.displayMessage("cache all files?", buttons=("Yes", "No"))
if result == 0:
    for cacheFile in fileCacheNodes:
        cacheFile.parm('execute').pressButton()