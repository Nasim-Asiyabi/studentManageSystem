import json
import os

STUDENTS_FILE = "students.json"
COURSES_FILE = "courses.json"


# =========================
# UI HELPERS
# =========================

def header(title):
    print("\n" + "=" * 55)
    print(f" {title}")
    print("=" * 55)


def line():
    print("-" * 55)


def success(msg):
    print(f"✅ {msg}")


def error(msg):
    print(f"❌ {msg}")


def continue_prompt():
    choice = input("\n👉 Do you want to continue? (y/n): ").lower()

    if choice == "y":
        return True
    else:
        print("\n👋 Exiting program...")
        exit()


# =========================
# FILE HANDLING
# =========================

def load_students():
    if not os.path.exists(STUDENTS_FILE):
        return []

    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def save_students(students):
    with open(STUDENTS_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)


def load_courses():
    if not os.path.exists(COURSES_FILE):
        return []

    try:
        with open(COURSES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def save_courses(courses):
    with open(COURSES_FILE, "w", encoding="utf-8") as file:
        json.dump(courses, file, indent=4, ensure_ascii=False)


# =========================
# STUDENT MANAGEMENT
# =========================

def add_student():

    students = load_students()

    header("ADD STUDENT")

    student_id = input("ID: ")

    for s in students:
        if s["id"] == student_id:
            error("This ID already exists!")
            return continue_prompt()

    name = input("Name: ")
    age = input("Age: ")
    major = input("Major: ")

    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "major": major,
        "courses": []
    }

    students.append(new_student)
    save_students(students)

    success("Student added successfully!")

    return continue_prompt()


def show_students():

    students = load_students()

    header("STUDENTS LIST")

    if len(students) == 0:
        error("No students found.")
        return continue_prompt()

    for s in students:
        line()
        print(f"🆔 ID    : {s['id']}")
        print(f"👤 Name  : {s['name']}")
        print(f"🎂 Age   : {s['age']}")
        print(f"📚 Major : {s['major']}")

    line()

    return continue_prompt()


def search_student():

    students = load_students()

    header("SEARCH STUDENT")

    student_id = input("Enter ID: ")

    for s in students:
        if s["id"] == student_id:

            success("Student Found")
            line()

            print(f"🆔 ID   : {s['id']}")
            print(f"👤 Name : {s['name']}")
            print(f"🎂 Age  : {s['age']}")
            print(f"📚 Major: {s['major']}")

            return continue_prompt()

    error("Student not found")

    return continue_prompt()


def edit_student():

    students = load_students()

    header("EDIT STUDENT")

    student_id = input("Enter ID: ")

    for s in students:
        if s["id"] == student_id:

            print("\n(Press Enter to keep old value)")

            new_name = input(f"Name ({s['name']}): ")
            new_age = input(f"Age ({s['age']}): ")
            new_major = input(f"Major ({s['major']}): ")

            if new_name:
                s["name"] = new_name
            if new_age:
                s["age"] = new_age
            if new_major:
                s["major"] = new_major

            save_students(students)

            success("Student updated successfully!")

            return continue_prompt()

    error("Student not found")

    return continue_prompt()


def delete_student():

    students = load_students()

    header("DELETE STUDENT")

    student_id = input("Enter ID: ")

    for s in students:
        if s["id"] == student_id:

            students.remove(s)
            save_students(students)

            success("Student deleted successfully!")
            return continue_prompt()

    error("Student not found")

    return continue_prompt()
# =========================
# COURSE MANAGEMENT
# =========================

def add_course():

    courses = load_courses()

    header("ADD COURSE")

    code = input("Course Code: ")

    for c in courses:
        if c["code"] == code:
            error("Course already exists!")
            return continue_prompt()

    name = input("Course Name: ")

    try:
        units = int(input("Units: "))
    except:
        error("Units must be a number")
        return continue_prompt()

    new_course = {
        "code": code,
        "name": name,
        "units": units
    }

    courses.append(new_course)
    save_courses(courses)

    success("Course added successfully!")

    return continue_prompt()


def show_courses():

    courses = load_courses()

    header("COURSES LIST")

    if len(courses) == 0:
        error("No courses found.")
        return continue_prompt()

    for c in courses:
        line()
        print(f"📌 Code : {c['code']}")
        print(f"📖 Name : {c['name']}")
        print(f"⏱ Units: {c['units']}")

    line()

    return continue_prompt()


def delete_course():

    courses = load_courses()

    header("DELETE COURSE")

    code = input("Enter Course Code: ")

    for c in courses:
        if c["code"] == code:

            courses.remove(c)
            save_courses(courses)

            success("Course deleted successfully!")

            return continue_prompt()

    error("Course not found")

    return continue_prompt()


# =========================
# COURSE SELECTION
# =========================

