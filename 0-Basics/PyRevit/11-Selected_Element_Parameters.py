# -*- coding: utf-8 -*-

__title__ = "Step 11"
__doc__ = """Description:

Read parameters of selected element

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

selected_ids = uidoc.Selection.GetElementIds()

for element_id in selected_ids:
    element = doc.GetElement(element_id)
    print("Element:")
    print(element.Name)

    print("Parameters:")
    for param in element.Parameters:
        print(param.Definition.Name)

'''
Output:

Element:
Interior - 7 1/4" Partition (1 hr)

Parameters:
Image
Category
Category
Cross-Section
IFC Predefined Type
Export to IFC As
Export to IFC
IfcGUID
Design Option
Design Option
Base Extension Distance
Top Extension Distance
Volume
Area
Phase Demolished
Phase Created
Comments
Length
Family and Type
Family
Type
Family Name
Type Name
Type Id
Related to Mass
Structural
Mark
Location Line
Structural Usage
Base is Attached
Top is Attached
Top Offset
Base Offset
Base Constraint
Unconnected Height
Top Constraint
Room Bounding

Element:
36" Diameter
Parameters:
Image
Category
Category
IFC Predefined Type
Export to IFC As
Export to IFC
IfcGUID
Design Option
Design Option
Volume
Area
Phase Demolished
Phase Created
Comments
Host Id
Level
Family and Type
Family
Type
Family Name
Type Name
Type Id
Moves With Nearby Elements
Host
Elevation from Level
Level
Mark

Element:
36" x 84"
Parameters:
Image
Category
Category
IFC Predefined Type
Export to IFC As
Export to IFC
IfcGUID
Design Option
Design Option
Volume
Area
Phase Demolished
Phase Created
Comments
Host Id
Level
Family and Type
Family
Type
Family Name
Type Name
Type Id
Head Height
Sill Height
Level
Rough Width
Rough Height
Frame Material
Frame Type
Finish
Mark
Swing Angle
Masonry Frame
Masonry Inset
Inset Calculate
Dry Wall Frame
MF Opening Height
MF Opening Width
Material
Under Cut
Hardware
Frame Finish
Jamb
Head
Sill

'''