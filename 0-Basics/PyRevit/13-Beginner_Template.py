# -*- coding: utf-8 -*-

__title__ = "Step 13"
__doc__ = """Description:

Full beginner template

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""
from Autodesk.Revit.DB import FilteredElementCollector, ViewSheet

# 1. Revit application
uiapp = __revit__

# 2. Current document in Revit UI
uidoc = uiapp.ActiveUIDocument

# 3. Actual Revit model/database
doc = uidoc.Document

# 4. Print project info
print("Connected to Revit")
print("Project title: " + doc.Title)
print("Project path: " + doc.PathName)

# 5. Collect sheets
sheets = FilteredElementCollector(doc).OfClass(ViewSheet).ToElements()

print("Sheets found: " + str(len(sheets)))

for sheet in sheets:
    print(sheet.SheetNumber + " - " + sheet.Name)

'''
Output:

Connected to Revit

Project title: Architectural

Project path: C:\FakePath\Architectural.rvt

Sheets found: 55

C101 - Site Plan
SD100 - Parking Deck Floor Plan
SD101 - First Floor Plan
SD102 - Second Floor Plan
SD103 - Third Floor Plan
SD104 - Fourth Floor Plan
SD105 - Fifth Floor Plan
SD106 - Roof Plan
A401 - Typical Public Restroom
A902 - Stair Towers - Cutaway Views
A901 - Perspective From Above
A601 - Door Schedule
G000 - Cover
A903 - 3D Views
K101 - Café Kitchen
A100 - Parking Deck Floor Plan
A101 - First Floor Plan
A102 - Second Floor Plan
A103 - Third Floor Plan
A104 - Fourth Floor Plan
A105 - Fifth Floor Plan
A107 - Roof Plan
A501 - Details
A405 - Wall Sections
A406 - Wall Sections
A302 - Building Sections
A303 - Building Sections
A304 - Building Sections
A305 - Building Sections
A307 - Building Sections
A301 - Building Sections
A306 - Building Sections
A201 - Building Elevations
A202 - Building Elevations
A108 - First Floor Ceiling Plan
A109 - Second Floor Ceiling Plan
A110 - Third Floor Ceiling Plan
A111 - Fourth Floor Ceiling Plan
A112 - Fifth Floor Ceiling Plan
G100 - Parking Deck Life Safety Plan
G101 - First Floor Life Safety Plan
G103 - Third Floor Life Safety Plan
G104 - Fourth Floor Life Safety Plan
G105 - Fifth Floor Life Safety Plan
G106 - Roof Plan Life Safety Plan
G102 - Second Floor Life Safety Plan
A402 - Enlarged Live/Work Cores
A403 - Enlarged Live/Work Cores
A106 - Green Roof
A502 - Partition Types
A404 - Residential Lobby
A602 - Schedules
A200 - Existing Conditions Elevations
A904 - Solar Study
G001 - Learn about this project
'''