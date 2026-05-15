import os
from pathlib import Path

from pandas import read_csv
import mlflow
from joblib import dump
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

from constants import CLEANED_DATA_FILE_NAME, TEST_SIZE, RANDOM_STATE, MODEL_FILE_NAME

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

## Do the mlflow run
with mlflow.start_run():
    # initialise and train
    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)

    mlflow.log_metric("r2_score", r2)
    mlflow.log_metric("mse", mse)

    result = mlflow.sklearn.log_model(sk_model=model, artifact_path="model")

    mlflow.register_model(
        model_uri=result.model_uri,
        name="my-linear-salary-registered-model"
    )

    print(f"Model scores - r2: {r2}, mse: {mse}")

dump(model, f"{models_path}/{MODEL_FILE_NAME}")
