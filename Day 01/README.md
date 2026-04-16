<p align="center">
  <video src="https://github.com/user-attachments/assets/d171ea61-25b9-432d-93f9-1b589a4c0d4c" autoplay loop muted playsinline>
  </video>
</p>

---
# 📦 Room Data Exporter (pyRevit Tool)

## 📋 Overview
The **Room Data Exporter** is a Python-based automation tool designed for Autodesk Revit. It bridges the gap between BIM geometry and data analysis by extracting room-specific parameters directly into a standardized CSV format.

This tool is part of the **Snowdon Automation Suite**, a 100-day initiative to replace high-volume manual BIM tasks with scalable code.

---

## 🚀 Business Value
* **Efficiency:** Eliminates the manual process of creating Revit schedules and exporting them through multiple menus.
* **Accuracy:** Uses the `FilteredElementCollector` to ensure only placed, physical rooms are quantified, reducing "ghost" data.
* **Interoperability:** Produces a clean CSV output ready for use in **Excel**, **Power BI**, or **SQL databases** for project management and facility audits.

---

## 🛠️ Technical Workflow
The script utilizes the **Revit API** and **pyRevit** framework to perform the following:
1. **Document Access:** Accesses the `ActiveUIDocument.Document` database.
2. **Filtering:** Filters for `BuiltInCategory.OST_Rooms` while excluding `ElementType` to target instances only.
3. **Validation:** Checks for `Area > 0` to ensure rooms are correctly placed within boundaries.
4. **Data Extraction:** Retrieves parameters including `Name`, `Number`, `Level`, `Area`, and `Department`.
5. **Output:** Invokes the `pyrevit.forms` API to provide a native Windows "Save File" dialogue.

---

## 📂 Installation & Usage
1. Ensure **pyRevit** is installed.
2. Place the `.pushbutton` folder within your `.extension` directory.
3. Click the **Export Rooms** button on the **Snowdon Tab**.
4. Select your save location and open the resulting `.csv` in Excel.

---

## 💻 Code Snippet (Logic Preview)
```python
# The core logic behind the collector
rooms = FilteredElementCollector(doc) \
        .OfCategory(BuiltInCategory.OST_Rooms) \
        .WhereElementIsNotElementType() \
        .ToElements()
```

## 👤 Author
## Hannah (Hengameh) Khajehpour
Digital Design Technologist | BIM Automation Specialist

[LinkedIn Profile](https://www.linkedin.com/in/hannahai/) | 📂 [GitHub Portfolio](https://github.com/HannahTech)

"Automating the AEC industry, one script at a time."
