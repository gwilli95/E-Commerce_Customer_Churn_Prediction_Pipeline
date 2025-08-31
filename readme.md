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
 - `uv.lock` and `pyproject.toml`: This project utilizes uv dependency management.

## Setup and Usage
### Prerequisites
 - Python version 3.10 or higher.
 - uv dependency manager installed
 - Kaggle account and authentication

### Limitations
 - Limited error handling (such as in utils functions); scaling this project or adapting it for use with substantially different datasets may cause runtime errors and require modifying code directly.

### Usage Steps
  - Clone repository
    - `git clone https://github.com/gwilli95/E-Commerce_Customer_Churn_Prediction_Pipeline`
  - Kaggle authentication
    - Kaggle authentication performed privately and automatically by source code once users have taken the following authentication steps (see Kaggle API webpage for details: https://www.kaggle.com/docs/api):
        - Kaggle > "Account" tab > "Create New Token" --> This will download a file named kaggle.json with API credentials.
        - Use command-line interface to move kaggle.json to .kaggle folder
            - On Linux/macOS:
              - `mkdir -p ~/.kaggle`
              - `mv ~/Downloads/kaggle.json ~/.kaggle/`
              - `chmod 600 ~/.kaggle/kaggle.json`
            - On Windows:
              - `mkdir $env:USERPROFILE\.kaggle`
              - `move ~\Downloads\kaggle.json $env:USERPROFILE\.kaggle\`
  - Install uv if needed and sync dependencies
    - Run `pip install uv`
    - Run `uv sync`
  - Mac users:
    - When attempting to sync dependencies using uv, particularly if the repository is cloned into an iCloud folder, you may encounter a Python version error in the Terminal:

    `file pyproject.toml`
    ```
    pyproject.toml: cannot open 'pyproject.toml' (No such file or directory)
    ```
  
    `uv sync`

    ```
    × No solution found when resolving dependencies for split (markers: python_full_version == '3.8.*'):
    ╰─▶ Because the requested Python version (>=3.8) does not satisfy Python>=3.9 and pandas>=2.3.1 depends on Python>=3.9, we can
        conclude that pandas>=2.3.1 cannot be used.
        And because only the following versions of pandas are available:
            pandas<=2.3.1
            pandas==2.3.2
        and your project depends on pandas>=2.3.1, we can conclude that your project's requirements are unsatisfiable.
    ```

    - This may be due to an issue where the project files appear in Finder or VS Code but are not yet fully downloaded and recognized by the Terminal, causing the Terminal not to recognize the Python version constraints specified in the `pyproject.toml` file. The easiest solution is to copy the full contents of the `pyproject.toml` file, delete the file, create a new file titled `pyproject.toml` in the same location, paste the contents, and save it. This creates a new local file recognized by the Terminal, and running `uv sync` again should download the dependencies as intended.