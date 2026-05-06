__title__ = "Step 4"
__doc__ = """Description:

Get Document

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""
uiapp = __revit__
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document

# The actual Revit project database
# Read or change: project info, sheets, views, walls, rooms, families, parameters

print("Document:")
print(doc)

'''
Output:
Document:
<Autodesk.Revit.DB.Document object at 0x000000000000027D [Autodesk.Revit.DB.Document]>
'''