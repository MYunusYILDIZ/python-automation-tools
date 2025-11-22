import pandas as pd
from src.file_tools.csv_summarizer.csv_summarizer import summarize_csv
import os
import tempfile


def test_summarize_csv_mean():
    # Temporary çalışma klasörü açalım
    with tempfile.TemporaryDirectory() as tmp:
        input_path = os.path.join(tmp, "input.csv")
        output_path = os.path.join(tmp, "output.csv")

        # Test CSV dosyası oluştur
        df = pd.DataFrame({
            "Product": ["A", "A", "B"],
            "Price": [10, 20, 7],
            "Quantity": [5, 5, 10]
        })
        df.to_csv(input_path, index=False)

        # Fonksiyonu çağır
        output_csv = summarize_csv(
            input_path=input_path,
            output_path=output_path,
            group_cols=["Product"],
            agg_mode="mean",
            add_timestamp=False
        )

        out = pd.read_csv(output_csv)

        # Beklenen değerler
        assert out[out["Product"] == "A"]["Price"].iloc[0] == 15
        assert out[out["Product"] == "A"]["Quantity"].iloc[0] == 5
        assert out[out["Product"] == "B"]["Price"].iloc[0] == 7
        assert out[out["Product"] == "B"]["Quantity"].iloc[0] == 10
