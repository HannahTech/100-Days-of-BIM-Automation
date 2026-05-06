# -*- coding: utf-8 -*-

__title__ = "Step 6"
__doc__ = """Description:

Read all sheets

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""

# FilteredElementCollector(doc) = search inside the current Revit document
# .OfClass(ViewSheet) = only find sheets
# .ToElements() = give me the actual elements

from Autodesk.Revit.DB import FilteredElementCollector, ViewSheet

doc = __revit__.ActiveUIDocument.Document

elements = FilteredElementCollector(doc)
print("elements")
print("type::")
print(type(elements))
print("dir:")
print(dir(elements))
print("")

ofClass = elements.OfClass(ViewSheet)
print("ofClass")
print(dir(ofClass))
print("")

sheets = ofClass.ToElements()
print("Sheets:")
print(dir(sheets))
print("")

print("Number of sheets:")
print(len(sheets))
print("")

print("All of sheets:")
for sheet in sheets:
    print(sheet.SheetNumber + " - " + sheet.Name)

'''
Output:

elements
type::
<type 'FilteredElementCollector'>
dir:
['ContainedInDesignOption', 'Dispose', 'Equals', 'Excluding', 'FirstElement', 'FirstElementId', 'GetElementCount', 'GetElementIdIterator', 'GetElementIterator', 'GetEnumerator', 'GetHashCode', 'GetType', 'IntersectWith', 'IsValidObject', 'IsViewValidForElementIteration', 'MemberwiseClone', 'OfCategory', 'OfCategoryId', 'OfClass', 'OwnedByView', 'ReferenceEquals', 'ReleaseUnmanagedResources', 'ToElementIds', 'ToElements', 'ToString', 'UnionWith', 'WhereElementIsCurveDriven', 'WhereElementIsElementType', 'WhereElementIsNotElementType', 'WhereElementIsViewIndependent', 'WherePasses', '__class__', '__contains__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
ofClass
['ContainedInDesignOption', 'Dispose', 'Equals', 'Excluding', 'FirstElement', 'FirstElementId', 'GetElementCount', 'GetElementIdIterator', 'GetElementIterator', 'GetEnumerator', 'GetHashCode', 'GetType', 'IntersectWith', 'IsValidObject', 'IsViewValidForElementIteration', 'MemberwiseClone', 'OfCategory', 'OfCategoryId', 'OfClass', 'OwnedByView', 'ReferenceEquals', 'ReleaseUnmanagedResources', 'ToElementIds', 'ToElements', 'ToString', 'UnionWith', 'WhereElementIsCurveDriven', 'WhereElementIsElementType', 'WhereElementIsNotElementType', 'WhereElementIsViewIndependent', 'WherePasses', '__class__', '__contains__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
Sheets:
['Add', 'AddRange', 'AsReadOnly', 'BinarySearch', 'Capacity', 'Clear', 'Contains', 'ConvertAll', 'CopyTo', 'Count', 'EnsureCapacity', 'Enumerator', 'Equals', 'Exists', 'Find', 'FindAll', 'FindIndex', 'FindLast', 'FindLastIndex', 'ForEach', 'GetEnumerator', 'GetHashCode', 'GetRange', 'GetType', 'IndexOf', 'Insert', 'InsertRange', 'IsReadOnly', 'IsSynchronized', 'Item', 'LastIndexOf', 'MemberwiseClone', 'ReferenceEquals', 'Remove', 'RemoveAll', 'RemoveAt', 'RemoveRange', 'Reverse', 'Slice', 'Sort', 'SyncRoot', 'ToArray', 'ToString', 'TrimExcess', 'TrueForAll', '__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__format__', '__getattribute__', '__getitem__', '__getslice__', '__hash__', '__init__', '__iter__', '__len__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__']
Number of sheets:
1
All of sheets:
A100 - Unnamed
'''
