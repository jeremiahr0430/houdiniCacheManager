
import hou, subprocess


def run():
    def deleteFiles():
        node = hou.pwd()
        toggle_value = node.evalParm("NewFolder.myToggle")
        file_value = node.evalParm("NewFolder.myFile")

        if toggle_value and file_value:
            # Delete files if toggle is on
            hou.ui.displayMessage(f"Deleting file: {file_value}")
            # Add your file deletion logic here
        else:
            hou.ui.displayMessage("Toggle is off or no file selected.")

    # Function to handle the logic for moving files
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

    # get node (find the path in your node's info panel)
    n = hou.selectedNodes()[0]

    # Delete all parms before regeneration
    node = n
    if node.parm('mainFolder'):
        ptg = node.parmTemplateGroup()
        ptg.remove(ptg.find("mainFolder"))
        node.setParmTemplateGroup(ptg)
        print('parms removed')

    # get existing list of parameters for the specified node
    g = n.parmTemplateGroup()

    # define folders and parameters
    f = hou.FolderParmTemplate(
            'mainFolder', 
            'Main Folder', 
            folder_type=hou.folderType.Simple,parm_templates=[
            ]
        )
    def createParms(mainFolder,folderNumber, folderLabel,loaderPath='path/to/your/file.geo',command="print('empty command')"):
        # Create folder for the found fileCache sop
        folder1 = hou.FolderParmTemplate(
                f'folder{folderNumber}', 
                folderLabel, 
                folder_type=hou.folderType.Simple,parm_templates=[
                ])
        # button to jump to the fileCache sop
        button = hou.ButtonParmTemplate(f"jumpToSop{folderNumber}", "Jump to the fileCache", script_callback=command, script_callback_language=hou.scriptLanguage.Python)
        # toggle for multi selection 
        toggle= hou.ToggleParmTemplate("myToggle", "Select", default_value=False)

        # Create a geo loader parameter template
        geoLoader = hou.StringParmTemplate(f"cacheLocation{folderNumber}", "Cache Location", 1, default_value=(loaderPath,))
        geoLoader.setStringType(hou.stringParmType.FileReference)
        geoLoader.setFileType(hou.fileType.Geometry) 

        # Create a separator parameter template
        separator= hou.SeparatorParmTemplate("mySeparator")
    
        # Add button, loader and toggle to folder for the fileCache sop    
        folder1.addParmTemplate(button)
        folder1.addParmTemplate(geoLoader)
        folder1.addParmTemplate(toggle)
        folder1.addParmTemplate(separator)
        
        # Add fileCache sop folder to main folder. (main folder is created to easily clear all parameters)
        f.addParmTemplate(folder1)

    createParms(f,'1','/obj/geo/fileCache')
    # for i in f:
    #     g.append(i)

    # Function to handle the logic for deleting files
    delete_button= hou.ButtonParmTemplate("deleteButton", "Delete Files")
    # delete_button.setScriptCallback(deleteFiles())
    move_button= hou.ButtonParmTemplate("moveButton", "Move Files")
    # move_button.setScriptCallback(moveFiles())
    f.addParmTemplate(delete_button)
    f.addParmTemplate(move_button)
    g.append(f)

    # apply changes
    n.setParmTemplateGroup(g)  

if __name__ == '__main__':
    run()