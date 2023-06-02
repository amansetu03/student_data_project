from tabulate import tabulate
class Student:
    def __init__(self, name, roll,email,marks):
        self.name = name
        self.roll = roll
        self.email= email
        self.marks = marks
        

class Method:
    def __init__(self, file_name):
        self.file_name = file_name
        
    def enter_marsk(self):
        marks = []
        try:
            for i in range(5):
                mark = float(input("Enter marks for subject {}: ".format(i + 1)))
                marks.append(mark)
        except:
            print("you enter invalid marks enter valid marks again ")
            return self.enter_marsk()
        else:
            return marks

    def accept_student(self, students):
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        # Check if the roll number already exists or not if exist then function call it self recursivly
        for i in students:
            if i.roll == roll:
                print("Roll number already exists. Please enter a unique roll number.")
                return self.accept_student(students)
        email = input("enter your email: ")
        marks=self.enter_marsk()
        student = Student(name, roll,email, marks)
        students.append(student)
        self.save_students(students)
        return student

    def display_students(self, students):
        if not students:
            print("No records found.")
            return
        print('student data'.center(100,"-"))
        header=["Name", "Roll NO", "Email", "Marks1", "Marks2", "Marks3", "Marks4", "Marks5"]
        data=[]
        for i in students:
            row = [i.name, i.roll, i.email] + i.marks
            data.append(row)
        print(tabulate(data, headers=header, tablefmt="grid"))
        
    def search_student(self, students, roll):
        for i in students:
            if i.roll == roll:
                return i
        return None

    def update_student(self, students, roll):
        for i in students:
            if i.roll == roll:
                print("Enter new details for student with roll number", roll)
                name = input("Enter student name: ")
                email = input("enter your email: ")
                marks = []
                for j in range(5):
                    mark = float(input("Enter marks for subject {}: ".format(j + 1)))
                    marks.append(mark)
                student.name = name
                student.email = email
                student.marks = marks
                self.save_students(students)
                print("Student record updated successfully.")
                return
        print("Student not found.")

    def delete_student(self, students, roll):
        for i in students:
            if i.roll == roll:
                students.remove(i)
                self.save_students(students)
                print("Student record deleted successfully.")
                return
        print("Student not found.")

    def save_students(self, students):
        with open(self.file_name, 'w') as file:
            for i in students:
                student_data = "{},{},{},{}\n".format(i.name,i.roll,i.email, ",".join(str(mark) for mark in i.marks))
                file.write(student_data)

    def load_students(self):
        students = []
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    name = data[0]
                    roll = data[1]
                    email = data[2]
                    marks = [float(mark) for mark in data[3:]]
                    student = Student(name, roll,email, marks)
                    students.append(student)
        except FileNotFoundError:
            print("file not found")
        return students

if __name__ == "__main__":

    file_name = "students.txt"
    method_instance = Method(file_name)
    students = method_instance.load_students()
    print("1. Accept Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")
    while True:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            student = method_instance.accept_student(students)
            print("Student record added successfully.")

        elif choice == 2:
            method_instance.display_students(students)

        elif choice == 3:
            roll = input("Enter roll number to search: ")
            student = method_instance.search_student(students, roll)
            if student:
                print("Student found:")
                data = [
                        ["Name", "Roll NO", "Email", "Marks1", "Marks2", "Marks3", "Marks4", "Marks5"],
                        [student.name, student.roll, student.email, student.marks[0], student.marks[1], student.marks[2], student.marks[3], student.marks[4]]
                        ]
                print(tabulate(data, headers="firstrow", tablefmt="grid"))
                
            else:
                print("Student not found.")

        elif choice == 4:
            roll = input("Enter roll number to update: ")
            method_instance.update_student(students, roll)

        elif choice == 5:
            roll = input("Enter roll number to delete: ")
            method_instance.delete_student(students, roll)

        elif choice == 6:
            break

        else:
            print("Invalid choice. Please try again.")
    print("Program by Aman Kumar Sharma")
    print(" program ended, thank you")
