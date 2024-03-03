
#import hou


import hou

# get node (find the path in your node's info panel)
n = hou.selectedNodes()[0]

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
    folder1 = hou.FolderParmTemplate(
            f'folder{folderNumber}', 
            folderLabel, 
            folder_type=hou.folderType.Simple,parm_templates=[
            ])
    button = hou.ButtonParmTemplate(f"jumpToSop{folderNumber}", "Jump to the fileCache", script_callback=command, script_callback_language=hou.scriptLanguage.Python)

    # Create a geo loader parameter template

    geoLoader = hou.StringParmTemplate(f"cacheLocation{folderNumber}", "Cache Location", 1, default_value=(loaderPath,))
    geoLoader.setStringType(hou.stringParmType.FileReference)
    geoLoader.setFileType(hou.fileType.Geometry) 
        
        
    folder1.addParmTemplate(button)
    folder1.addParmTemplate(geoLoader)
    f.addParmTemplate(folder1)
createParms(f,'1','/obj/geo/fileCache')
# for each folder and parameter defined, add to the list


# for i in f:
#     g.append(i)
g.append(f)
# apply changes
n.setParmTemplateGroup(g)  