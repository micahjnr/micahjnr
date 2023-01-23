# Define a dictionary of grades and their corresponding point values
grades = {"A": 5.0, "B": 4.0, "C": 3.0, "D": 2.0, "E": 1.0, "F": 0.0}

# Get the number of courses
num_courses = int(input("Enter the number of courses: "))

# Initialize variables to store the total number of credits and the total point value
total_credits = 0
total_points = 0

# Iterate over the number of courses
for i in range(num_courses):
    # Get the course details
    course_name = input("Enter the name of the course: ")
    course_credits = int(input("Enter the number of credits for the course: "))
    course_grade = input("Enter the grade for the course: ").upper()

    # Check if the entered grade is valid
    if course_grade not in grades:
        print("Invalid grade entered. Please enter a valid grade.")
        continue

    # Add the course credits and point value to the total
    total_credits += course_credits
    total_points += grades[course_grade] * course_credits

# Calculate the CGPA
cgpa = total_points / total_credits

# Print the CGPA
print("Your CGPA is: {:.2f}".format(cgpa))
