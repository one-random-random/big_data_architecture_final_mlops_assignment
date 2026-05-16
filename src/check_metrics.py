import json
from pathlib import Path
from constants import PRODUCTION_METRICS_FILE_NAME, CANDIDATE_METRICS_FILE_NAME


project_root = Path(__file__).resolve().parent.parent
candidate_metrics_path = project_root / "reports" / "metrics" / CANDIDATE_METRICS_FILE_NAME
production_metrics_path = project_root / "models" / PRODUCTION_METRICS_FILE_NAME


if not candidate_metrics_path.exists():
    raise FileNotFoundError(f"Candidate metrics file not found: {candidate_metrics_path}")
if not production_metrics_path.exists():
    raise FileNotFoundError(f"Production metrics file not found: {production_metrics_path}")


with open(candidate_metrics_path) as candidate_file:
    candidate_metrics = json.load(candidate_file)
with open(production_metrics_path) as production_file:
    production_metrics = json.load(production_file)

candidate_r2_score = candidate_metrics["r2_score"]
minimum_r2_score = production_metrics["minimum_r2_score"]

print(f"Candidate r2_score: {candidate_r2_score}")
print(f"Minimum required r2_score: {minimum_r2_score}")


# Since this is being used in the workflow, by throwing an error it stops the workflow,
# and therefore stopping any image building or deployment taking place.
if candidate_r2_score < minimum_r2_score:
    raise ValueError(
        f"Model quality check failed. Candidate r2_score {candidate_r2_score} "
        f"is below minimum required r2_score {minimum_r2_score}."
    )

# This will only be printed when the candidate model has passed the minimum requirement
# and will allow the rest of the workflow to continue.
print("Model quality check passed.")
