import pandas as pd

def load_activity_data(path: str) -> pd.DataFrame:
    """Load a CSV activity/event file."""
    return pd.read_csv(path)

def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """Basic, reproducible preprocessing for a preliminary prototype."""
    data = df.copy()
    data = data.drop_duplicates()

    # Convert categorical fields into numeric indicators when present.
    categorical = [c for c in ["activity_type", "channel", "device_type"] if c in data.columns]
    if categorical:
        data = pd.get_dummies(data, columns=categorical, dtype=int)

    return data

if __name__ == "__main__":
    print("Preprocessing module ready. Provide a CSV path when integrating real/suitable research data.")
