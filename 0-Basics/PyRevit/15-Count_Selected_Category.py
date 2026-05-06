# -*- coding: utf-8 -*-

__title__ = "Step 15"
__doc__ = """Description:

Count by category (Select one from the list)

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""
from Autodesk.Revit.DB import *
from pyrevit import forms

#  (Select one from the list)
# doc = __revit__.ActiveUIDocument.Document

# categories = {

#     "Walls": BuiltInCategory.OST_Walls,
#     "Doors": BuiltInCategory.OST_Doors,
#     "Windows": BuiltInCategory.OST_Windows,
#     "Rooms": BuiltInCategory.OST_Rooms,
#     "Sheets": BuiltInCategory.OST_Sheets,
#     "Views": BuiltInCategory.OST_Views,
#     "Floors": BuiltInCategory.OST_Floors,
#     "Columns": BuiltInCategory.OST_Columns
# }

# # Show selection window
# selected_name = forms.SelectFromList.show(

#     sorted(categories.keys()),
#     title="Select Category",
#     button_name="Count Elements"
# )

# if not selected_name:
#     print("No category selected.")

# else:
#     selected_category = categories[selected_name]

#     count = (
#         FilteredElementCollector(doc)
#         .OfCategory(selected_category)
#         .WhereElementIsNotElementType()
#         .GetElementCount()
#     )

#     print(selected_name + " count:")
#     print(count)


#  (Select Multi from the list)

doc = __revit__.ActiveUIDocument.Document

# Category dictionary
categories = {

    "Walls": BuiltInCategory.OST_Walls,
    "Doors": BuiltInCategory.OST_Doors,
    "Windows": BuiltInCategory.OST_Windows,
    "Rooms": BuiltInCategory.OST_Rooms,
    "Sheets": BuiltInCategory.OST_Sheets,
    "Views": BuiltInCategory.OST_Views,
    "Floors": BuiltInCategory.OST_Floors,
    "Columns": BuiltInCategory.OST_Columns
}

# Multi-selection popup
selected_names = forms.SelectFromList.show(

    sorted(categories.keys()),
    multiselect=True,
    title="Select Categories",
    button_name="Count Elements"
)

# If user cancels
if not selected_names:
    print("No categories selected.")

else:

    print("Selected Categories:")
    print("")

    # Loop through selected categories
    for name in selected_names:

        category = categories[name]

        count = (
            FilteredElementCollector(doc)
            .OfCategory(category)
            .WhereElementIsNotElementType()
            .GetElementCount()
        )

        print(name + " : " + str(count))

'''
Output:

Selected Categories:

Floors : 191
Rooms : 54
'''