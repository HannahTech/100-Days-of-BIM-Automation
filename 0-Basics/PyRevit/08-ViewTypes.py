# -*- coding: utf-8 -*-

__title__ = "Step 8"
__doc__ = """Description:

Read all views and ViewTypes

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""

from Autodesk.Revit.DB import FilteredElementCollector, View

doc = __revit__.ActiveUIDocument.Document

views = (
    FilteredElementCollector(doc)
    .OfClass(View)
    .ToElements()
    )

print("Number of views:")
print(len(views))
view_types = set()

print("All of views:")
for view in views:
    if not view.IsTemplate:
        view_types.add(str(view.ViewType))
        print(str(view.ViewType) + " - " + view.Name)
        
print("ViewTypes in this file:")

for vt in sorted(view_types):
    print(vt)

'''
Output:

Number of views:
32

All of views:

ProjectBrowser - Project View
FloorPlan - Level 0
CeilingPlan - Level 0
FloorPlan - Level 1
CeilingPlan - Level 1
Elevation - North
Elevation - East
Elevation - South
Elevation - West
FloorPlan - Site
ThreeD - {3D}
SystemBrowser - System Browser
Schedule - Keynote Legend
Legend - Door Legend
Legend - Key Plan
Schedule - View List
DrawingSheet - Unnamed
Schedule - Room Schedule
Schedule - <Revision Schedule>

ViewTypes in this file:

CeilingPlan
DrawingSheet
Elevation
FloorPlan
Legend
ProjectBrowser
Schedule
SystemBrowser
ThreeD
'''