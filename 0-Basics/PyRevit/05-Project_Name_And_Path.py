# -*- coding: utf-8 -*-

__title__ = "Step 5"
__doc__ = """Description:

Print project name and path

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""

# __revit__ → Revit application
# ActiveUIDocument → current open Revit file in UI
# Document → actual model database
# doc.Title → project/file title

uiapp = __revit__
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document

project_name = doc.Title
project_path = doc.PathName

print("Project name is:")
print(project_name)


print("Project Path is:")
print(project_path)

'''
Output:
Project name is:
sample project
Project Path is:
C:\FakePath\sample project.rvt
'''