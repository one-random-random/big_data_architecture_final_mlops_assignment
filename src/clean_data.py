from pathlib import Path

import pandas as pd

project_root = Path(__file__).resolve().parent.parent
data_path = project_root / 'data'
source_salary_data_path = data_path / 'Salary_Data.csv'
cleaned_data_file_name = 'cleaned_salary_data.csv'
output_path = data_path / cleaned_data_file_name

df = pd.read_csv(input_path)

print("Original data")
print(df.head())

# Strip whitespace
df.columns = df.columns.str.strip()

# Strip whitespace from row values
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

# Convert all to lower case
df = df.map(lambda x: x.lower() if isinstance(x, str) else x)

df.drop_duplicates(inplace=True)

output_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(str(output_path), index=False)

print(output_path)

print("Cleaned data: ")
print(df.head())

print(f"\nCleaned data saved to {cleaned_data_file_name}")
