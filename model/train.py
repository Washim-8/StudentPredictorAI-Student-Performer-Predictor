"""
train.py — Convenience entry point to generate dataset and train model.
Run: python model/train.py
"""
import os
import sys

# Ensure project root is in path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from dataset.generate_dataset import generate_dataset
from model.model import train_and_evaluate

DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "dataset", "students.csv")

if __name__ == "__main__":
    print("=" * 50)
    print("  Student Performer Predictor - Training Pipeline")
    print("=" * 50)

    # Step 1: Generate dataset if it doesn't exist
    if not os.path.exists(DATASET_PATH):
        print("\n[1/2] Generating synthetic dataset...")
        df = generate_dataset(1000)
        df.to_csv(DATASET_PATH, index=False)
        print(f"      Dataset saved: {len(df)} records")
    else:
        print("\n[1/2] Dataset already exists — skipping generation.")

    # Step 2: Train models
    print("\n[2/2] Training models...\n")
    best_model_name, best_score, results, le, scaler = train_and_evaluate()

    print("\n" + "=" * 50)
    print(f"  Training Complete!")
    print(f"  Best Model  : {best_model_name}")
    print(f"  Test Accuracy: {best_score:.4f} ({best_score * 100:.2f}%)")
    print("=" * 50)
