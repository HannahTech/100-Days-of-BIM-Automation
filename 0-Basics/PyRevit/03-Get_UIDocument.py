__title__ = "Step 3"
__doc__ = """Description:

Get UIDocument

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""

uiapp = __revit__
uidoc = uiapp.ActiveUIDocument

# The document as opened in the Revit interface
# Knows active view, selected elements, current user selection

print("UIDocument:")
print(uidoc)

'''
Output:
UIDocument:
<Autodesk.Revit.UI.UIDocument object at 0x000000000000027C [Autodesk.Revit.UI.UIDocument]>
'''