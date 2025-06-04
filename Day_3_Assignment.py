student = {"name": ["ARPIT", "DIVYA"], "marks": [50, 49]}


def add_name():
    name = input("Enter name: ")
    student[name] = None
    print(f"{name} added successfully.")


def add_marks():
    name = input("Enter the name of the student: ")
    if name in student:
        marks = int(input("Enter marks of the student: "))
        student[name] = marks
        print(f"Marks for {name} added successfully.")
    else:
        print(f"Student {name} not found. Please add the student first.")


def update_marks():
    name = input("Enter the name of the student for updating marks: ")
    if name in student:
        marks = int(input("Enter new marks for the student: "))
        student[name] = marks
        print(f"Marks for {name} updated successfully.")
    else:
        print(f"Student {name} not found.")


def topper():
    if not student:
        print("No data exists to find the topper.")
        return

    max_marks = -1
    topper_name = None

    for name, marks in student.items():
        if marks is not None and marks > max_marks:
            max_marks = marks
            topper_name = name

    if topper_name:
        print(f"Topper is {topper_name} with {max_marks} marks.")
    else:
        print("No marks data available to find topper.")


def delete_name():
    name = input("Enter name of student you want to delete: ")
    if name in student:
        student.pop(name)
        print(f"{name} has been deleted.")
    else:
        print("Student record not found.")


def start():
    while True:
        print("\n__Student Marks Management System__")
        print("1. Add Name")
        print("2. Add Marks")
        print("3. Update Marks")
        print("4. View All Students")
        print("5. Delete Student name")
        print("6. Find Topper")
        print("7. Exit and Stop")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_name()
        elif choice == "2":
            add_marks()
        elif choice == "3":
            update_marks()
        elif choice == "4":
            print("\nCurrent Student Records:")
            for name, marks in student.items():
                print(f"{name}: {marks}")
        elif choice == "5":
            delete_name()
        elif choice == "6":
            topper()
        elif choice == "7":
            print("End")
            break
        else:
            print("Invalid Choice")


start()
