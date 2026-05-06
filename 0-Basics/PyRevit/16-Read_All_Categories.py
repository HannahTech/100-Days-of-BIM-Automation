# -*- coding: utf-8 -*-

__title__ = "Step 16"
__doc__ = """Description:

Automatically reads all categories

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""
from Autodesk.Revit.DB import FilteredElementCollector
from pyrevit import forms

doc = __revit__.ActiveUIDocument.Document

# Collect all placed elements
elements = (
    FilteredElementCollector(doc)
    .WhereElementIsNotElementType()
    .ToElements()
)

# Create category dictionary
categories = {}

for element in elements:

    if element.Category:

        category_name = element.Category.Name

        categories[category_name] = element.Category

# MULTI-SELECTION WINDOW
selected_names = forms.SelectFromList.show(

    sorted(categories.keys()),

    multiselect=True,

    title="Select Categories",

    button_name="Count Categories",

    width=500,

    height=600
)

# If user cancels
if not selected_names:

    print("No category selected.")

else:

    print("Category Counts:")
    print("")

    for selected_name in selected_names:

        selected_category = categories[selected_name]

        count = 0

        for element in elements:

            if element.Category:

                if element.Category.Id == selected_category.Id:

                    count += 1

        print(selected_name + " : " + str(count))

'''
Output:

Category Counts:

Floors : 191
Levels : 18
Rooms : 54
'''