# -*- coding: utf-8 -*-

__title__ = "Step 7"
__doc__ = """Description:

Read all views

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""

from Autodesk.Revit.DB import FilteredElementCollector, View

doc = __revit__.ActiveUIDocument.Document

views = FilteredElementCollector(doc).OfClass(View).ToElements()

print("Number of views:")
print(len(views))
print("")

print("All of views:")
for view in views:
    if not view.IsTemplate:
        print(view.Name)

'''
Output:

Number of views:
32
All of views:
Project View
Level 0
Level 0
Level 1
Level 1
North
East
South
West
Site
{3D}
System Browser
Keynote Legend
Door Legend
Key Plan
View List
Unnamed
Room Schedule
<Revision Schedule>
'''