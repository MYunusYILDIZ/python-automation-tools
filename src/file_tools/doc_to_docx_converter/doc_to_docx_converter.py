import os
import re
import string
import traceback

try:
    import win32com.client as win32
except ImportError:
    win32 = None


def clean_filename(filename, max_length=50):
    """
    Cleans the filename from unsafe characters and shortens it.
    """
    name, ext = os.path.splitext(filename)

    # Turkish character mapping
    replacements = {
        'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
        'Ç': 'C', 'Ğ': 'G', 'İ': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U'
    }
    name = ''.join(replacements.get(c, c) for c in name)

    allowed_chars = string.ascii_letters + string.digits + " _-."
    name = ''.join(c for c in name if c in allowed_chars)

    name = re.sub(r'\s+', ' ', name)

    if len(name) > max_length:
        name = name[:max_length]

    name = name.strip(' ._-')

    if not name:
        name = "converted_file"

    return name + ext


def convert_doc_to_docx(source_folder, target_folder):
    """
    Converts all .doc files in a folder to .docx.
    Windows + Microsoft Word required.
    """
    if win32 is None:
        print("[ERROR] Missing dependency: pywin32 (win32com).")
        print("This tool currently works only on Windows.")
        return []

    os.makedirs(source_folder, exist_ok=True)
    os.makedirs(target_folder, exist_ok=True)

    doc_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.doc')]

    if not doc_files:
        print(f"[INFO] No .doc files found in {source_folder}")
        return []

    print(f"[INFO] Found {len(doc_files)} .doc files:")
    for f in doc_files:
        print(f" - {f}")

    converted = []

    try:
        word = win32.Dispatch("Word.Application")
        word.Visible = False
        word.DisplayAlerts = False

        for doc_file in doc_files:
            try:
                src_path = os.path.abspath(os.path.join(source_folder, doc_file))
                clean_name = clean_filename(doc_file)[:-4] + ".docx"
                dst_path = os.path.abspath(os.path.join(target_folder, clean_name))

                if len(dst_path) > 220:
                    short_name = clean_filename(doc_file, max_length=30)[:-4] + ".docx"
                    dst_path = os.path.abspath(os.path.join(target_folder, short_name))

                doc = word.Documents.Open(src_path)
                doc.SaveAs(dst_path, FileFormat=16)  # 16 = docx
                doc.Close()

                print(f"[OK] {doc_file} → {clean_name}")
                converted.append(dst_path)

            except Exception as e:
                print(f"[FAIL] Error converting {doc_file}: {e}")
                print(traceback.format_exc())

    except Exception as e:
        print(f"[CRITICAL] Word application error: {e}")
        return []
    finally:
        try:
            word.Quit()
        except:
            pass

    print("\n[INFO] Conversion finished.")
    print(f"[INFO] Total converted files: {len(converted)}")

    return converted


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SOURCE = os.path.join(BASE_DIR, "../../doc_files")
    TARGET = os.path.join(BASE_DIR, "../../converted_docs")

    print(f"Source folder: {os.path.abspath(SOURCE)}")
    print(f"Target folder: {os.path.abspath(TARGET)}")

    convert_doc_to_docx(SOURCE, TARGET)
