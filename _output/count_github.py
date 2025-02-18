#!/usr/bin/env python3

import pandas as pd

files = ["_output/questions.csv", "_output/question_tags.csv"]
total_count = 0

for file in files:
    try:
        count = 0
        for chunk in pd.read_csv(file, dtype=str, on_bad_lines="skip", chunksize=10000):  # Adjust chunk size if needed
            count += chunk.apply(lambda row: row.astype(str).str.contains("GitHub", case=False, na=False).any(), axis=1).sum()
        
        total_count += count

    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Total lines containing 'GitHub': {total_count}")
