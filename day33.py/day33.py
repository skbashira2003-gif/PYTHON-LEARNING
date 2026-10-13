import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ============================================================
# DAY 34 - MATPLOTLIB BEGINNER PRACTICE
# ============================================================

# ------------------------------------------------------------
# DATA
# ------------------------------------------------------------

students = ["Bashira", "Rahul", "Priya", "Arjun", "Sneha"]
marks = [85, 72, 90, 65, 78]

days = [1, 2, 3, 4, 5]
progress = [60, 70, 65, 80, 90]

subjects = ["Python", "SQL", "DSA"]
subject_marks = [85, 80, 75]

study_hours = [1, 2, 3, 4, 5]
study_marks = [50, 55, 65, 75, 90]


# ============================================================
# TASK 1 - BASIC LINE PLOT
# ============================================================

plt.plot(days, progress)

plt.xlabel("Days")
plt.ylabel("Marks")
plt.title("Student Progress")
plt.grid()

plt.show()


# ============================================================
# TASK 2 - BAR CHART
# ============================================================

plt.bar(students, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()


# ============================================================
# TASK 3 - HORIZONTAL BAR CHART
# ============================================================

plt.barh(students, marks)

plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Student Marks - Horizontal Bar")

plt.show()


# ============================================================
# TASK 4 - PIE CHART
# ============================================================

plt.pie(
    subject_marks,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title("Subject Marks Distribution")

plt.show()


# ============================================================
# TASK 5 - SCATTER PLOT
# ============================================================

plt.scatter(study_hours, study_marks)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.grid()

plt.show()


# ============================================================
# TASK 6 - HISTOGRAM
# ============================================================

all_marks = [45, 50, 55, 60, 65, 70, 72, 75, 80, 85, 90, 95]

plt.hist(all_marks)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")

plt.show()


# ============================================================
# TASK 7 - CUSTOMIZE LINE PLOT
# ============================================================

plt.plot(
    days,
    progress,
    marker="o",
    linestyle="--",
    linewidth=2,
    label="Student Progress"
)

plt.xlabel("Days")
plt.ylabel("Marks")
plt.title("Customized Student Progress")

plt.legend()
plt.grid()

plt.show()


# ============================================================
# TASK 8 - NUMPY + MATPLOTLIB
# ============================================================

numpy_marks = np.array([60, 70, 80, 90, 95])

average = np.mean(numpy_marks)

print("NumPy Marks:", numpy_marks)
print("Average Marks:", average)

plt.plot(numpy_marks, marker="o")

plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.title("NumPy Marks")

plt.show()


# ============================================================
# TASK 9 - PANDAS + MATPLOTLIB
# ============================================================

data = {
    "Name": ["Bashira", "Rahul", "Priya", "Arjun", "Sneha"],
    "Marks": [85, 72, 90, 65, 78]
}

df = pd.DataFrame(data)

print("\nStudent Data:")
print(df)

plt.bar(df["Name"], df["Marks"])

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance")

plt.show()


# ============================================================
# TASK 10 - FIND TOPPER AND PLOT
# ============================================================

topper_index = df["Marks"].idxmax()

topper_name = df.loc[topper_index, "Name"]
topper_marks = df.loc[topper_index, "Marks"]

print("\nTopper:", topper_name)
print("Topper Marks:", topper_marks)

plt.bar(df["Name"], df["Marks"])

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance - Topper")

plt.show()


# ============================================================
# TASK 11 - SAVE GRAPH
# ============================================================

plt.bar(students, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Report")

plt.savefig("student_marks.png")

plt.show()

print("\nGraph saved successfully as student_marks.png")