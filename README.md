## Git Branching Strategy and Rules

- Main is main branch and considered true source of code for this project
- All code writting should be done so on feature branchs created from main
- Git Rule stops any direct pushes or force pushes to main
- Only way to get code onto main branch is to create a Pull Request from feature branch to the main branch.
    - Caveat - Since only me developing, have set the number of approvers to 0. This allows me to merge the PR's but forces the process at least. If more dev's join, increase to minimum of 1.



## Local MLflow Testing on Windows

Use these steps to run MLflow locally and test that `src/train.py` records model metrics.

### Prerequisites

- Run commands from the repository root.
- Use Anaconda Prompt or PowerShell.
- Ensure the dependencies are listed in `requirements.txt`.

### 1. Install dependencies and prepare data

```powershell
python -m pip install -r requirements.txt
python src\clean_data.py
```

### 2. Start the local MLflow server

Run:
```powershell
mlflow server --host 127.0.0.1 --port 5555 --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlartifacts
```

*Leave this terminal running while you train the model.*

### 3. Run training against MLflow

From a different terminal, trigger the training of the model, run:

```powershell
$env:MLFLOW_TRACKING_URI = "http://127.0.0.1:5555"
python src\train.py
```

### 4. Verify the run via the MLFlow UI App on local machine

```text
http://127.0.0.1:5555
```

Should now see the run you just did appear, it will have the `r2_score` and `mse`. The artifact should be present there.

## Local Docker Testing on Windows

Use these steps to build and run the Flask app in Docker locally.

### Prerequisites

- Docker Desktop is installed and running.
- Run commands from the repository root.

### 1. Build the Docker image

```powershell
docker build -t salary-prediction-app .
```

### 2. Run the container

```powershell
docker run --name salary-prediction-container -p 5000:5000 salary-prediction-app
```

### 3. Test the Flask app

Open these URLs in a browser:

```text
http://127.0.0.1:5000/
http://127.0.0.1:5000/predict?experience=2
```

### 4. Stop and remove the container

```powershell
docker stop salary-prediction-container
docker rm salary-prediction-container
```
