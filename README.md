# End-to-End-Machine-Learning-Project-with-MLFLOW

## Overview

This project demonstrates an end-to-end machine learning workflow using MLFLOW. It covers data preprocessing, model training, hyperparameter tuning, and model deployment.

## Features

- Data preprocessing and feature engineering
- Model training and evaluation
- Hyperparameter tuning
- Model versioning and tracking with MLFLOW
- Model deployment

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/dipan97-hue/End-to-End-Machine-Learning-Project-with-MLFLOW 
    ```
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### dagshub 
[dagshub](https://dagshub.com)
 ```sh
import dagshub
dagshub.init(repo_owner='dipan97-hue', repo_name='End-to-End-Machine-Learning-Project-with-MLFLOW', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
  
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License.