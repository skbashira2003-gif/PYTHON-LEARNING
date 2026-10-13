
import numpy as np
import pandas as pd

# Student details
data = {
    "Name": ["Bashira", "Ravi", "Rakesh", "Priya", "Suresh"],
    "Python": [85, 45, 90, 78, 32],
    "SQL": [90, 55, 88, 82, 40],
    "NumPy": [80, 60, 95, 75, 35]
}

# Create DataFrame using Pandas
df = pd.DataFrame(data)

# Calculate total marks using NumPy
marks = df[["Python", "SQL", "NumPy"]].to_numpy()

df["Total"] = np.sum(marks, axis=1)
df["Average"] = np.mean(marks, axis=1).round(2)

# Add result column
df["Result"] = np.where(df["Average"] >= 40, "Pass", "Fail")

print("STUDENT PERFORMANCE ANALYSIS")
print(df)

# Overall statistics
print("\nCLASS STATISTICS")
print("Highest Total:", np.max(df["Total"]))
print("Lowest Total:", np.min(df["Total"]))
print("Class Average:", round(np.mean(df["Average"]), 2))

# Students scoring above 80 average
print("\nSTUDENTS SCORING ABOVE 80")
print(df[df["Average"] > 80][["Name", "Average"]])

# Sort students by total marks
print("\nSTUDENTS RANKING")
print(df.sort_values("Total", ascending=False)[["Name", "Total"]])

# Save results to CSV
df.to_csv("student_performance.csv", index=False)

print("\nReport saved to student_performance.csv")
