import pandas as pd
import numpy as np

def get_column_type_counts(df: pd.DataFrame) -> list:
    return list(np.unique([str(type(col)) for col in df.columns]))
