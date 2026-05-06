# -*- coding: utf-8 -*-

__title__ = "Step 12"
__doc__ = """Description:

Read one parameter value

-------------------------------
Author: Hengameh Khajehpour
-------------------------------
"""

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

selected_ids = uidoc.Selection.GetElementIds()

for element_id in selected_ids:
    element = doc.GetElement(element_id)
    print(dir(element))
    
    param = element.LookupParameter("Comments")

    if param:
        print("Comments:")
        print(param.AsString())
    else:
        print("This element has no Comments parameter.")

'''
Output:

['AddCoping', 'ArePhasesModifiable', 'AssemblyInstanceId', 'CanBeHidden', 'CanBeLocked', 'CanDeleteSubelement', 'CanFlipFacing', 'CanFlipHand', 'CanFlipWorkPlane', 'CanHaveTypeAssigned', 'CanRotate', 'CanSplit', 'Category', 'ChangeTypeId', 'CreatedPhaseId', 'DeleteEntity', 'DeleteSubelement', 'DeleteSubelements', 'DemolishedPhaseId', 'DesignOption', 'Dispose', 'Document', 'EvaluateAllParameterValues', 'EvaluateParameterValues', 'ExtensionUtility', 'FacingFlipped', 'FacingOrientation', 'FlipFromToRoom', 'GetChangeTypeAny', 'GetChangeTypeElementAddition', 'GetChangeTypeElementDeletion', 'GetChangeTypeGeometry', 'GetChangeTypeParameter', 'GetCopingIds', 'GetDependentElements', 'GetEntity', 'GetEntitySchemaGuids', 'GetExternalFileReference', 'GetExternalResourceReference', 'GetExternalResourceReferenceExpanded', 'GetExternalResourceReferences', 'GetExternalResourceReferencesExpanded', 'GetFamilyPointPlacementReferences', 'GetGeneratingElementIds', 'GetGeometryObjectFromReference', 'GetMaterialArea', 'GetMaterialIds', 'GetMaterialVolume', 'GetMonitoredLinkElementIds', 'GetMonitoredLocalElementIds', 'GetOrderedParameters', 'GetOriginalGeometry', 'GetParameter', 'GetParameterFormatOptions', 'GetParameters', 'GetPhaseStatus', 'GetReferenceByName', 'GetReferenceName', 'GetReferenceType', 'GetReferences', 'GetSpatialElementCalculationPoint', 'GetSpatialElementFromToCalculationPoints', 'GetSubComponentIds', 'GetSubelements', 'GetSweptProfile', 'GetTotalTransform', 'GetTransform', 'GetTypeId', 'GetValidTypes', 'GroupId', 'HandFlipped', 'HandOrientation', 'HasModifiedGeometry', 'HasPhases', 'HasSpatialElementCalculationPoint', 'HasSpatialElementFromToCalculationPoints', 'HasSweptProfile', 'Host', 'HostFace', 'HostParameter', 'Id', 'Invisible', 'IsCreatedPhaseOrderValid', 'IsDemolishedPhaseOrderValid', 'IsExternalFileReference', 'IsHidden', 'IsModifiable', 'IsMonitoringLinkElement', 'IsMonitoringLocalElement', 'IsPhaseCreatedValid', 'IsPhaseDemolishedValid', 'IsSlantedColumn', 'IsTransient', 'IsValidObject', 'IsValidType', 'IsWorkPlaneFlipped', 'LevelId', 'Location', 'LookupParameter', 'MEPModel', 'Mirrored', 'Name', 'OwnerViewId', 'Parameters', 'ParametersMap', 'Pinned', 'RefersToExternalResourceReference', 'RefersToExternalResourceReferences', 'ReleaseUnmanagedResources', 'RemoveCoping', 'SetCopingIds', 'SetEntity', 'Split', 'StructuralMaterialId', 'StructuralMaterialType', 'StructuralType', 'StructuralUsage', 'SuperComponent', 'Symbol', 'UniqueId', 'VersionGuid', 'ViewSpecific', 'WorksetId', '__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'flipFacing', 'flipHand', 'getBoundingBox', 'rotate', 'setElementType']

Comments:
None
'''