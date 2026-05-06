# -*- coding: utf-8 -*-

__title__ = "Step 10"
__doc__ = """Description:

Read selected elements

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

selected_ids = uidoc.Selection.GetElementIds()

# uidoc.Selection = UI selection
# doc.GetElement(id) = get real model element from its ID

print("Selected element count:")
print(len(selected_ids))
print(selected_ids)

for element_id in selected_ids:
    element = doc.GetElement(element_id)
    print(element.Name)

'''
Output:
Selected element count:
3

List[ElementId]([<Autodesk.Revit.DB.ElementId object at 0x000000000000027B [737373]>, <Autodesk.Revit.DB.ElementId object at 0x000000000000027C [738713]>, <Autodesk.Revit.DB.ElementId object at 0x000000000000027D [1247720]>])
Interior - 7 1/4" Partition (1 hr)
36" Diameter
36" x 84"
'''