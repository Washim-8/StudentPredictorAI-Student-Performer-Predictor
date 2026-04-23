import os
import json
import joblib
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "spp_secret_key_2024"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "trained_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "model", "scaler.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "model", "label_encoder.pkl")
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "students.csv")

FEATURE_COLS = [
    "attendance", "internal_marks", "study_hours_per_day",
    "previous_cgpa", "assignments_completed", "extracurricular"
]

FIELD_RANGES = {
    "attendance": (0, 100),
    "internal_marks": (0, 100),
    "study_hours_per_day": (0, 10),
    "previous_cgpa": (0, 10),
    "assignments_completed": (0, 10),
    "extracurricular": (0, 1),
}

ADVICE = {
    "High": "🎉 Excellent! Keep maintaining your study habits. You're on the path to academic excellence!",
    "Average": "📚 You are on track! Focus more on attendance and daily study time to reach your full potential.",
    "Low": "⚠️ Immediate intervention recommended. Seek academic support and improve your attendance and study schedule."
}

MODEL_NAME = "RandomForest"


def load_model_artifacts():
    """Load model, scaler, and encoder from disk."""
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    le = joblib.load(ENCODER_PATH)
    # Try to infer model name
    global MODEL_NAME
    MODEL_NAME = type(model).__name__
    return model, scaler, le


def validate_inputs(form_data):
    """Validate form inputs (supports both form data and JSON dict). Returns (cleaned_dict, errors)."""
    errors = []
    cleaned = {}

    for field in FEATURE_COLS:
        val = form_data.get(field, None)
        if val is None or str(val).strip() == "":
            errors.append(f"'{field.replace('_', ' ').title()}' is required.")
            continue
        try:
            num = float(val)
        except (ValueError, TypeError):
            errors.append(f"'{field.replace('_', ' ').title()}' must be a number.")
            continue

        lo, hi = FIELD_RANGES[field]
        if not (lo <= num <= hi):
            errors.append(f"'{field.replace('_', ' ').title()}' must be between {lo} and {hi}.")
            continue

        cleaned[field] = num

    return cleaned, errors


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    cleaned, errors = validate_inputs(request.form)

    if errors:
        for err in errors:
            flash(err, "danger")
        return redirect(url_for("index"))

    try:
        model, scaler, le = load_model_artifacts()
    except Exception as e:
        flash("Model not found. Please train the model first by running: python model/train.py", "danger")
        return redirect(url_for("index"))

    features = np.array([[
        cleaned["attendance"],
        cleaned["internal_marks"],
        cleaned["study_hours_per_day"],
        cleaned["previous_cgpa"],
        cleaned["assignments_completed"],
        int(cleaned["extracurricular"]),
    ]])

    features_scaled = scaler.transform(features)
    pred_encoded = model.predict(features_scaled)[0]
    pred_label = le.inverse_transform([pred_encoded])[0]

    proba = model.predict_proba(features_scaled)[0]
    confidence = float(max(proba)) * 100

    advice = ADVICE.get(pred_label, "")

    return render_template(
        "result.html",
        prediction=pred_label,
        confidence=round(confidence, 2),
        advice=advice,
        inputs=cleaned,
        model_name=MODEL_NAME
    )


@app.route("/api/predict", methods=["GET", "POST"])
def api_predict():
    if request.method == "GET":
        return jsonify({
            "message": "Send a POST request with JSON body containing: attendance, internal_marks, study_hours_per_day, previous_cgpa, assignments_completed, extracurricular",
            "example": {
                "attendance": 80,
                "internal_marks": 75,
                "study_hours_per_day": 6,
                "previous_cgpa": 8.5,
                "assignments_completed": 8,
                "extracurricular": 1
            }
        })

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    cleaned, errors = validate_inputs(data)
    if errors:
        return jsonify({"error": "Validation failed", "details": errors}), 422

    try:
        model, scaler, le = load_model_artifacts()
    except Exception as e:
        return jsonify({"error": "Model not trained yet. Run: python model/train.py"}), 503

    features = np.array([[
        cleaned["attendance"], cleaned["internal_marks"],
        cleaned["study_hours_per_day"], cleaned["previous_cgpa"],
        cleaned["assignments_completed"], int(cleaned["extracurricular"]),
    ]])

    features_scaled = scaler.transform(features)
    pred_encoded = model.predict(features_scaled)[0]
    pred_label = le.inverse_transform([pred_encoded])[0]

    proba = model.predict_proba(features_scaled)[0]
    confidence = round(float(max(proba)), 4)

    return jsonify({
        "prediction": pred_label,
        "confidence": confidence,
        "model": MODEL_NAME,
        "advice": ADVICE.get(pred_label, "")
    })


@app.route("/dashboard")
def dashboard():
    try:
        df = pd.read_csv(DATASET_PATH)
    except FileNotFoundError:
        flash("Dataset not found. Please run: python model/train.py", "danger")
        return redirect(url_for("index"))

    total = len(df)
    counts = df["performance"].value_counts().to_dict()

    pct_high = round(counts.get("High", 0) / total * 100, 1)
    pct_avg = round(counts.get("Average", 0) / total * 100, 1)
    pct_low = round(counts.get("Low", 0) / total * 100, 1)

    # Group averages
    group_avg = df.groupby("performance")[
        ["attendance", "internal_marks", "study_hours_per_day", "previous_cgpa"]
    ].mean().round(2)

    groups = group_avg.index.tolist()
    avg_attendance = group_avg["attendance"].tolist()
    avg_marks = group_avg["internal_marks"].tolist()
    avg_study = group_avg["study_hours_per_day"].tolist()
    avg_cgpa = group_avg["previous_cgpa"].tolist()

    pie_labels = list(counts.keys())
    pie_values = list(counts.values())

    return render_template(
        "dashboard.html",
        total=total,
        pct_high=pct_high,
        pct_avg=pct_avg,
        pct_low=pct_low,
        groups=json.dumps(groups),
        avg_attendance=json.dumps(avg_attendance),
        avg_marks=json.dumps(avg_marks),
        avg_study=json.dumps(avg_study),
        avg_cgpa=json.dumps(avg_cgpa),
        pie_labels=json.dumps(pie_labels),
        pie_values=json.dumps(pie_values),
        count_high=counts.get("High", 0),
        count_avg=counts.get("Average", 0),
        count_low=counts.get("Low", 0),
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/about_contact")
def about_contact():
    return render_template("about_contact.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
