# -*- coding: utf-8 -*-

from pyrevit import revit, forms, script
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction
import csv

doc = revit.doc
output = script.get_output()

csv_path = forms.pick_file(file_ext='csv')
if not csv_path:
    forms.alert("No CSV selected.")
    script.exit()

# Read CSV by Room Name
room_rules = {}

with open(csv_path, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["RoomName"].strip().lower()
        room_rules[name] = {
            "Department": row["Department"].strip(),
            "Occupancy": row["Occupancy"].strip()
        }

rooms = FilteredElementCollector(doc) \
    .OfCategory(BuiltInCategory.OST_Rooms) \
    .WhereElementIsNotElementType() \
    .ToElements()

updated = 0
skipped = []

t = Transaction(doc, "Auto Fill Room Department and Occupancy")
t.Start()

for room in rooms:
    name_param = room.LookupParameter("Name")
    dept_param = room.LookupParameter("Department")
    occ_param = room.LookupParameter("Occupancy")

    if not name_param:
        continue

    room_name = name_param.AsString().strip()
    key = room_name.lower()

    if key not in room_rules:
        skipped.append(room_name)
        continue

    dept_value = room_rules[key]["Department"]
    occ_value = room_rules[key]["Occupancy"]

    current_dept = dept_param.AsString() if dept_param else ""
    current_occ = occ_param.AsString() if occ_param else ""

    # Only fill if empty
    if dept_param and not dept_param.IsReadOnly:
        if not current_dept or current_dept.strip() == "":
            dept_param.Set(dept_value)
            updated += 1

    if occ_param and not occ_param.IsReadOnly:
        if not current_occ or current_occ.strip() == "":
            occ_param.Set(occ_value)
            updated += 1

t.Commit()

output.print_md("# Room Auto-Fill Complete")
output.print_md("Updated parameter fields: **{}**".format(updated))

if skipped:
    output.print_md("## Room names not found in CSV")
    for name in sorted(set(skipped)):
        output.print_md("- {}".format(name))

forms.alert("Done. Updated {} empty fields.".format(updated))