print("================================")
print("   STUDENT PERFORMANCE TRACKER")
print("================================")

subjects = ("Maths", "Science", "Computer")
students = []


def calculate_result(marks):
    total = sum(marks)
    percentage = round(total / len(subjects), 2)

    if percentage >= 75:
        result = "Distinction"
    elif percentage >= 60:
        result = "First Class"
    elif percentage >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return total, percentage, result


def add_student():
    name = input("Enter student name: ")

    marks = []

    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter marks for {subject}: "))

                if mark < 0 or mark > 100:
                    print("Invalid marks! Enter a value between 0 and 100.")
                    continue

                break

            except ValueError:
                print("Please enter numbers only.")

        marks.append(mark)

    total, percentage, result = calculate_result(marks)

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "result": result
    }

    students.append(student)

    print("\nStudent added successfully!")


def view_students():
    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for student in students:
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Percentage:", student["percentage"], "%")
        print("Result:", student["result"])
        print("------------------------------------")


def search_student():
    if len(students) == 0:
        print("\nNo students found.")
        return

    search_name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Total:", student["total"])
            print("Percentage:", student["percentage"], "%")
            print("Result:", student["result"])
            break

    else:
        print("\nStudent not found.")


def delete_student():
    if len(students) == 0:
        print("\nNo students found.")
        return

    delete_name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == delete_name.lower():
            students.remove(student)
            print("\nStudent deleted successfully!")
            break

    else:
        print("\nStudent not found.")


def class_statistics():
    if len(students) == 0:
        print("\nNo students found.")
        return

    total_percentage = 0

    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        total_percentage += student["percentage"]

        if student["percentage"] > highest_student["percentage"]:
            highest_student = student

        if student["percentage"] < lowest_student["percentage"]:
            lowest_student = student

    average_percentage = round(
        total_percentage / len(students), 2
    )

    print("\n========== CLASS STATISTICS ==========")
    print("Total Students:", len(students))
    print("Average Percentage:", average_percentage, "%")
    print(
        "Highest Scorer:",
        highest_student["name"],
        "-",
        highest_student["percentage"],
        "%"
    )
    print(
        "Lowest Scorer:",
        lowest_student["name"],
        "-",
        lowest_student["percentage"],
        "%"
    )


while True:
    print("\n================================")
    print("            MAIN MENU")
    print("================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Class Statistics")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        class_statistics()

    elif choice == "6":
        print("Thank you for using the Student Performance Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")