from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent  # adjust as needed

DATA_PATH = BASE_DIR / "data" / "comments_dataset.csv"

def load_data(filepath=DATA_PATH):
    df = pd.read_csv(filepath)
    return df

