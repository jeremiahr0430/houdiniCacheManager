import hou
# checkbox to select all.
def setAllToggles(kwargs):
    parms = kwargs['node'].parms()
    controlToggle = kwargs['parm']
    controlState = controlToggle.eval()
    for p in parms:

        if "selectCacheToggle" in p.name():
            p.set(controlState)