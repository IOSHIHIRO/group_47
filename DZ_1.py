class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def  introduce_myself (self):
        print(f'Меня зовут {self.full_name}. Мне {self.age} лет. Я женат/замужем: {self.is_married}')
class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
            if not self.marks:
                return 0
            return sum(self.marks.values()) / len(self.marks)

class Teacher(Person):
    base_salary = 30000
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus_years = max(self.experience - 3, 0)
        bonus = bonus_years * 0.05 * Teacher.base_salary
        return Teacher.base_salary + bonus

EM = Person('emiran',18, 'не замужем')
print(f'Меня зовут {EM.full_name}. Мне {EM.age} лет. Я женат/замужем: {EM.is_married}')


teacher = Teacher("L", 45, 'не замужем', 10, )
print(f"Учитель: {teacher.full_name}")
teacher.introduce_myself()
print(f"Опыт работы: {teacher.experience} лет")
print(f"Зарплата: {teacher.base_salary}")

def create_students():
    students = []
    students.append(Student("Кирей Катамине", 18, 'Не замужем', {"Физра": 5, "Химия": 4, "Литература": 3}))
    students.append(Student("Кира Есикаге", 17, 'Не замужем', {"Анатомия": 4, "География": 5, "Истроия": 4}))
    students.append(Student("Риас Гремори", 19, 'Не замужем', {"Химия": 5, "Информатика": 5, "Алгебра": 5}))
    return students

students = create_students()
for student in students:
    student.introduce_myself()
    Interest = round(student.calculate_average_mark(),1)
    print(f"Оценки: {student.marks}")
    print(f"Средняя оценка: {Interest}")