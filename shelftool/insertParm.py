
import hou, subprocess

from houdiniCacheManager.cachemanage import findMoveCache
from importlib import reload
reload(findMoveCache)

# This is for giving using options between to create a new cache manager node and not to   
# This is not needed any more as parameters will be created on an HDA
def createNull():
    def set_unique_name(base_name):
        # Assuming 'node' is the Houdini node's parent
        counter = 1
        new_name = f"{base_name}_{counter}"
        while hou.node(f'/obj/{new_name}'):
            # If a node with the same name exists, increment the counter
            counter += 1
            new_name = f"{base_name}_{counter}"
        return new_name

    unique_name = set_unique_name("Cache_Manager")
    # Create a null node
        # and name it as Cache_Manager
    nullNode= hou.node("/obj").createNode('null',unique_name)
    # and hide existing parms
    for parm in nullNode.parms():
        parm.hide(True)
    return nullNode

def createParms(node):

    def insertParms(node,mainFolder,folderNumber, folderLabel,loaderPath='path/to/your/file.geo'):
        node.setSelected(True)
        # Create folder for the found fileCache sop
        folder1 = hou.FolderParmTemplate(
                f'folder{folderNumber}', 
                folderLabel, 
                folder_type=hou.folderType.Simple,parm_templates=[
                ])
        # button to jump to the fileCache sop
        command =  'hou.phm().jumpToSop.jumpToSop(kwargs)'
        button = hou.ButtonParmTemplate(f"jumpToSop{folderNumber}", "Jump to the fileCache", script_callback= command, script_callback_language=hou.scriptLanguage.Python)

        # Create a geo loader parameter template
        geoLoader = hou.StringParmTemplate(f"cacheLocation{folderNumber}", "Cache Location", 1, default_value=(loaderPath,))
        geoLoader.setStringType(hou.stringParmType.FileReference)
        geoLoader.setFileType(hou.fileType.Geometry) 

        # toggle for multi selection 
        toggle= hou.ToggleParmTemplate(f"selectCacheToggle{folderNumber}", "Select", default_value=False)

        # # Create a separator parameter template
        # separator= hou.SeparatorParmTemplate("mySeparator")
    
        # Add button, loader and toggle to folder for the fileCache sop    
        folder1.addParmTemplate(button)
        folder1.addParmTemplate(geoLoader)
        folder1.addParmTemplate(toggle)
        # folder1.addParmTemplate(separator)
        
        # Add fileCache sop folder to main folder. (main folder is created to easily clear all parameters)
        mainFolder.addParmTemplate(folder1)

    # Delete all parms before regeneration
    if node.parm('mainFolder'):
        ptg = node.parmTemplateGroup()
        ptg.remove(ptg.find("mainFolder"))
        node.setParmTemplateGroup(ptg)
        print('parms removed')

    # get existing list of parameters for the specified node
    group = node.parmTemplateGroup()

    # define folders and parameters
    mainFolder = hou.FolderParmTemplate(
            'mainFolder', 
            'Main Folder', 
            folder_type=hou.folderType.Simple,parm_templates=[
            ]
        )

    # Testing to create multi parms (range(5) will be replaced by a list of fileCache sop found)

    fmc = findMoveCache.FindMoveCache()
    #Get the Dictionary
    filePathDict,filecacheNames, pathList, sopLocations= fmc.filePathDict() 
    for i,sopL in enumerate(sopLocations):
        insertParms(node,mainFolder,i,sopL,pathList[i])
        print(f'the sop {filecacheNames[i]} \nIts path is {pathList[i]}')

    # for i in f:
    #     g.append(i)

    # Create a separator parameter template
    separator= hou.SeparatorParmTemplate("mySeparator")
    # select all toggle
    controlToggalCommand = 'hou.phm().setAllToggles.setAllToggles(kwargs)'
    selectAllToggle = hou.ToggleParmTemplate("selectAllCache", "Select All Cache", default_value=False,script_callback=controlToggalCommand, script_callback_language=hou.scriptLanguage.Python)
    # Function to handle the logic for deleting files
    deleteCommand = 'hou.phm().moveCacheFiles.rmCacheFiles(kwargs)' 
    delete_button= hou.ButtonParmTemplate("deleteButton", "Delete Files", script_callback = deleteCommand, script_callback_language=hou.scriptLanguage.Python)
    # delete_button.setScriptCallback(deleteFiles())
    move_button= hou.ButtonParmTemplate("moveButton", "Move Files")
    # move_button.setScriptCallback(moveFiles())
    mainFolder.addParmTemplate(separator)
    mainFolder.addParmTemplate(selectAllToggle)
    mainFolder.addParmTemplate(delete_button)
    mainFolder.addParmTemplate(move_button)
    group.append(mainFolder)

    # apply changes
    node.setParmTemplateGroup(group)  

def run(node):
    # result = hou.ui.displayMessage("create a new node?", buttons=("Yes", "No"))
    # if result ==0:
    #     node = createNull()
    #     createParms(node)
    # else:
    #     node = hou.selectedNodes()[0]
    #     createParms(node)
    createParms(node)


if __name__ == '__main__':
    run()