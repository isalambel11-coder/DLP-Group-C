import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_baseline(df: pd.DataFrame, target: str = "label"):
    """Train a simple baseline classifier when labelled data is available."""
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' is not available.")

    X = df.drop(columns=[target])
    y = df[target]

    X = X.select_dtypes(include=["number", "bool"])
    if X.empty:
        raise ValueError("No numeric features are available after preprocessing.")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced"
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(classification_report(y_test, predictions))
    return model

if __name__ == "__main__":
    print("Baseline DLP detection module ready.")
