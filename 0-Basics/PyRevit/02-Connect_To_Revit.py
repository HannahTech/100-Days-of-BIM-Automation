__title__ = "Step 2"
__doc__ = """Description:

Connect to Revit and Get UIApplication

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""

# UIApplication = Revit software window
# UIDocument = the open project as user sees it
# Document = the actual project database
# Element = one object inside the project
# Parameter = data attached to that object


# This is the Revit UI application object.
# Represents the active Revit user interface session and gives access to the active document.

uiapp = __revit__

print("Connected to Revit, UIApplication:")
print(uiapp)

# __revit__ = the current Revit application session

'''
Output:

Connected to Revit, UIApplication:
<Autodesk.Revit.UI.UIApplication object at 0x000000000000027B [Autodesk.Revit.UI.UIApplication]>
'''