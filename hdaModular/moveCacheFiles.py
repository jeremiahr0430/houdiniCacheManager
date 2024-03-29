import hou
import subprocess
from houdiniCacheManager.hdaModular import cacheSopUtils 
from houdiniCacheManager.cachemanage import findMoveCache

def rmCacheFiles(kwargs):
    # Get the current node (assumes this is called within an HDA callback)
    node = kwargs['node']

    # Get all 'selectCacheToggle' toggles
    toggle_parms = [parm for parm in node.parms() if parm.name().startswith('selectCacheToggle')]
    cacheLocations = [parm for parm in node.parms() if parm.name().startswith('cacheLocation')]

    # Create a list of file paths to be removed
    files_to_remove = []
    # def findFilePathBySopName(sopName):
    #     fmc = findMoveCache.FindMoveCache()
    #     filePathDict,filecacheNames, pathList, sopLocations= fmc.filePathDict() 
    #     # find the folder's label 
    #     filePath = filePathDict[sopName] 
    #     return filePath
    for toggle_parm in toggle_parms:
        # check if toggle is on
        if toggle_parm.eval():
            # Assuming the associated cache file has the same name as the toggle
            print(f'toggle parm name is {toggle_parm.name()}')
            parmNum = cacheSopUtils.findParmNum(toggle_parm)
            parmName = cacheLocations[int(parmNum)].name()
            print(f'parm name is {parmName}')
            cache_file_path = node.parm(parmName).eval()  #cacheSopUtils.findFilePathBySopName(parmName) 
            print(f'the found file path is {cache_file_path}')
            files_to_remove.append(cache_file_path)

    # Check if there are files to remove
    if files_to_remove:
        # Create a single 'rm' command to remove all files
        rm_command = f"rm {' '.join(files_to_remove)}"

        # Execute the 'rm' command using subprocess
        subprocess.run(rm_command, shell=True)
        print("Cache files deleted.")
    else:
        print("No cache files selected for deletion.")

def moveFiles():
    node = hou.pwd()
    file_value = node.evalParm("NewFolder.myFile")

    if file_value:
        # Prompt the user to select a folder
        destination_folder = hou.ui.selectFile(title="Select Destination Folder", file_type=hou.fileType.Directory)

        if destination_folder:
            # Move the file using a command line command
            command = f"move {file_value} {destination_folder}"
            subprocess.run(command, shell=True)
            hou.ui.displayMessage(f"File moved to: {destination_folder}")
        else:
            hou.ui.displayMessage("No destination folder selected.")
    else:
        hou.ui.displayMessage("No file selected.")