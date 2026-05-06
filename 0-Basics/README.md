# Revit Python & Dynamo Beginner Automation Series

A beginner-friendly learning repository for understanding **Revit API**, **pyRevit**, **Python**, and **Dynamo** through small practical automation examples.

This repository is designed for architects, BIM coordinators, computational designers, and Revit users who want to transition from visual scripting into real Revit automation.

---

# Goals of This Repository

This project teaches:

* How Revit API works internally
* The relationship between:

  * UIApplication
  * UIDocument
  * Document
  * Elements
  * Parameters
* How to collect and filter Revit elements
* How to explore Revit data programmatically
* How Dynamo concepts translate into Python/Revit API logic
* How to build reusable pyRevit tools

---

# Technologies Used

* Python
* pyRevit
* Revit API
* Dynamo
* IronPython

---

# Repository Structure

```text
/Revit-Python-Beginner-Series

    /pyRevit
        01_Import_Basic_Classes
        02_Connect_To_Revit
        03_Get_UIDocument
        04_Get_Document
        05_Project_Name_And_Path
        06_Read_All_Sheets
        07_Read_All_Views
        08_ViewTypes
        09_Active_View
        10_Selected_Elements
        11_Selected_Element_Parameters
        12_Read_One_Parameter
        13_Beginner_Template
        14_Count_Walls
        15_Count_Selected_Category
        16_Read_All_Categories
        17_Count_All_Categories

    /Dynamo
        05_Project_Name_And_Path.dyn
        06_Read_All_Sheets.dyn
        07_Read_All_Views.dyn
        09_Active_View.dyn
        10_Selected_Elements.dyn
        11_Selected_Element_Parameters.dyn
        12_Read_One_Parameter.dyn
        14_Count_Walls.dyn
        15_Count_Selected_Category.dyn
        16_Read_All_Categories.dyn
        17_Count_All_Categories.dyn
```

---

# pyRevit Lessons

## 01 — Import Basic Revit API Classes

Learn the purpose of importing classes from:

* Autodesk.Revit.DB
* Autodesk.Revit.UI

---

## 02 — Connect to Revit

Understanding:

* `__revit__`
* UIApplication

---

## 03 — Get UIDocument

Understanding the UI-side document.

---

## 04 — Get Document

Understanding the Revit database document.

---

## 05 — Print Project Name and Path

Read:

* Project title
* File path

Dynamo version included.

---

## 06 — Read All Sheets

Use:

* `FilteredElementCollector`
* `ViewSheet`

Dynamo version included.

---

## 07 — Read All Views

Collect and print all project views.

Dynamo version included.

---

## 08 — Read All Views and ViewTypes

Explore:

* View names
* View types

Dynamo version included.

---

## 09 — Active View

Read the currently active Revit view.

Dynamo version included.

---

## 10 — Read Selected Elements

Access currently selected elements in Revit.

Dynamo version included.

---

## 11 — Read Parameters of Selected Element

Explore all parameters of a selected Revit element.

Dynamo version included.

---

## 12 — Read One Parameter Value

Read a specific parameter by name.

Dynamo version included.

---

## 13 — Full Beginner Template

A reusable pyRevit script template for future tools.

---

## 14 — Count by Category (Walls)

Count all wall elements in the project.

Dynamo version included.

---

## 15 — Count by Category (User Selection)

Use pyRevit UI forms for category selection.

Dynamo version included.

---

## 16 — Automatically Read All Categories

Automatically discover all categories in the project.

Dynamo version included.

---

## 17 — Count Categories in Entire Project

Generate category statistics for the entire Revit model.

Dynamo version included.

---

# Learning Philosophy

This repository focuses on understanding Revit from the inside out:

```text
Revit
→ UIApplication
→ UIDocument
→ Document
→ Elements
→ Parameters
```

The goal is not only writing scripts, but understanding how Revit stores and manages BIM data internally.

---

# Why pyRevit Instead of Only Dynamo?

Dynamo is excellent for visual scripting and learning concepts.

However, pyRevit and Revit API provide:

* More scalability
* More flexibility
* Better reusable tools
* Faster automation workflows
* Professional BIM automation pipelines

This repository shows both approaches and explains how they connect.

---

# Recommended Learning Order

1. pyRevit basics
2. Revit API concepts
3. Element collection
4. Parameters
5. Categories
6. Filtering
7. Dynamo comparisons
8. Real automation workflows

---

# Requirements

* Autodesk Revit
* pyRevit
* Dynamo
* Basic Python knowledge helpful but not required

---

# Author

Created by Hengameh Khajehpour

Focused on:

* BIM Automation
* Revit API
* Computational Design
* Python for AEC
* Digital Design Technology
