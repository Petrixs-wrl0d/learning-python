#student management system 
#1.add a student...input
#2.view all the student in the system
#3.search for a student by his id
#4.delete a student from the system
#5.update a student details
#6.quit the system
#a 'class' of student should have the following attributes: name, age, 1(id), multiple(course), gender and multiple(score)
# validations:
    # an age cannot be negative
    # score must be between zero and 100
    # student id must be unique
    # a name cannot be empty


# print('STUDENT MANAGEMENT SYSTEM')
# print('1. Add a student')
# print('2. View all students')
# print('3. Search for a student by ID')
# print('4. Delete a student from the system')
# print('5. Update a student details')
# print('6. Quit the system')

# choice = input("Enter your choice (1-6): ")


class Student:

    def __init__(self, student_id, name, age, gender, courses, scores):
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if not isinstance(scores, list) or any(score < 0 or score > 100 for score in scores):
            raise ValueError("Scores must be between 0 and 100.")

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.age = int(age)
        self.gender = gender.strip()
        self.courses = courses
        self.scores = scores

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Student ID: {self.student_id}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Courses: {self.courses}\n"
            f"Scores: {self.scores}\n"
        )


studentS = []


def parse_list(value):
    if not value.strip():
        return []
    return [item.strip() for item in value.split(',') if item.strip()]


def add_student():

    student_obj = {}

    student_id = input("Enter student ID: ").strip()
    if student_id in studentS:
        print(f"This student ID [{student_id}] already exists in the system.")
        return

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    age_text = input("Enter age: ").strip()
    if not age_text or not age_text.isdigit():
        print("Error: age must be a number.")
        return

    age = int(age_text)
    if age < 0:
        print("Age cannot be negative. Try again.")
        return

    gender = input("Enter student gender: ").strip()
    if not gender:
        print("Gender cannot be empty.")
        return

    course_text = input("Enter courses separated by commas: ").strip()
    courses = parse_list(course_text)

    score_text = input("Enter scores separated by commas: ").strip()
    score_values = []
    if score_text:
        try:
            score_values = [int(score.strip()) for score in score_text.split(',') if score.strip()]
        except ValueError:
            print("Scores must be numbers between 0 and 100.")
            return

    try:
        new_student = Student(student_id, name, age, gender, courses, score_values)
    except ValueError as exc:
        print(exc)
        return

    studentS[student_id] = new_student
    print(f"Student {name} added successfully.")

    add_student() = student_obj
    studentS.push


def view_all_students():
    # if studentS:
    #     print("No students in the system.")
    #     return

    # for student in studentS.values():
        print(studentS)


def search_student():
    student_id = input("Enter student ID to search: ").strip()
    student = studentS.get(student_id)
    if student is None:
        print("No student found with that ID.")
        return
    print(student)


def delete_student():
    student_id = input("Enter student ID to delete: ").strip()
    if student_id not in studentS:
        print("This user is not found with this ID.")
        return

    confirm = input("Are you sure you want to delete this user? (y/n): ").strip().lower()
    if confirm == "y":
        del studentS[student_id]
        print("Student deleted.")
    else:
        print("Unable to delete.")


def update_student():
    student_id = input("Enter student ID: ").strip()
    student = studentS.get(student_id)
    if student is None:
        print("No student found with this ID.")
        return

    new_name = input(f"Name [{student.name}]: ").strip()
    if new_name:
        student.name = new_name

    new_age_text = input(f"Age [{student.age}]: ").strip()
    if new_age_text:
        try:
            new_age = int(new_age_text)
        except ValueError:
            print("Age must be a number.")
            return
        if new_age < 0:
            print("Age cannot be negative.")
            return
        student.age = new_age

    new_gender = input(f"Gender [{student.gender}]: ").strip()
    if new_gender:
        student.gender = new_gender

    new_courses = input(f"Courses [{student.courses}]: ").strip()
    if new_courses:
        student.courses = parse_list(new_courses)

    new_scores = input(f"Scores [{student.scores}]: ").strip()
    if new_scores:
        try:
            parsed_scores = [int(score.strip()) for score in new_scores.split(',') if score.strip()]
        except ValueError:
            print("Scores must be numbers between 0 and 100.")
            return
        if any(score < 0 or score > 100 for score in parsed_scores):
            print("Scores must be between 0 and 100.")
            return
        student.scores = parsed_scores

    print("Student details updated successfully.")


def main():
    actions = {
        "1": add_student,
        "2": view_all_students,
        "3": search_student,
        "4": delete_student,
        "5": update_student,
    }

    while True:
        print("\nSTUDENT MANAGEMENT SYSTEM")
        print("1. Add a student")
        print("2. View all students")
        print("3. Search for a student by ID")
        print("4. Delete a student from the system")
        print("5. Update a student details")
        print("6. Quit the system")

        choice = input("Enter your choice (1-6): ").strip()
        if choice == "6":
            print("GOODBYE")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice.")
            continue

        action()


if __name__ == "__main__":
    main()

        
     