def select_course():

    students = load_students()
    courses = load_courses()

    header("SELECT COURSE")

    student_id = input("Student ID: ")

    student = None
    for s in students:
        if s["id"] == student_id:
            student = s
            break

    if student is None:
        error("Student not found")
        return continue_prompt()

    if len(courses) == 0:
        error("No courses available")
        return continue_prompt()

    print("\n📚 Available Courses")
    line()

    for c in courses:
        print(f"{c['code']} | {c['name']} | {c['units']} units")

    line()

    code = input("Enter Course Code: ")

    course = None
    for c in courses:
        if c["code"] == code:
            course = c
            break

    if course is None:
        error("Course not found")
        return continue_prompt()

    for sc in student["courses"]:
        if sc["code"] == code:
            error("Course already selected")
            return continue_prompt()

    student["courses"].append({
        "code": course["code"],
        "name": course["name"],
        "units": course["units"]
    })

    save_students(students)

    success("Course selected successfully")

    return continue_prompt()


def remove_student_course():

    students = load_students()

    header("REMOVE COURSE")

    student_id = input("Student ID: ")

    for s in students:
        if s["id"] == student_id:

            if len(s["courses"]) == 0:
                error("No courses selected")
                return continue_prompt()

            print("\n📌 Selected Courses")
            line()

            for c in s["courses"]:
                print(f"{c['code']} | {c['name']}")

            line()

            code = input("Enter Course Code: ")

            for c in s["courses"]:
                if c["code"] == code:

                    s["courses"].remove(c)
                    save_students(students)

                    success("Course removed successfully")

                    return continue_prompt()

            error("Course not found")
            return continue_prompt()

    error("Student not found")
    return continue_prompt()


def show_student_courses():

    students = load_students()

    header("STUDENT COURSES")

    student_id = input("Enter Student ID: ")

    for s in students:
        if s["id"] == student_id:

            print(f"\n👤 Name: {s['name']}")
            line()
            
            if len(s["courses"]) == 0:
                error("No courses selected")
                return continue_prompt()

            total_units = 0

            for c in s["courses"]:
                print(f"{c['code']} | {c['name']} | {c['units']} units")
                total_units += c["units"]

            line()
            print(f"📊 Total Units: {total_units}")

            return continue_prompt()

    error("Student not found")

    return continue_prompt()
# =========================
# GRADES SYSTEM
# =========================

def add_grade():

    students = load_students()

    header("ADD GRADE")

    student_id = input("Student ID: ")

    for s in students:
        if s["id"] == student_id:

            if len(s["courses"]) == 0:
                error("No courses selected")
                return continue_prompt()

            print("\n📚 Student Courses")
            line()

            for c in s["courses"]:
                print(f"{c['code']} | {c['name']}")

            line()

            code = input("Enter Course Code: ")

            for c in s["courses"]:
                if c["code"] == code:

                    try:
                        grade = float(input("Enter Grade (0-20): "))
                    except:
                        error("Invalid grade")
                        return continue_prompt()

                    if grade < 0 or grade > 20:
                        error("Grade must be between 0 and 20")
                        return continue_prompt()

                    c["grade"] = grade

                    save_students(students)

                    success("Grade saved successfully")

                    return continue_prompt()

            error("Course not found")

            return continue_prompt()

    error("Student not found")

    return continue_prompt()


# =========================
# GPA CALCULATION
# =========================

def calculate_gpa(student):

    total_units = 0
    total_points = 0

    for c in student["courses"]:

        if "grade" in c:

            total_units += c["units"]
            total_points += c["grade"] * c["units"]

    if total_units == 0:
        return 0

    return total_points / total_units


# =========================
# REPORT CARD
# =========================

def show_report_card():

    students = load_students()

    header("REPORT CARD")

    student_id = input("Enter Student ID: ")

    for s in students:
        if s["id"] == student_id:

            print(f"\n🆔 ID   : {s['id']}")
            print(f"👤 Name : {s['name']}")
            print(f"📚 Major: {s['major']}")

            line()

            print("📖 Courses:")

            for c in s["courses"]:

                grade = c.get("grade", "Not set")

                print(
                    f"{c['code']} | "
                    f"{c['name']} | "
                    f"{c['units']} units | "
                    f"⭐ {grade}"
                )

            line()

            gpa = calculate_gpa(s)

            print(f"📊 GPA: {round(gpa, 2)}")

            return continue_prompt()

    error("Student not found")

    return continue_prompt()


# =========================
# MAIN MENU
# =========================

def main_menu():

    while True:

        print("\n" + "=" * 55)
        print("🎓 STUDENT MANAGEMENT SYSTEM")
        print("=" * 55)

        print("\n👨‍🎓 Students")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Edit Student")
        print("5. Delete Student")

        print("\n📚 Courses")
        print("6. Add Course")
        print("7. Show Courses")
        print("8. Delete Course")

        print("\n🧑‍🎓 Selection")
        print("9. Select Course")
        print("10. Remove Course")
        print("11. Show Student Courses")

        print("\n📝 Grades")
        print("12. Add Grade")
        print("13. Show Report Card")

        print("\n0. Exit")

        choice = input("\n👉 Choose option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            edit_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            add_course()

        elif choice == "7":
            show_courses()

        elif choice == "8":
            delete_course()

        elif choice == "9":
            select_course()
        elif choice == "10":
            remove_student_course()

        elif choice == "11":
            show_student_courses()

        elif choice == "12":
            add_grade()

        elif choice == "13":
            show_report_card()

        elif choice == "0":
            print("\n👋 Goodbye!")
            break

        else:
            error("Invalid option")


# =========================
# START PROGRAM
# =========================

main_menu()

