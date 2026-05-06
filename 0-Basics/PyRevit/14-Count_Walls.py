# -*- coding: utf-8 -*-

__title__ = "Step 14"
__doc__ = """Description:

Count by category (Walls)

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""
from Autodesk.Revit.DB import *

doc = __revit__.ActiveUIDocument.Document

walls = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_Walls)
    .WhereElementIsNotElementType()
    .GetElementCount()
)

print("Wall count:")
print(walls)

'''
Output:

Wall count:
1128
'''