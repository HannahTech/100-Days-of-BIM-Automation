# -*- coding: utf-8 -*-

__title__ = "Step 9"
__doc__ = """Description:

Active View

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""
doc = __revit__.ActiveUIDocument.Document

active_view = doc.ActiveView

print("Active view:")
print(active_view.Name)

'''
Output:

Active view:
L1
'''