import os
from pathlib import Path

from pandas import read_csv
from joblib import dump
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from constants import CLEANED_DATA_FILE_NAME, TEST_SIZE, RANDOM_STATE

project_root = Path(__file__).resolve().parent.parent
project_src_dir = project_root / 'src'
data_path = project_root / 'data'
cleaned_data_path = data_path / CLEANED_DATA_FILE_NAME
models_path = project_root / 'models'

if os.path.exists(cleaned_data_path):
    print(f"File found: {cleaned_data_path}")
else:
    raise FileNotFoundError(f"Run the clean_data script! File expected: {cleaned_data_path}")

df = read_csv(cleaned_data_path)
print(df.head())

X = df["YearsExperience"].values.reshape(-1, 1)
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

model = LinearRegression()
model.fit(X_train, y_train)
dump(model, f"{models_path}/YearsExperienceSalaryModel.pkl")
