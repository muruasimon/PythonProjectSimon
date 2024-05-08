# Define a list of tuples containing information about students
students = [
    ("Alice", 20, "A"),
    ("Bob", 22, "B"),
    ("Charlie", 21, "C"),
    ("David", 23, "A"),
    ("Eve", 19, "B")
]

# Create a dictionary to store student information
student_dict = {}

# Iterate through the list of tuples and populate the dictionary
for name, age, grade in students:
    student_dict[name] = {"age": age, "grade": grade}

# Print the student dictionary
print("Student Dictionary:")
print(student_dict)
print()

# Create a list of unique grades using a set
unique_grades = {info["grade"] for info in student_dict.values()}

# Print the unique grades
print("Unique Grades:")
print(unique_grades)
print()

# Create a list of tuples containing student names and ages
student_names_and_ages = [(name, info["age"]) for name, info in student_dict.items()]

# Print the list of tuples
print("Student Names and Ages:")
print(student_names_and_ages)
