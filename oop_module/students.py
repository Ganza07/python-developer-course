class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        all_grades = [g for grades in self.grades.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade():.1f}"

    def __eq__(self, other):
        return isinstance(other, Lecturer) and self._average_grade() == other._average_grade()

    def __lt__(self, other):
        return isinstance(other, Lecturer) and self._average_grade() < other._average_grade()

    def __gt__(self, other):
        return isinstance(other, Lecturer) and self._average_grade() > other._average_grade()

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _average_grade(self):
        all_grades = [g for grades in self.grades.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        courses = ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет"
        finished = ", ".join(self.finished_courses) if self.finished_courses else "Нет"
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self._average_grade():.1f}\n"
                f"Курсы в процессе изучения: {courses}\n"
                f"Завершенные курсы: {finished}")

    def __eq__(self, other):
        return isinstance(other, Student) and self._average_grade() == other._average_grade()

    def __lt__(self, other):
        return isinstance(other, Student) and self._average_grade() < other._average_grade()

    def __gt__(self, other):
        return isinstance(other, Student) and self._average_grade() > other._average_grade()

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_hw_grade(students_list, course_name):
    total = 0
    count = 0
    for student in students_list:
        if course_name in student.grades:
            total += sum(student.grades[course_name])
            count += len(student.grades[course_name])
    return round(total / count, 2) if count else 0


def average_lecture_grade(lecturers_list, course_name):
    total = 0
    count = 0
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            total += sum(lecturer.grades[course_name])
            count += len(lecturer.grades[course_name])
    return round(total / count, 2) if count else 0


if __name__ == "__main__":
    # 1. Создаём по 2 экземпляра каждого класса
    stu1 = Student('Иван', 'Иванов', 'м')
    stu2 = Student('Мария', 'Петрова', 'ж')
    lec1 = Lecturer('Алексей', 'Сидоров')
    lec2 = Lecturer('Елена', 'Кузнецова')
    rev1 = Reviewer('Дмитрий', 'Волков')
    rev2 = Reviewer('Ольга', 'Смирнова')

    # Настраиваем курсы
    for s in [stu1, stu2]:
        s.courses_in_progress = ['Python', 'Git']
        s.finished_courses = ['Введение в программирование']
    for l in [lec1, lec2]:
        l.courses_attached = ['Python']
    for r in [rev1, rev2]:
        r.courses_attached = ['Python']

    # 2. Вызываем методы выставления оценок
    rev1.rate_hw(stu1, 'Python', 9)
    rev1.rate_hw(stu1, 'Python', 10)
    rev2.rate_hw(stu2, 'Python', 8)
    rev2.rate_hw(stu2, 'Python', 9)

    stu1.rate_lecture(lec1, 'Python', 9)
    stu2.rate_lecture(lec1, 'Python', 10)
    stu1.rate_lecture(lec2, 'Python', 8)
    stu2.rate_lecture(lec2, 'Python', 9)

    # 3. Вызываем магические методы (__str__ через print, сравнение через операторы)
    print("=== Студенты (__str__) ===")
    print(stu1)
    print(stu2)
    print("\n=== Лекторы (__str__) ===")
    print(lec1)
    print(lec2)
    print("\n=== Ревьюеры (__str__) ===")
    print(rev1)
    print(rev2)

    print("\n=== Сравнение (__eq__, __lt__) ===")
    print(f"lec1 == lec2: {lec1 == lec2}")
    print(f"stu1 > stu2: {stu1 > stu2}")

    # 4. Вызываем новые функции
    print("\n=== Полевые испытания (функции) ===")
    print(f"Средняя оценка за ДЗ по Python: {average_hw_grade([stu1, stu2], 'Python')}")
    print(f"Средняя оценка за лекции по Python: {average_lecture_grade([lec1, lec2], 'Python')}")

    # 5. Доработка - демонстрация отказов
    print("\n=== Тестирование отказов (Вывод: 'Ошибка') ===")

    # Отказ по роли: Студент пытается оценить ревьюера (а должен лектора)
    print(f"stu1.rate_lecture(rev1, 'Python', 5): {stu1.rate_lecture(rev1, 'Python', 5)}")

    # Отказ по курсу: Лектор не ведет 'Java'
    print(f"stu1.rate_lecture(lec1, 'Java', 8): {stu1.rate_lecture(lec1, 'Java', 8)}")
