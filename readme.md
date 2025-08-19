# Customer Churn Prediction Pipeline Using Kaggle API and Random Forest
 - Summary: Data science project that ingests e-commerce customer churn dataset from Kaggle API, visualizes and preprocesses the dataset, trains Random Forest Classifier with light hyper-parameter tuning, and outputs predicted churn back to the processed dataset.
- Use: This project demonstrates a full basic pipeline and provides a scalable and expandable template for similar projects and applications.

## Project Overview
### Data Used
This project uses "E-Commerce Dataset," published on Kaggle by user Anagha Paul in October 2024. It is a synthetic dataset with a mix of realistic features (8 numerical and 12 categorical) and with intentionally missing values, and it is intented for practicing and demonstrating industry-relevant data cleaning, exploration, and modeling. Its identifier, used for ingestion via the Kaggle package, is "anaghapaul/e-commerce-dataset."

### Model Used
The model used is Random Forest Classifier from scikit-learn. GridSearchCV was used for light hyper-parameter optimization.

### Model Results
```
Best estimator: RandomForestClassifier(n_estimators=300, random_state=42)

Train classification report:
               precision    recall  f1-score   support

           0       1.00      1.00      1.00      3277
           1       1.00      1.00      1.00       664

    accuracy                           1.00      3941
   macro avg       1.00      1.00      1.00      3941
weighted avg       1.00      1.00      1.00      3941

Test classification report:
               precision    recall  f1-score   support

           0       0.96      0.99      0.98      1405
           1       0.95      0.81      0.87       284

    accuracy                           0.96      1689
   macro avg       0.95      0.90      0.92      1689
weighted avg       0.96      0.96      0.96      1689
```

### Project Structure
 - `__init__.py`: Left empty and used to denote the src/ folder as a package for modular imports.
 - `config.py`: Used for centralized configuration of the Kaggle dataset identifier and the paths for all project folders, which are imported in the notebooks.
 - `utils.py`: Stores functions used for data ingestion and preprocessing.
 - `poetry.lock` and `pyproject.toml`: This project utilizes Poetry dependency management.

## Setup and Usage
### Prerequisites
 - Python version 3.10 or higher.
 - Poetry dependency manager installed
 - Kaggle account and authentication

### Limitations
 - Limited error handling (such as in utils functions); scaling this project or adapting it for use with substantially different datasets may cause runtime errors and require modifying code directly.

### Usage Steps
  - Clone repository
    - `git clone https://github.com/gwilli95/E-Commerce_Customer_Churn_Prediction_Pipeline`
  - Install Poetry if needed
    - Run `pip install poetry` OR
    - See Poetry website (https://pypi.org/project/poetry/) for details on alternative methods that could be more preferable for your setup.
 - Download dependencies
    - Run `poetry install --no-root`
 - Kaggle authentication
    - Kaggle authentication performed privately and automatically by source code once users have taken the following authentication steps (see Kaggle API webpage for details: https://www.kaggle.com/docs/api):
        - Kaggle > "Account" tab > "Create New Token" --> This will download a file named kaggle.json with API credentials.
        - Use command-line interface to move kaggle.json to .kaggle folder
            - On Linux/OSX:
              - `mkdir -p ~/.kaggle`
              - `mv ~/Downloads/kaggle.json ~/.kaggle/`
              - `chmod 600 ~/.kaggle/kaggle.json`
            - On Windows:
              - `mkdir $env:USERPROFILE\.kaggle`
              - `move ~\Downloads\kaggle.json $env:USERPROFILE\.kaggle\`