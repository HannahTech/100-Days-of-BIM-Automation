# Import Revit API and pyRevit tools
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
from pyrevit import script, forms

# 1. Initialize output window (pop-up window, pyRevit specific)

output = script.get_output()

# 2. Collect all Rooms in the active document
# __revit__: This is a "magic" variable PyRevit provides. It represents the UIApplication
# .ActiveUIDocument: This looks at the specific window/file you are currently clicking on.
# .Document: This moves from the "User Interface" (UI) level to the "Database" level. You need the Document level to read or write data.

doc = __revit__.ActiveUIDocument.Document

# FilteredElementCollector(doc): You are telling Revit, "I want to search inside this specific document (doc)."
# OfCategory(BuiltInCategory.OST_Rooms): This is like a filter. Revit has millions of things in its database (lines, points, hidden settings). This tells the API to ignore everything except Rooms.
# WhereElementIsNotElementType(): This is a crucial "pro tip." In Revit, there is a difference between a Type (the blueprint for a room) and an Instance (the actual room placed in your floor plan). This line ensures you only get the rooms physically placed in the model.

rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()

# 3. Create a data list for the table
# This is where we extract specific parameters: Name, Number, Level, Area, Department

data = []
for r in rooms:
    # Ensure the room is actually placed (Area > 0)
    if r.Area > 0:
        row = [
            r.LookupParameter("Name").AsString(),
            r.LookupParameter("Number").AsString(),
            r.Level.Name,
            r.LookupParameter("Area").AsValueString(), # Uses project units
            r.LookupParameter("Department").AsString() or "N/A"
        ]
        data.append(row)

# 4. Export to Excel (CSV) via pyRevit
# This will prompt you to save the file immediately

if data:
    header = ["Name", "Number", "Level", "Area", "Department"]
    save_path = forms.save_file(file_ext='csv', default_name='RoomDataExport.csv')
    
    if save_path:
        import csv
        with open(save_path, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        forms.alert("Export Complete!", title="Success")
