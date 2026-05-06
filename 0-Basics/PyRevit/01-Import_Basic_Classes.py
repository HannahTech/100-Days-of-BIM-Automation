# -*- coding: utf-8 -*-

__title__ = "Step 1"
# __context__ = "selection" Only active when something selected
__doc__ = """Description:

Import basic Revit API classes

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""
from Autodesk.Revit.DB import * # model/database side (when working with real project data: sheets, walls, rooms, parameters)
from Autodesk.Revit.UI import * # user interface side (when working with selection, messages, active view, Revit window)

print("Import basic Revit API classes Completed!!!")

'''
Output:

Import basic Revit API classes Completed!!!
'''