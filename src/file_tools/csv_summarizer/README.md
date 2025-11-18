# 📄 csv_summarizer — General-Purpose CSV Grouping & Summary Tool

This tool provides a **simple, universal data summarization utility** built on top of Python and Pandas.

It helps you:

- Group CSV files by one or more columns  
- Compute statistical summaries (mean, sum, min, max)  
- Export clean, ready-to-use output files  

It works with any dataset — sales logs, lab measurements, survey results, engineering tables, or general numeric CSV files.

---

## 🚀 Features

- Automatic detection of numerical columns  
- Flexible grouping (one or multiple columns)  
- Multiple aggregation modes:
  - `mean` (default)  
  - `sum`  
  - `min`  
  - `max`
- UTF-8 output for full compatibility  
- CLI interface for automation and scripting  

---

## ▶️ Usage

From the project root:

```bash
python file_tools/csv_summarizer/csv_summarizer.py \
    input.csv \
    output.csv \
    --group ColumnA ColumnB \
    --mode mean
```

---

## 📌 Example

### Input (`sales.csv`)
| Product | Region | Price | Quantity |
|---------|--------|-------|----------|
| A       | EU     | 10    | 5        |
| A       | EU     | 12    | 3        |
| B       | US     | 7     | 8        |

### Command

```bash
python file_tools/csv_summarizer/csv_summarizer.py sales.csv summary.csv --group Product Region --mode mean
```

### Output
| Product | Region | Price | Quantity |
|---------|--------|-------|----------|
| A       | EU     | 11    | 4        |
| B       | US     | 7     | 8        |

---

## 📦 Requirements

```
pandas
numpy
```

---

## 📝 Notes

- Non-numeric columns are ignored during calculations  
- Group columns must exist in the input CSV  
- Output is UTF-8 encoded and Excel-friendly  

---

## 📬 Contact

Feel free to reach out for suggestions or improvements.
