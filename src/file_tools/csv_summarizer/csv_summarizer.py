import pandas as pd
import numpy as np
import argparse
import sys
import os
from datetime import datetime


def add_timestamp_to_filename(output_path, group_cols):
    """
    Verilen output yoluna timestamp ekler.
    Örn: output.csv -> output_2025-01-23_23-55.csv
    """
    folder = os.path.dirname(output_path)
    name, ext = os.path.splitext(os.path.basename(output_path))

    # Timestamp oluştur
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    # Grup kolonlarını kısa bir şekilde dosya adına ekleyelim
    if group_cols:
        group_part = "_".join([c.replace(" ", "") for c in group_cols])
        new_name = f"{name}_{group_part}_{timestamp}{ext}"
    else:
        new_name = f"{name}_{timestamp}{ext}"

    return os.path.join(folder, new_name)


def summarize_csv(input_path, output_path, group_cols, agg_mode="mean"):
    """
    Genel amaçlı CSV özetleyici.
    
    • group_cols: ["Category", "Type"] gibi gruplanacak kolonlar
    • agg_mode: mean | sum | min | max
    """
    if not os.path.exists(input_path):
        print(f"Hata: {input_path} bulunamadı.")
        sys.exit(1)

    df = pd.read_csv(input_path)

    # Sayısal kolonları otomatik bul
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    # Grup kolonları numeric'te varsa çıkart
    for c in group_cols:
        if c in numeric_cols:
            numeric_cols.remove(c)

    if not numeric_cols:
        print("Sayısal kolon bulunamadı. Özetleme yapılamıyor.")
        sys.exit(1)

    # Gruplama
    grouped = df.groupby(group_cols)

    # Kullanıcının istediği özetleme tipi
    if agg_mode == "mean":
        agg_df = grouped[numeric_cols].mean().reset_index()
    elif agg_mode == "sum":
        agg_df = grouped[numeric_cols].sum().reset_index()
    elif agg_mode == "min":
        agg_df = grouped[numeric_cols].min().reset_index()
    elif agg_mode == "max":
        agg_df = grouped[numeric_cols].max().reset_index()
    else:
        print("Hatalı agg_mode. Kullanılabilir: mean | sum | min | max")
        sys.exit(1)

    # Timestamp'li dosya adı oluştur
    final_output_path = add_timestamp_to_filename(output_path, group_cols)

    # CSV olarak kaydet
    agg_df.to_csv(final_output_path, index=False, encoding="utf-8-sig")
    print(f"Özetleme tamamlandı: {final_output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genel amaçlı CSV özetleyici.")
    parser.add_argument("input", help="Girdi CSV dosyası")
    parser.add_argument("output", help="Çıktı CSV dosyası (timestamp otomatik eklenecek)")
    parser.add_argument("--group", nargs="+", required=True,
                        help="Gruplama yapılacak kolonlar (örn: --group Category Type)")
    parser.add_argument("--mode", choices=["mean", "sum", "min", "max"], default="mean",
                        help="Özetleme türü (varsayılan: mean)")

    args = parser.parse_args()

    summarize_csv(
        input_path=args.input,
        output_path=args.output,
        group_cols=args.group,
        agg_mode=args.mode
    )
