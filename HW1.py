class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married
    def introduce_myself (self):
        print(f'ФИО: {self.full_name}\nВозраст: {self.age}\nСемейное положение: {self.is_married}')
class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks
    def introduce_myself(self):
        super().introduce_myself()
        print('Оценки')
        for subject, mark in self.marks.items():
            print(f'{subject}: {mark}')
    def average_mark(self):
        return sum(self.marks.values()) / len(self.marks)
class Teacher(Person):
    base_salary = 30000
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience
    def calculate_salary(self):
        salary = self.base_salary
        if self.experience > 3:
            for _ in range (self.experience - 3):
                salary += salary * 0.05
        return salary
    def introduce_myself(self):
        super().introduce_myself()
        print(f'Зарплата: {self.calculate_salary()}')
def create_students():
    student1 = Student("Максат Иманалиев", 20, 'no', {"Математика": 4, "История": 5, "Биология": 3})
    student2 = Student("Какаши Хатваки", 22, 'no', {"Физика": 3, "Литература": 5, "Английский": 4})
    student3 = Student("Мытык Мытыгович", 19, 'yes', {"Программирование": 5, "Физкультура": 5})
    return [student1, student2, student3]
ff = Teacher("Александра Петровна", 55, 'no', 3)
ff.introduce_myself()
students = create_students()
for student in students:
    student.introduce_myself()