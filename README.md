# Python-Automation-Tools

A collection of practical, lightweight tools built in Python for automation, data processing, and utility applications.

## 🚀 Overview

This repository demonstrates a modular toolbox of scripts and mini-applications designed for everyday automation tasks, project prototyping, and freelance use-cases.  
Each tool lives in its own folder under `src/file_tools/` and includes examples so you can start quickly.

## 📁 Structure

```
python-automation-tools/
│
├── src/
│   └── file_tools/
│       ├── csv_summarizer/
│       ├── doc_to_docx_converter/
│       └── interval_mapper/         ← (incoming tool)
│
├── examples/
│   ├── csv_summarizer/
│   │   ├── sample_input.csv
│   │   └── sample_output.csv
│   ├── doc_to_docx_converter/
│   │   └── …                     ← example files
│   └── interval_mapper/
│       ├── sample_intervals.csv
│       ├── sample_input.csv
│       └── sample_output.csv
│
├── requirements.txt
├── LICENSE
└── README.md
```

## 🛠 Tools Included

### 📄 csv_summarizer  
Group CSV files by one or more columns and compute summary statistics (mean, sum, min, max).  
See `src/file_tools/csv_summarizer/README.md` for details.

### 📁 doc_to_docx_converter  
Bulk convert `.doc` files into `.docx`, clean filenames, and produce ready-to-use output folders.  
See `src/file_tools/doc_to_docx_converter/README.md` for details.

### 📊 interval_mapper  
Map numeric values against defined intervals and assign labels—ideal for engineering data workflow.  
See `src/file_tools/interval_mapper/README.md` for details.

## 📦 Requirements

```
pip install -r requirements.txt
```

Current requirements:

```
pandas
numpy
# (Add more as needed by each tool)
```

## 📌 How to Use

Choose the tool you want and follow its individual README instructions.  
For example, for `csv_summarizer`:

```bash
python src/file_tools/csv_summarizer/csv_summarizer.py \
    examples/csv_summarizer/sample_input.csv \
    examples/csv_summarizer/sample_output.csv \
    --group Product Region \
    --mode mean
```

## 🧭 Roadmap & Next Steps

- Add more file-tool modules: **excel_cleaner**, **batch_file_renamer**, **pdf_converter**  
- Improve documentation: add video or GIF demos  
- Add unit tests and CI workflows  
- Consider packaging selected tools as Python libraries  

## 🤝 Contributing

Feel free to open issues, suggest new tool ideas, or submit pull requests.  
All contributions are welcome—please follow the code style and include usage examples.

## 📬 Contact

M. Yunus YILDIZ  
📧 m.y.yildiz@outlook.com.tr  
🔗 LinkedIn: https://linkedin.com/in/myunusyildiz
