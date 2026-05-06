# -*- coding: utf-8 -*-

__title__ = "Step 17"
__doc__ = """Description:

Count categories in entire project

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""
from Autodesk.Revit.DB import *

'''
FilteredElementCollector(doc) : All project elements
OfCategory(...) : Filtered category
WhereElementIsNotElementType() : Only placed elements
GetElementCount() : Count result
'''

doc = __revit__.ActiveUIDocument.Document

elements = (
    FilteredElementCollector(doc)
    .WhereElementIsNotElementType()
    .ToElements()
)

category_counts = {}

for element in elements:
    if element.Category:
        category_name = element.Category.Name
        if category_name not in category_counts:
            category_counts[category_name] = 0

        category_counts[category_name] += 1

for category in sorted(category_counts):
    print(category + " : " + str(category_counts[category]))
    
'''
Output:

<Area Boundary> : 628
<Insulation Batting Lines> : 5
<Path of Travel Lines> : 95
<Room Separation> : 38
<Sketch> : 3210
<Stair/Ramp Sketch: Boundary> : 22
<Stair/Ramp Sketch: Landing Center> : 3
<Stair/Ramp Sketch: Riser> : 6
<Stair/Ramp Sketch: Run> : 3
<Stair/Ramp Sketch: Stair Path> : 3
Adaptive Points : 2
Area Schemes : 2
Area Tags : 101
Areas : 101
Array : 6
Automatic Sketch Dimensions : 1023
Balusters : 237
Building Type Settings : 33
Callout Heads : 1
Cameras : 36
Casework : 177
Ceilings : 68
Color Fill Legends : 22
Color Fill Schema : 9
Columns : 118
Constraints : 280
Curtain Panels : 681
Curtain Wall Grids : 235
Curtain Wall Mullions : 1425
Cut Profile : 5
Design Option Sets : 2
Design Options : 6
Detail Groups : 61
Detail Items : 231
Dimensions : 696
Divisions : 10
Door Tags : 251
Doors : 142
Electrical Demand Factor Definitions : 9
Electrical Load Classification Parameter Element : 90
Electrical Load Classifications : 15
Elevation Marks : 36
Elevations : 15
Entourage : 10
Floors : 191
Food Service Equipment : 26
Furniture : 168
Generic Annotations : 245
Generic Models : 278
Grid Heads : 2
Grids : 28
Guide Grid : 1
HVAC Load Schedules : 50
HVAC Zones : 1
Handrails : 121
Hardscape : 10
Internal Origin : 1
Keynote Tags : 3
Landings : 17
Legend Components : 328
Level Heads : 2
Levels : 18
Lighting Fixtures : 447
Lines : 1184
Material Assets : 146
Material Tags : 65
Materials : 220
Model Groups : 49
Multi-Category Tags : 36
Multistory Stairs : 3
Panel Schedule Templates - Branch Panel : 3
Panel Schedule Templates - Data Panel : 1
Panel Schedule Templates - Switchboard : 1
Parking : 20
Parking Tags : 20
Parts : 28
Path of Travel Tags : 93
Phases : 3
Pipe Segments : 11
Plan Region : 40
Planting : 117
Planting Tags : 54
Plumbing Fixtures : 149
Primary Contours : 2
Project Base Point : 1
Project Information : 1
Property Line Segment Tags : 8
Property Line Segments : 8
Property Lines : 1
RVT Links : 8
Railing Rail Path Extension Lines : 1195
Railings : 131
Ramps : 2
Raster Images : 17
Rectangular Straight Wall Opening : 9
Reference Planes : 1037
Revision : 3
Revision Cloud Tags : 1
Revision Clouds : 2
Revision Numbering Sequences : 2
Roofs : 20
Room Tags : 361
Rooms : 54
Runs : 43
Schedule Graphics : 68
Schedules : 92
Scope Boxes : 3
Section Boxes : 36
Section Marks : 8
Shaft Openings : 9
Shared Site : 2
Sheets : 55
Site : 75
Slab Edges : 68
Space Type Settings : 125
Specialty Equipment : 288
Spot Elevation Symbols : 2
Spot Elevations : 4
Spot Slopes : 194
Stair Paths : 360
Stairs : 27
Structural Load Cases : 8
Sun Path : 438
Supports : 2779
Survey Point : 1
Text Notes : 335
Title Blocks : 55
Top Rails : 91
Vertical Circulation : 2
View Reference : 1
View Titles : 1
Viewports : 121
Views : 326
Wall Sweeps : 258
Wall Tags : 1229
Walls : 1128
Window Tags : 102
Windows : 106
Work Plane Grid : 201
'''