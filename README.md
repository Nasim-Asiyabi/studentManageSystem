# 📚 Student Management System

> A comprehensive command-line Student Management System built with Python for educational institutions to manage student records, courses, enrollments, and academic performance.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

---

## ✨ Features

### 👨‍🎓 Student Management
- **Add Student** - Register new students with ID, name, age, and major
- **View Students** - Display complete list of all enrolled students
- **Search Student** - Find specific students by their unique ID
- **Edit Student** - Update student information (name, age, major)
- **Delete Student** - Remove students from the system permanently

### 📚 Course Management
- **Add Course** - Create new courses with code, name, and credit units
- **View Courses** - Display all available courses in the system
- **Delete Course** - Remove courses from the system

### 📝 Course Enrollment
- **Select Course** - Enroll students in available courses
- **Remove Course** - Drop courses from a student's schedule
- **View Student Courses** - Display all courses a student is enrolled in with total credit units

### 📊 Grade Management
- **Add Grade** - Assign grades (0-20 scale) to students for specific courses
- **Report Card** - Generate comprehensive report cards with GPA calculation

---

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher installed on your system

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   ```

2. **Navigate to project directory**
   ```bash
   cd student-management-system
   ```

3. **Run the application**
   ```bash
   python student_management.py
   ```

---

## 💻 Usage

### Quick Start
1. Launch the application
2. Navigate through the menu using number inputs
3. Follow on-screen prompts to perform operations
4. All changes are automatically saved to JSON files

### Main Menu
```
========================================
STUDENT MANAGEMENT SYSTEM
========================================
1. Add Student
2. Show Students
3. Search Student
4. Edit Student
5. Delete Student

Course Management
6. Add Course
7. Show Courses
8. Delete Course

Course Selection
9. Select Course
10. Remove Student Course
11. Show Student Courses

Grades
12. Add Grade
13. Show Report Card

0. Exit
```

### Sample Report Card
```
===== REPORT CARD =====
ID: STU001
Name: John Doe
Major: Computer Science

Courses
--------------------------------------------------
CS101 | Programming Fundamentals | 3 Units | Grade: 17.5
CS102 | Data Structures | 4 Units | Grade: 15.0
--------------------------------------------------

GPA: 16.07
```

---

## 📁 Data Structure

### Student Object
```json
{
  "id": "STU001",
  "name": "John Doe",
  "age": "20",
  "major": "Computer Science",
  "courses": [
    {
      "code": "CS101",
      "name": "Programming Fundamentals",
      "units": 3,
      "grade": 17.5
    }
  ]
}
```

### Course Object
```json
{
  "code": "CS101",
  "name": "Programming Fundamentals",
  "units": 3
}
```

### Files
- `students.json` - Stores all student records
- `courses.json` - Stores all course information

---

## 🛠️ Technologies Used

- **Python 3.6+** - Core programming language
- **JSON** - Data storage format
- **OS Module** - File system operations
- **JSON Module** - Data serialization/deserialization

### Dependencies
```
No external dependencies required!
Only Python built-in modules are used:
- json
- os
```

---

## 🎯 Future Enhancements

- [ ] Export reports to PDF/Excel
- [ ] Search by multiple criteria
- [ ] Batch import/export of data
- [ ] Graphical user interface (GUI)
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] User authentication and roles
- [ ] Email notifications
- [ ] Statistics and analytics dashboard
- [ ] Cloud sync across devices
- [ ] Attendance tracking
- [ ] Payment management

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📞 Contact

**Author:** Nasim Asiyabi
**GitHub:** [NasimASiyabi](https://github.com/Nasim-Asiyabi)  


## 🙏 Acknowledgments

- Built as a comprehensive learning project
- Demonstrates core Python concepts including file I/O, JSON handling, and modular programming
- Designed for educational institutions to manage student data efficiently

---

## ⭐ Support

If you find this project useful, please give it a star! ⭐

---

**Made with ❤️ and Python**
