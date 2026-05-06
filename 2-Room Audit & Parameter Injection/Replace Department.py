# -*- coding: utf-8 -*-
from pyrevit import revit, DB, forms

doc = revit.doc

old_name = forms.ask_for_string(
    default="Residential",
    prompt="Enter the department name you want to replace:"
)

new_name = forms.ask_for_string(
    default="Condominium",
    prompt="Enter the new department name:"
)

if not old_name or not new_name:
    forms.alert("Cancelled.")
    raise SystemExit

rooms = DB.FilteredElementCollector(doc)\
    .OfCategory(DB.BuiltInCategory.OST_Rooms)\
    .WhereElementIsNotElementType()\
    .ToElements()

changed = 0

with revit.Transaction("Replace Room Department"):
    for room in rooms:
        dept_param = room.LookupParameter("Department")

        if dept_param and not dept_param.IsReadOnly:
            current_value = dept_param.AsString()

            if current_value == old_name:
                dept_param.Set(new_name)
                changed += 1

forms.alert(
    "Done!\n\nChanged {} room(s) from '{}' to '{}'.".format(
        changed, old_name, new_name
    )
)