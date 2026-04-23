import pandas as pd
import numpy as np
import random
import os

random.seed(42)
np.random.seed(42)

INDIAN_FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Reyansh", "Sai", "Ayaan",
    "Krishna", "Ishaan", "Shaurya", "Atharv", "Advik", "Pranav", "Dhruv",
    "Ananya", "Diya", "Priya", "Meera", "Riya", "Sneha", "Pooja", "Kavya",
    "Divya", "Nisha", "Tanvi", "Shreya", "Aisha", "Rhea", "Zara", "Isha",
    "Rohan", "Rahul", "Amit", "Raj", "Dev", "Kiran", "Nikhil", "Kunal", "Harsh",
    "Sakshi", "Swati", "Neha", "Ankita", "Komal", "Simran", "Payal", "Ritika",
    "Gaurav", "Siddharth", "Yash", "Varun", "Deepak", "Suresh", "Ramesh"
]

INDIAN_LAST_NAMES = [
    "Sharma", "Verma", "Gupta", "Singh", "Kumar", "Patel", "Shah", "Mehta",
    "Joshi", "Nair", "Reddy", "Rao", "Iyer", "Pillai", "Menon", "Krishnan",
    "Chatterjee", "Banerjee", "Mukherjee", "Das", "Bose", "Roy", "Ghosh",
    "Mishra", "Pandey", "Tiwari", "Tripathi", "Shukla", "Chaudhary", "Yadav",
    "Agarwal", "Jain", "Saxena", "Srivastava", "Kapoor", "Malhotra", "Khanna",
    "Bhatia", "Arora", "Bajaj", "Chopra", "Sethi", "Tandon", "Walia", "Dhawan"
]

def generate_name():
    return f"{random.choice(INDIAN_FIRST_NAMES)} {random.choice(INDIAN_LAST_NAMES)}"

def assign_performance(attendance, internal_marks, study_hours):
    if attendance >= 75 and internal_marks >= 70 and study_hours >= 5:
        return "High"
    elif attendance < 60 or internal_marks < 50:
        return "Low"
    else:
        return "Average"

def generate_dataset(n=1000):
    rows = []
    for i in range(1, n + 1):
        attendance = round(random.uniform(40, 100), 2)
        internal_marks = round(random.uniform(30, 100), 2)
        study_hours = round(random.uniform(0, 10), 2)
        previous_cgpa = round(random.uniform(4.0, 10.0), 2)
        assignments_completed = random.randint(0, 10)
        extracurricular = random.randint(0, 1)
        performance = assign_performance(attendance, internal_marks, study_hours)

        rows.append({
            "student_id": i,
            "name": generate_name(),
            "attendance": attendance,
            "internal_marks": internal_marks,
            "study_hours_per_day": study_hours,
            "previous_cgpa": previous_cgpa,
            "assignments_completed": assignments_completed,
            "extracurricular": extracurricular,
            "performance": performance
        })

    df = pd.DataFrame(rows)
    return df

if __name__ == "__main__":
    output_path = os.path.join(os.path.dirname(__file__), "..", "dataset", "students.csv")
    df = generate_dataset(1000)
    df.to_csv(output_path, index=False)
    print(f"Dataset generated: {len(df)} rows")
    print(df["performance"].value_counts())
