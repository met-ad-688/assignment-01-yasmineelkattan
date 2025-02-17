import pandas as pd

files = ["./questions.csv", "./question_tags.csv"]
count = 0

for file in files:
    try:
        df = pd.read_csv(file)
        count += df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False).any(), axis=1).sum()
    except FileNotFoundError:
        print(f"Warning: {file} not found.")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Total lines containing 'GitHub': {count}")