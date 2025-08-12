import os
import kaggle
import pandas as pd
import pathlib
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from config import DATA_PATH

def ingest_kaggle_data(handle, path=DATA_PATH):
    api = kaggle.KaggleApi()
    api.authenticate()
    
    #Ensures path is a pathlib path; converts it if it is a string, and keeps it the same otherwise
    path = pathlib.Path(path)
        
    path.mkdir(parents=True, exist_ok=True)

    api.dataset_download_files(handle, path=str(path), unzip=True)
    first_csv = [f for f in os.listdir(path) if f.endswith(".csv")][0]
    first_csv_path = os.path.join(path, first_csv)
    
    df = pd.read_csv(first_csv_path)
    
    return df

def list_column_types(df):
    binary_cols = [col for col in df.columns if df[col].nunique() == 2]
    num_cols = df.select_dtypes(include = "number").columns.tolist()
    for col in binary_cols:
        if col in num_cols:
            num_cols.remove(col)
    multi_cat_cols = df.columns.difference(binary_cols+num_cols).tolist()   
    
    return num_cols, binary_cols, multi_cat_cols

def one_hot_encode(df):    
    #Listing columns by type
    num_cols, binary_cols, multi_cat_cols = list_column_types(df)

    #One-hot encoding categorical columns
    binary_dummies = pd.get_dummies(df[binary_cols], drop_first=True).astype(int)
    multi_cat_dummies = pd.get_dummies(df[multi_cat_cols], drop_first=False).astype(int)
    df = df.drop(columns = binary_cols+multi_cat_cols)
    df = pd.concat([df[num_cols], multi_cat_dummies, binary_dummies], axis = 1)
    
    return df

def impute_missing(df):
    num_cols, binary_cols, multi_cat_cols = list_column_types(df)

    num_transform = SimpleImputer(strategy="median")
    cat_transform = SimpleImputer(strategy="most_frequent")
    cat_cols = binary_cols + multi_cat_cols
    all_cols = num_cols + cat_cols

    col_transform = ColumnTransformer(transformers=[("num", num_transform, num_cols), ("cat", cat_transform, cat_cols)])
    df = pd.DataFrame(col_transform.fit_transform(df), columns = all_cols)
    df[num_cols] = df[num_cols].apply(pd.to_numeric)
    df[cat_cols] = df[cat_cols].astype(str)

    return df
    