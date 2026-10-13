import pandas as pd
import numpy as np

# Student Data
data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Bashira", "Rahul", "Priya", "Arjun", "Sneha"],
    "Python": [85, 72, 90, 65, 78],
    "SQL": [80, 75, 88, 60, 82],
    "DSA": [78, 70, 92, 55, 80],
    "Attendance": [92, 85, 96, 72, 88]
}

# Pandas DataFrame
df = pd.DataFrame(data)

# Total Marks
df["Total"] = df[["Python", "SQL", "DSA"]].sum(axis=1)

# Average using NumPy
df["Average"] = np.round(
    df[["Python", "SQL", "DSA"]].mean(axis=1), 2
)

# Grade using NumPy
df["Grade"] = np.select(
    [
        df["Average"] >= 90,
        df["Average"] >= 80,
        df["Average"] >= 70,
        df["Average"] >= 60
    ],
    ["A+", "A", "B", "C"],
    default="D"
)

# Pass / Fail
df["Result"] = np.where(
    df["Average"] >= 40,
    "Pass",
    "Fail"
)

# Attendance Status
df["Attendance_Status"] = np.where(
    df["Attendance"] >= 75,
    "Eligible",
    "Shortage"
)

# Display Report
print("\n===== STUDENT PERFORMANCE REPORT =====")
print(df.to_string(index=False))

# Class Statistics
print("\n===== CLASS STATISTICS =====")
print("Total Students:", len(df))
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Average:", df["Average"].max())
print("Lowest Average:", df["Average"].min())

# Topper
topper = df.loc[df["Average"].idxmax()]

print("\n===== TOPPER =====")
print("Name:", topper["Name"])
print("Average:", topper["Average"])
print("Grade:", topper["Grade"])

# Students above 80
print("\n===== STUDENTS ABOVE 80 =====")

high_students = df[df["Average"] > 80]

print(
    high_students[
        ["Name", "Average", "Grade"]
    ].to_string(index=False)
)

# Attendance shortage
print("\n===== ATTENDANCE SHORTAGE =====")

shortage = df[df["Attendance"] < 75]

print(
    shortage[
        ["Name", "Attendance"]
    ].to_string(index=False)
)

# Subject Averages using NumPy
python_avg = np.mean(df["Python"])
sql_avg = np.mean(df["SQL"])
dsa_avg = np.mean(df["DSA"])

print("\n===== SUBJECT AVERAGES =====")
print("Python:", round(python_avg, 2))
print("SQL:", round(sql_avg, 2))
print("DSA:", round(dsa_avg, 2))

# Save to CSV
df.to_csv(
    "student_performance_report.csv",
    index=False
)

print("\nReport saved successfully!")