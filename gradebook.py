# Function to determine letter grade
def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Input
name = input("Enter the student name: ")

grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))
grade4 = float(input("Enter grade 4: "))
grade5 = float(input("Enter grade 5: "))

# Calculate the average
average = (grade1 + grade2 + grade3 + grade4 +grade5) / 5

# Get letter grade
letter = get_letter_grade(average)

# Output
print()
print(name)
print()
print("Average:", average)
print()
print("Letter Grade:", letter)






