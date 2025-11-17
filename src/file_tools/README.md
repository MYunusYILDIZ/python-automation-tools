# File Tools

This module contains small, modular utilities focused on file operations.  
Each tool is placed in its own folder and includes a dedicated README for usage details.

The tools in this directory are designed to be:
- Lightweight
- Practical
- Easy to understand
- Independent from each other
- Suitable for automation and scripting workflows

---

## Available Tools

### 📄 DOC → DOCX Converter
Folder: `doc_to_docx_converter`

Converts all `.doc` files inside a directory into `.docx` format using Microsoft Word's COM automation.  
Includes filename cleaning (Turkish character removal, unsafe character filtering, length normalization).

---

## Planned Tools

These tools will be added as the project grows:

### 📝 Batch File Renamer  
Rename files in bulk using patterns, prefixes, numbering, and cleanup rules.

### 📦 File Compressor  
Automated ZIP creation for selected files or entire folders.

### 🔍 Duplicate File Detector  
Finds duplicate files using hashing or size+name matching.

### 🧹 Filename Cleaner  
Cleans invalid characters, spaces, and formatting issues in multiple files.

---

## Structure

Each tool follows this structure:
```
tool_name/
  tool_name.py
  README.md
```

Example:
```
doc_to_docx_converter/
  doc_to_docx_converter.py
  README.md
```

---

This folder will continue expanding with new file-related utilities aimed at automation and productivity.


