import pandas as pd
import numpy as np
import os
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "..", "dataset", "students.csv")
MODEL_PATH = os.path.join(BASE_DIR, "trained_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "label_encoder.pkl")

FEATURE_COLS = [
    "attendance", "internal_marks", "study_hours_per_day",
    "previous_cgpa", "assignments_completed", "extracurricular"
]
TARGET_COL = "performance"


def load_and_preprocess(path=None):
    if path is None:
        path = DATASET_PATH

    df = pd.read_csv(path)

    # Drop non-feature columns
    df = df.drop(columns=["student_id", "name"], errors="ignore")

    # Handle missing values
    for col in FEATURE_COLS:
        if df[col].isnull().any():
            df[col].fillna(df[col].median(), inplace=True)

    if df[TARGET_COL].isnull().any():
        df[TARGET_COL].fillna(df[TARGET_COL].mode()[0], inplace=True)

    return df


def train_and_evaluate():
    df = load_and_preprocess()

    X = df[FEATURE_COLS]
    y = df[TARGET_COL]

    # Encode labels
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )

    models = {
        "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42),
        "DecisionTree": DecisionTreeClassifier(random_state=42),
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
        "SVC": SVC(probability=True, random_state=42),
    }

    results = []
    best_model = None
    best_score = 0
    best_model_name = ""

    print("\n" + "=" * 75)
    print(f"{'Model':<22} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1':>10}")
    print("=" * 75)

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average="weighted", zero_division=0)
        rec = recall_score(y_test, y_pred, average="weighted", zero_division=0)
        f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)
        cm = confusion_matrix(y_test, y_pred)

        print(f"{name:<22} {acc:>10.4f} {prec:>10.4f} {rec:>10.4f} {f1:>10.4f}")

        results.append({
            "model": name, "accuracy": acc, "precision": prec,
            "recall": rec, "f1": f1, "cm": cm, "obj": model
        })

        if acc > best_score:
            best_score = acc
            best_model = model
            best_model_name = name

    print("=" * 75)
    print(f"\nBest Model: {best_model_name} | Accuracy: {best_score:.4f}\n")

    # Save best model, scaler, encoder
    joblib.dump(best_model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    joblib.dump(le, ENCODER_PATH)

    print(f"Model saved  : {MODEL_PATH}")
    print(f"Scaler saved : {SCALER_PATH}")
    print(f"Encoder saved: {ENCODER_PATH}")

    return best_model_name, best_score, results, le, scaler


def predict_single(input_dict, model=None, scaler=None, le=None):
    """Predict performance for a single student input dict."""
    if model is None:
        model = joblib.load(MODEL_PATH)
    if scaler is None:
        scaler = joblib.load(SCALER_PATH)
    if le is None:
        le = joblib.load(ENCODER_PATH)

    features = np.array([[
        float(input_dict["attendance"]),
        float(input_dict["internal_marks"]),
        float(input_dict["study_hours_per_day"]),
        float(input_dict["previous_cgpa"]),
        float(input_dict["assignments_completed"]),
        int(input_dict["extracurricular"]),
    ]])

    features_scaled = scaler.transform(features)
    pred_encoded = model.predict(features_scaled)[0]
    pred_label = le.inverse_transform([pred_encoded])[0]

    proba = model.predict_proba(features_scaled)[0]
    confidence = float(max(proba))

    return pred_label, confidence


if __name__ == "__main__":
    train_and_evaluate()
