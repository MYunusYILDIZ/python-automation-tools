import pandas as pd
import numpy as np
import argparse
import sys
import os


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

    # CSV olarak kaydet
    agg_df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"Özetleme tamamlandı: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genel amaçlı CSV özetleyici.")
    parser.add_argument("input", help="Girdi CSV dosyası")
    parser.add_argument("output", help="Çıktı CSV dosyası")
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
