# 📐 interval_mapper — Universal Interval-to-Label Mapping Tool

A general-purpose tool that maps numeric values to labeled intervals.  
Works with any domain: engineering ranges, scoring bands, rating systems, categories, and more.

---

## 🚀 Features

- Maps any numeric column to category intervals  
- Supports optional grouping (e.g., different interval sets per region/type)  
- CSV → CSV transformation  
- UTF-8 friendly (Excel compatible)  
- Fully deterministic and easy to automate  

---

## 📁 Required Input Files

### **1️⃣ intervals.csv**

Must contain:

| Min | Max | Label | (optional) Group |
|-----|-----|--------|------------------|

Example:

```
Min,Max,Label
0,10,Low
11,20,Medium
21,30,High
```
---
### **2️⃣ points.csv**

Must contain:

| Value | (optional) Group |
|-------|-------------------|

Example:
```
Value
3
17
22
30
```
---

## ▶️ Usage

From project root:

```bash
python src/file_tools/interval_mapper/interval_mapper.py \
    intervals.csv \
    points.csv \
    output.csv \
    --group GroupColumnName \
    --value Value
```
### Minimal version (no grouping)
```
python src/file_tools/interval_mapper/interval_mapper.py \
    examples/interval_mapper/sample_intervals.csv \
    examples/interval_mapper/sample_input.csv \
    examples/interval_mapper/sample_output.csv
```
---
## 📌 Example (included dataset)
### intervals.csv
```
Min,Max,Label
0,10,Low
11,20,Medium
21,30,Zone2
31,40,High
```
### input.csv
```
Value
3
17
22
7
23
30
```
### Output (sample_output.csv)
```
Value,MatchedLabel
3,Low
17,Medium
22,Zone2
7,Low
23,Zone2
30,High
```
---
## 📦 Requirements
```bash
pandas
```
---
## 📝 Notes
- If `--group` is provided, both files must contain that column
- Intervals must not overlap unless used carefully
- Values outside all intervals receive `MatchedLabel = ""`

---

### 📬 Contact
Feel free to open an issue or suggest improvements.

---
