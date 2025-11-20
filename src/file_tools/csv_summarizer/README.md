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
- Aggregation modes: `mean`, `sum`, `min`, `max`
- **Optional auto-generated output filename with timestamp**  
- UTF-8 output (Excel-friendly)
- Command-line usage

---

## ▶️ Usage

From the project root:

```bash
python src/file_tools/csv_summarizer/csv_summarizer.py \
    input.csv \
    output.csv \
    --group ColumnA ColumnB \
    --mode mean
```
If you prefer automatic timestamped output filename, simply pass `auto` instead of a path:

```bash
python src/file_tools/csv_summarizer/csv_summarizer.py \
    input.csv \
    auto \
    --group ColumnA ColumnB
```
This will create a file like
```
summary_2025-01-14_23-55-12.csv
```
---

## 📌 Example (using the included dataset)

### Input  
Located at:

```
examples/csv_summarizer/sample_input.csv
```

Contents:

```
Product,Region,Price,Quantity
A,EU,10,5
A,EU,12,3
B,US,7,8
B,US,7,10
C,EU,5,12
C,EU,15,3
```

### Command

```bash
python src/file_tools/csv_summarizer/csv_summarizer.py \
    examples/csv_summarizer/sample_input.csv \
    examples/csv_summarizer/sample_output.csv \
    --group Product Region \
    --mode mean
```

### Output  
Generated at:

```
examples/csv_summarizer/sample_output.csv
```

Example output:

```
Product,Region,Price,Quantity
A,EU,11.0,4.0
B,US,7.0,9.0
C,EU,10.0,7.5
```

---

## 📦 Requirements

```
pandas
numpy
```

---

## 📝 Notes

- Non-numeric columns are ignored automatically  
- Group columns must exist in the CSV  
- Output is UTF-8 encoded  
- Use `auto` to automatically generate timestamped output filenames
---

## 📬 Contact

Feel free to reach out for suggestions or improvements.
