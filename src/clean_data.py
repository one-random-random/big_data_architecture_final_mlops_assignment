import os
import pandas as pd

df = pd.read_csv('../data/Salary_Data.csv')
cleaned_data_file_name = 'cleaned_salary_data.csv'

print("Original data")
print(df.head())

# Strip whitespace
df.columns = df.columns.str.strip()

# Strip whitespace from row values
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

# Convert all to lower case
df = df.map(lambda x: x.lower() if isinstance(x, str) else x)

df.drop_duplicates(inplace=True)

workspace = os.getenv('GITHUB_WORKSPACE')

model_cleaning_dir = os.path.join(workspace, 'src')

output_path = os.path.join,(workspace, 'data', cleaned_data_file_name)

os.makedirs(model_cleaning_dir, exist_ok=True)

df.to_csv(output_path, index=False)

print(output_path)

print("Cleaned data: ")
print(df.head())

print(f"\nCleaned data saved to {cleaned_data_file_name}")