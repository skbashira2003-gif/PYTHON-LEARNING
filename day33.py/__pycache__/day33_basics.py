
import matplotlib.pyplot as plt

# Data
subjects = ["Python", "SQL", "NumPy", "Pandas"]
marks = [85, 90, 75, 80]

# 1. Line Chart
plt.plot(subjects, marks, marker="o")
plt.title("Student Marks - Line Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid()
plt.show()

# 2. Bar Chart
plt.bar(subjects, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 3. Scatter Plot
plt.scatter(subjects, marks)
plt.title("Student Marks - Scatter Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 4. Pie Chart
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Student Marks - Pie Chart")
plt.show()

# 5. Histogram
plt.hist(marks, bins=4)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Save chart
plt.bar(subjects, marks)
plt.savefig("student_marks.png")
plt.show()