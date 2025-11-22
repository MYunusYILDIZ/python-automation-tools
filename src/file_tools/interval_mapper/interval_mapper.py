import pandas as pd
import argparse
import sys
import os


def map_intervals(intervals_path, points_path, output_path,
                  group_col=None, value_col="Value"):
    """
    Universal interval-to-value mapper.

    intervals.csv must contain:
        Min, Max, Label   (+ optional Group column)
    points.csv must contain:
        value_col         (+ optional Group column)
    """

    if not os.path.exists(intervals_path):
        print(f"Error: {intervals_path} not found.")
        sys.exit(1)
    if not os.path.exists(points_path):
        print(f"Error: {points_path} not found.")
        sys.exit(1)

    df_intervals = pd.read_csv(intervals_path)
    df_points = pd.read_csv(points_path)

    required_int_cols = {"Min", "Max", "Label"}
    if not required_int_cols.issubset(df_intervals.columns):
        print("Intervals file must contain: Min, Max, Label")
        sys.exit(1)

    if value_col not in df_points.columns:
        print(f"Points file must contain: {value_col}")
        sys.exit(1)

    # Sort intervals
    if group_col and group_col in df_intervals.columns:
        df_intervals = df_intervals.sort_values([group_col, "Min"]).reset_index(drop=True)
    else:
        df_intervals = df_intervals.sort_values(["Min"]).reset_index(drop=True)

    matched_rows = []

    for _, p in df_points.iterrows():
        value = p[value_col]
        group_val = p[group_col] if group_col else None

        if group_col:
            intervals_subset = df_intervals[df_intervals[group_col] == group_val]
        else:
            intervals_subset = df_intervals

        matched_label = None

        for _, interval in intervals_subset.iterrows():
            if interval["Min"] <= value <= interval["Max"]:
                matched_label = interval["Label"]
                break

        output = {
            value_col: value,
            "MatchedLabel": matched_label
        }

        if group_col:
            output[group_col] = group_val

        matched_rows.append(output)

    pd.DataFrame(matched_rows).to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"Mapping complete: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Universal interval mapper.")

    parser.add_argument("--intervals", required=True, help="Intervals CSV path")
    parser.add_argument("--points", required=True, help="Points CSV path")
    parser.add_argument("--output", required=True, help="Output CSV path")
    parser.add_argument("--group", help="Optional group column name")
    parser.add_argument("--value", default="Value",
                        help="Numeric column to map (default: Value)")

    args = parser.parse_args()

    map_intervals(
        intervals_path=args.intervals,
        points_path=args.points,
        output_path=args.output,
        group_col=args.group,
        value_col=args.value
    )
