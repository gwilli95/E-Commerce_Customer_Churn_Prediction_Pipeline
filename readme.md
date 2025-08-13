# Customer Churn Prediction Pipeline Using Kaggle API and Random Forest
This data science project ingests an e-commerce customer churn dataset from Kaggle using the Kaggle package API, visualizes and preprocesses the data, trains Random Forest Classifier with light hyper-parameter tuning, and outputs predicted churn back to the processed dataset, demonstrating a full basic pipeline and providing a scalable and expandable template for similar projects and applications.

## Project Overview
### Data Used
This project uses "E-Commerce Dataset," published on Kaggle by user Anagha Paul in October 2024. It is a synthetic dataset with a mix of realistic features (8 numerical and 12 categorical) and intentionally missing values, and it is intented for practicing and demonstrating industry-relevant data cleaning, exploration, and modeling. Its identifier, used for ingestion via the Kaggle package, is "anaghapaul/e-commerce-dataset."

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

### Project Structure: Supplemental Files
 - __init__.py: Left empty and used to denote the src/ folder as a package for modular imports.
 - config.py: Used for centralized configuration of the Kaggle dataset identifier and the paths for all project folders, which are imported in the notebooks.
 - utils.py: Stores functions used for data ingestion and preprocessing.
 - poetry.lock and pyproject.toml: This project utilizes Poetry dependency management.

## Setup and Usage
### Prerequisites
 - Python version 3.12 or higher.
 - ...