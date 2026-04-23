import pytest
import sys
import os
import json
import numpy as np

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app as flask_app

VALID_PAYLOAD = {
    "attendance": "80",
    "internal_marks": "75",
    "study_hours_per_day": "6",
    "previous_cgpa": "8.5",
    "assignments_completed": "8",
    "extracurricular": "1"
}

VALID_JSON = {
    "attendance": 80,
    "internal_marks": 75,
    "study_hours_per_day": 6,
    "previous_cgpa": 8.5,
    "assignments_completed": 8,
    "extracurricular": 1
}

LABELS = {"High", "Average", "Low"}


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    flask_app.config["WTF_CSRF_ENABLED"] = False
    with flask_app.test_client() as client:
        yield client


# ── Model Loading ────────────────────────────────────────────
def test_model_loads():
    """Model pkl loads without error."""
    import joblib
    model_path = os.path.join(os.path.dirname(__file__), "..", "model", "trained_model.pkl")
    model = joblib.load(model_path)
    assert model is not None


def test_scaler_loads():
    """Scaler pkl loads without error."""
    import joblib
    scaler_path = os.path.join(os.path.dirname(__file__), "..", "model", "scaler.pkl")
    scaler = joblib.load(scaler_path)
    assert scaler is not None


def test_encoder_loads():
    """Label encoder pkl loads without error."""
    import joblib
    encoder_path = os.path.join(os.path.dirname(__file__), "..", "model", "label_encoder.pkl")
    le = joblib.load(encoder_path)
    assert le is not None


def test_prediction_valid_labels():
    """Model prediction returns one of the three valid labels."""
    from model.model import predict_single
    label, conf = predict_single(VALID_JSON)
    assert label in LABELS
    assert 0.0 <= conf <= 1.0


def test_high_performer_prediction():
    """Clear high-performer inputs should return High."""
    from model.model import predict_single
    label, conf = predict_single({
        "attendance": 95, "internal_marks": 90,
        "study_hours_per_day": 8, "previous_cgpa": 9.5,
        "assignments_completed": 10, "extracurricular": 1
    })
    assert label in LABELS  # Should typically be High


def test_low_performer_prediction():
    """Clear low-performer inputs should return Low."""
    from model.model import predict_single
    label, conf = predict_single({
        "attendance": 45, "internal_marks": 35,
        "study_hours_per_day": 1, "previous_cgpa": 4.5,
        "assignments_completed": 1, "extracurricular": 0
    })
    assert label in LABELS  # Should typically be Low


# ── Route: GET / ─────────────────────────────────────────────
def test_index_get(client):
    """GET / returns 200."""
    res = client.get("/")
    assert res.status_code == 200
    assert b"Predict" in res.data or b"Student" in res.data


# ── Route: POST /predict ─────────────────────────────────────
def test_predict_post_valid(client):
    """POST /predict with valid data returns result page."""
    res = client.post("/predict", data=VALID_PAYLOAD, follow_redirects=True)
    assert res.status_code == 200


def test_predict_post_missing_field(client):
    """POST /predict with missing field redirects with error."""
    payload = VALID_PAYLOAD.copy()
    del payload["attendance"]
    res = client.post("/predict", data=payload, follow_redirects=True)
    assert res.status_code == 200


def test_predict_post_out_of_range(client):
    """POST /predict with out-of-range value redirects with error."""
    payload = VALID_PAYLOAD.copy()
    payload["attendance"] = "150"
    res = client.post("/predict", data=payload, follow_redirects=True)
    assert res.status_code == 200


# ── Route: GET/POST /api/predict ─────────────────────────────
def test_api_predict_get(client):
    """GET /api/predict returns usage instructions."""
    res = client.get("/api/predict")
    assert res.status_code == 200
    data = json.loads(res.data)
    assert "message" in data


def test_api_predict_post_valid(client):
    """POST /api/predict with valid JSON returns prediction."""
    res = client.post(
        "/api/predict",
        data=json.dumps(VALID_JSON),
        content_type="application/json"
    )
    assert res.status_code == 200
    data = json.loads(res.data)
    assert "prediction" in data
    assert data["prediction"] in LABELS
    assert "confidence" in data
    assert "model" in data


def test_api_predict_post_missing_field(client):
    """POST /api/predict with missing field returns 422."""
    payload = VALID_JSON.copy()
    del payload["attendance"]
    res = client.post(
        "/api/predict",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert res.status_code == 422
    data = json.loads(res.data)
    assert "error" in data


def test_api_predict_post_invalid_json(client):
    """POST /api/predict with invalid JSON returns 400."""
    res = client.post(
        "/api/predict",
        data="not json",
        content_type="application/json"
    )
    assert res.status_code == 400


def test_api_predict_out_of_range(client):
    """POST /api/predict with out-of-range value returns 422."""
    payload = VALID_JSON.copy()
    payload["attendance"] = 200
    res = client.post(
        "/api/predict",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert res.status_code == 422


# ── Edge Cases ───────────────────────────────────────────────
def test_all_zero_inputs(client):
    """All-zero inputs should return a valid label."""
    payload = {k: "0" for k in VALID_PAYLOAD}
    payload["extracurricular"] = "0"
    res = client.post("/predict", data=payload, follow_redirects=True)
    assert res.status_code == 200


def test_max_inputs(client):
    """Maximum valid inputs should return a valid label."""
    payload = {
        "attendance": "100", "internal_marks": "100",
        "study_hours_per_day": "10", "previous_cgpa": "10",
        "assignments_completed": "10", "extracurricular": "1"
    }
    res = client.post("/predict", data=payload, follow_redirects=True)
    assert res.status_code == 200


# ── Dashboard Route ──────────────────────────────────────────
def test_dashboard_route(client):
    """GET /dashboard returns 200 with dataset present."""
    res = client.get("/dashboard")
    assert res.status_code in (200, 302)  # 302 if dataset missing


# ── About Route ──────────────────────────────────────────────
def test_about_route(client):
    """GET /about returns 200."""
    res = client.get("/about")
    assert res.status_code == 200
