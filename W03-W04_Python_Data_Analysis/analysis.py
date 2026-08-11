import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. PYTHON ESSENTIALS
# Functions, OOP, List Comprehension, Dictionary Comprehension
# ============================================================

def calculate_average(marks):
    return sum(marks) / len(marks)


class StudentAnalyzer:
    def __init__(self, students):
        self.students = students

    def total_students(self):
        return len(self.students)

    def average_marks(self):
        marks = [student["Marks"] for student in self.students]
        return calculate_average(marks)


students = [
    {"Name": "Aarav", "Marks": 85},
    {"Name": "Ananya", "Marks": 78},
    {"Name": "Riya", "Marks": 91}
]

# List comprehension
passed_students = [
    student["Name"]
    for student in students
    if student["Marks"] >= 40
]

# Dictionary comprehension
student_scores = {
    student["Name"]: student["Marks"]
    for student in students
}

analyzer = StudentAnalyzer(students)

print("========== PYTHON ESSENTIALS ==========")
print("Total students:", analyzer.total_students())
print("Average marks:", analyzer.average_marks())
print("Passed students:", passed_students)
print("Student scores:", student_scores)


# ============================================================
# 2. NUMPY
# Arrays, Vectorized Operations, Broadcasting
# ============================================================

marks_array = np.array([85, 78, 91, 67, 73, 88, 95, 72, 81, 64])

print("\n========== NUMPY ==========")
print("NumPy Array:", marks_array)

# Vectorized operation
percentage = marks_array / 100
print("Percentage:", percentage)

# Broadcasting
bonus_marks = marks_array + 5
print("Marks after bonus:", bonus_marks)

print("Average using NumPy:", np.mean(marks_array))


# ============================================================
# 3. PANDAS
# DataFrame, Cleaning, Merging, GroupBy
# ============================================================

df = pd.read_csv("data/students.csv")

print("\n========== PANDAS ==========")
print("\nStudent Data:")
print(df)

# Data cleaning
df = df.drop_duplicates()
df = df.dropna()

print("\nCleaned Data:")
print(df)

# GroupBy
department_avg = df.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(department_avg)


# ============================================================
# 4. PANDAS MERGING
# ============================================================

assessments = pd.read_csv("data/assessments.csv")

merged_df = pd.merge(
    df,
    assessments,
    on="Student_ID"
)

print("\nMerged Data:")
print(merged_df)


# ============================================================
# 5. DATA VISUALIZATION
# Matplotlib and Seaborn
# ============================================================

# Create output directory if needed
import os

os.makedirs("output", exist_ok=True)


# Matplotlib - Average marks by department
department_avg.plot(kind="bar")

plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.tight_layout()

plt.savefig("output/department_average.png")
plt.close()


# Seaborn - Marks distribution
sns.histplot(
    df["Marks"],
    bins=5,
    kde=True
)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()

plt.savefig("output/marks_distribution.png")
plt.close()


# Seaborn - Attendance vs Marks
sns.scatterplot(
    data=df,
    x="Attendance",
    y="Marks",
    hue="Department"
)

plt.title("Attendance vs Marks")
plt.tight_layout()

plt.savefig("output/attendance_vs_marks.png")
plt.close()


print("\n========== VISUALIZATION ==========")
print("Visualizations saved in the output folder.")

print("\n========== PROJECT COMPLETE ==========")