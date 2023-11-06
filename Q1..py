# 1) store marks of 5 subjects
# 	here use marks as actual data and subject names as indexes.
# accept both marks and subjects from the user.
import pandas as pd
subject_marks={}

for i in range(0,5):
    subject_names=input(f"Enter the sub names{i+1}:")
    marks=float(input(f"Enter the {subject_names} marks:"))
    subject_marks[subject_names] = marks

print("Subject Marks:")
for subject,marks in subject_marks.items():
    print(f"{subject}:{marks}")

harsha=pd.Series(subject_marks)
print(harsha)

