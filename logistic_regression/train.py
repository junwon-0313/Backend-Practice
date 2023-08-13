import argparse
import sys
import numpy as np
from sklearn.linear_model import LogisticRegression
import mlflow
import mlflow.sklearn

if __name__ == "__main__":
    mlflow.sklearn.autolog()
    
    X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
    y = np.array([0, 0, 1, 1, 1, 0])

    lr = LogisticRegression(
        solver=sys.argv[1], penalty=sys.argv[2], l1_ratio=float(sys.argv[3])
    )

    with mlflow.start_run() as run:
        lr.fit(X,y)
     
    score = lr.score(X, y)  
    print("Score:", score)

    # mlflow.start_run()  # Start an MLflow run

    # mlflow.log_param("penalty", penalty)
    # mlflow.log_param("l1_ratio", l1_ratio)  # Fixed typo: '0.1' -> l1_ratio
    # mlflow.log_metric("score", score)
    # mlflow.sklearn.log_model(lr, "model")

    # mlflow.end_run()  # End the MLflow run
