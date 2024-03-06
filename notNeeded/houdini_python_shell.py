>>> 
>>> mulparm = node.parm('folder0')
>>> print(mulparm)
<hou.Parm folder0 in /obj/multiParmTest1>
>>> mulparm.eval()
3
>>> mulparm.set(5)
>>> button = node.parm('button1')
>>> button.setLabel('new')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Parm' object has no attribute 'setLabel'
>>> print(button)
<hou.Parm button1 in /obj/multiParmTest1>
>>> button.setLabel('new')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Parm' object has no attribute 'setLabel'
>>> geoParm = node.parm('geo1')
>>> print(geoParm)
<hou.Parm geo1 in /obj/multiParmTest1>
>>> geoParm.setLabel('aa')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Parm' object has no attribute 'setLabel'
>>> parmTemp = geoParm.parmTemplate()
>>> print(parmTemp)
<hou.StringParmTemplate name='geo1' label='geo1' length=1 naming_scheme=Base1 string_type=FileReference file_type=G
eometry default_value=('',) tags={ "script_callback_language" : "python", }>
>>> 
>>> parmTemp.setLabel('new')
>>> node.setParmT
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'ObjNode' object has no attribute 'setParmT'
>>> node.setParmTemplateGroup(node.parmTemplateGroup())
>>> node.setParmTemplateGroup(parmTemp)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "E:\Program Files/Side Effects Software/Houdini 19.5.493/houdini/python3.9libs\hou.py", line 15802, in setPa
rmTemplateGroup
    return _hou.Node_setParmTemplateGroup(self, parm_template_group, rename_conflicting_parms)
TypeError: in method 'Node_setParmTemplateGroup', argument 2 of type 'HOM_ParmTemplateGroup &'
>>> parmTemp
<hou.StringParmTemplate name='geo1' label='new' length=1 naming_scheme=Base1 string_type=FileReference file_type=Ge
ometry default_value=('',) tags={ "script_callback_language" : "python", }>
>>> node.setParmTemplateGroup(parmTemp)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "E:\Program Files/Side Effects Software/Houdini 19.5.493/houdini/python3.9libs\hou.py", line 15802, in setPa
rmTemplateGroup
    return _hou.Node_setParmTemplateGroup(self, parm_template_group, rename_conflicting_parms)
TypeError: in method 'Node_setParmTemplateGroup', argument 2 of type 'HOM_ParmTemplateGroup &'
>>> 
>>> 
>>> 
>>> parmN = node.parm('parmNumber')
>>> print(parmN)
<hou.Parm parmNumber in /obj/multiParmTest1>
>>> parmNTemp = parmN.parmTemplate()
>>> print(parmNTemp)
<hou.IntParmTemplate name='parmNumber' label='Parm Number' length=1 naming_scheme=Base1 look=Regular default_value=
(0,) tags={ "script_callback_language" : "python", }>
>>> parmNTemp.setLabel('The Number')
>>> newParmTempGroup = hou.ParmTemplateGroup()
>>> newParmTempGroup.append(parmNTemp)
>>> node.setParmTemplateGroup(parmNTemp)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "E:\Program Files/Side Effects Software/Houdini 19.5.493/houdini/python3.9libs\hou.py", line 15802, in setPa
rmTemplateGroup
    return _hou.Node_setParmTemplateGroup(self, parm_template_group, rename_conflicting_parms)
TypeError: in method 'Node_setParmTemplateGroup', argument 2 of type 'HOM_ParmTemplateGroup &'
>>> 
>>> 
>>> Label of parmNumber on /obj/multiParmTest1 changed to 'New Label'.hou.node('/obj/multiParmTest1')
hou.node('/obj/multiParmTest1')
<hou.ObjNode of type jerem::dev::multiParmTest::1.0 at /obj/multiParmTest1>
>>> 
>>> 
>>> 
>>> 
>>> Label of parmNumber on /obj/multiParmTest1 changed to 'New Label'.
<hou.Parm parmNumber in /obj/multiParmTest1>
Label of parmNumber on /obj/multiParmTest1 changed to 'New Label'.