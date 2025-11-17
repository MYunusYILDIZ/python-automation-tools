# DOC → DOCX Converter

This tool converts all `.doc` files inside a given folder into `.docx` format using Microsoft Word’s COM automation interface.

It is designed as a lightweight and practical utility for automating bulk document conversions on Windows.

---

## 🚀 Features

- Converts **all `.doc` files** in a folder to `.docx`
- Cleans file names:
  - **Removes Turkish characters** (ç → c, ğ → g, ı → i, ö → o, ş → s, ü → u)
  - Removes unsupported / unsafe characters
  - Normalizes multiple spaces
  - Prevents overly long filenames
- Automatically creates required folders
- Safe handling of long Windows paths
- Clear status logging
- Windows-only (Word COM automation)

---

## 📁 Folder Structure

The script expects the following directory structure relative to its own location:

doc_files/        → place .doc files here  
converted_docs/   → converted .docx files will be saved here  

These folders will be created automatically if they do not exist.

---

## 🔧 Requirements

- **Windows OS**
- **Microsoft Word** installed  
- Python dependency:

   ```bash
  pip install pywin32

## ▶️ Usage

From the project root:

  ```bash
  python src/file_tools/doc_to_docx_converter/doc_to_docx_converter.py
  ```
The tool will:

1. Scan `doc_files/` for `.doc` files  
2. Clean unsafe or problematic filenames  
3. Convert documents to `.docx`  
4. Save output into `converted_docs/`  
5. Print a detailed conversion summary  

---

## ⚠️ Notes & Limitations

- This tool works only on Windows (Word COM automation)  
- Password-protected .doc files are not supported and will likely fail during conversion
- If Microsoft Word is already running, automation may be affected  
- Filename cleaning ensures Windows filesystem compatibility  

---
